import cv2
import numpy as np
import os
from pathlib import Path

def remove_background_grabcut(img, iterations=5):
    """
    使用 GrabCut 算法去除背景
    """
    # 创建掩码
    mask = np.zeros(img.shape[:2], np.uint8)
    
    # 创建背景和前景模型
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    
    # 定义矩形区域（假设中心80%区域是前景）
    h, w = img.shape[:2]
    rect = (int(w*0.1), int(h*0.1), int(w*0.8), int(h*0.8))
    
    # 初始化掩码：边缘区域标记为背景，中心区域标记为可能的前景
    mask[:] = cv2.GC_PR_BGD  # 可能背景
    mask[int(h*0.1):int(h*0.9), int(w*0.1):int(w*0.9)] = cv2.GC_PR_FGD  # 可能前景
    mask[int(h*0.2):int(h*0.8), int(w*0.2):int(w*0.8)] = cv2.GC_FGD  # 确定前景
    
    # 运行 GrabCut
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterations, cv2.GC_INIT_WITH_MASK)
    
    # 创建最终掩码（0和2是背景，1和3是前景）
    mask2 = np.where((mask == 2) | (mask == 0), 0, 255).astype('uint8')
    
    return mask2

def remove_background_edges(img):
    """
    使用边缘检测和轮廓填充去除背景
    """
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 使用 Canny 边缘检测
    edges = cv2.Canny(gray, 50, 150)
    
    # 形态学操作来连接边缘
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=2)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=3)
    
    # 查找轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None
    
    # 找到最大的轮廓（假设是前景物体）
    largest_contour = max(contours, key=cv2.contourArea)
    
    # 创建掩码
    mask = np.zeros(gray.shape, np.uint8)
    cv2.fillPoly(mask, [largest_contour], 255)
    
    # 形态学操作来平滑掩码
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    
    return mask

def remove_background_kmeans(img, n_clusters=3):
    """
    使用 OpenCV K-means 颜色聚类来分离前景和背景
    """
    # 重塑图像为像素列表
    h, w = img.shape[:2]
    pixels = img.reshape(-1, 3).astype(np.float32)
    
    # 使用 OpenCV K-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(pixels, n_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    labels = labels.reshape(h, w)
    
    # 假设边缘的像素主要是背景
    edge_pixels = np.concatenate([
        labels[0, :].flatten(),  # 上边缘
        labels[-1, :].flatten(),  # 下边缘
        labels[:, 0].flatten(),  # 左边缘
        labels[:, -1].flatten()  # 右边缘
    ])
    
    # 找到边缘最常见的标签（背景）
    if len(edge_pixels) > 0:
        background_label = np.bincount(edge_pixels.astype(int)).argmax()
    else:
        background_label = 0
    
    # 创建掩码（背景为0，前景为255）
    mask = np.where(labels == background_label, 0, 255).astype('uint8')
    
    return mask

def remove_background_combined(img):
    """
    结合多种方法去除背景
    """
    # 方法1: 尝试 GrabCut
    try:
        mask_grabcut = remove_background_grabcut(img, iterations=5)
        if mask_grabcut is not None and np.sum(mask_grabcut > 0) > img.shape[0] * img.shape[1] * 0.1:
            return mask_grabcut
    except:
        pass
    
    # 方法2: 尝试边缘检测
    try:
        mask_edges = remove_background_edges(img)
        if mask_edges is not None and np.sum(mask_edges > 0) > img.shape[0] * img.shape[1] * 0.1:
            return mask_edges
    except:
        pass
    
    # 方法3: 使用 K-means
    try:
        mask_kmeans = remove_background_kmeans(img, n_clusters=3)
        if mask_kmeans is not None:
            return mask_kmeans
    except:
        pass
    
    # 如果所有方法都失败，返回一个简单的中心区域掩码
    h, w = img.shape[:2]
    mask = np.zeros((h, w), np.uint8)
    cv2.ellipse(mask, (w//2, h//2), (int(w*0.4), int(h*0.4)), 0, 0, 360, 255, -1)
    return mask

def remove_background(image_path, output_path=None):
    """
    移除背景，生成透明PNG图片
    
    参数:
        image_path: 输入图片路径
        output_path: 输出图片路径（如果为None，则覆盖原文件）
    """
    # 读取图片
    img = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    
    if img is None:
        print(f"  错误: 无法读取图片 {image_path}")
        return False
    
    # 使用组合方法创建掩码
    mask = remove_background_combined(img)
    
    # 如果掩码为空，返回False
    if mask is None:
        print(f"  ✗ 无法创建掩码: {Path(image_path).name}")
        return False
    
    # 平滑掩码边缘
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    
    # 创建带透明通道的图像
    bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    bgra[:, :, 3] = mask
    
    # 如果输出路径为None，则覆盖原文件
    if output_path is None:
        output_path = image_path
    
    # 保存为PNG（支持透明通道）
    success = cv2.imwrite(str(output_path), bgra, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    
    if success:
        # 计算前景区域的比例
        foreground_ratio = np.sum(mask > 0) / (mask.shape[0] * mask.shape[1]) * 100
        print(f"  ✓ 已处理: {Path(image_path).name} (前景: {foreground_ratio:.1f}%)")
        return True
    else:
        print(f"  ✗ 保存失败: {Path(image_path).name}")
        return False

def process_directory(directory_path, backup=True):
    """
    处理目录下的所有图片
    
    参数:
        directory_path: 图片目录路径
        backup: 是否创建备份
    """
    directory = Path(directory_path)
    
    # 支持的图片格式（使用大小写不敏感匹配）
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp']
    
    # 获取所有图片文件（去重）
    image_files = set()
    for ext in image_extensions:
        # 匹配小写
        image_files.update(directory.glob(f'*{ext}'))
        # 匹配大写
        image_files.update(directory.glob(f'*{ext.upper()}'))
        # 匹配首字母大写
        image_files.update(directory.glob(f'*{ext.capitalize()}'))
    
    # 转换为列表并排序
    image_files = sorted(list(image_files))
    
    # 排除备份目录中的文件
    backup_dir = directory / 'backup_original'
    image_files = [f for f in image_files if backup_dir not in f.parents]
    
    if not image_files:
        print(f"在 {directory_path} 中未找到图片文件")
        return
    
    print(f"找到 {len(image_files)} 个图片文件\n")
    
    # 创建备份目录
    if backup:
        backup_dir = directory / 'backup_original'
        backup_dir.mkdir(exist_ok=True)
        print(f"备份目录: {backup_dir}\n")
    
    processed_count = 0
    for img_file in image_files:
        print(f"处理: {img_file.name}")
        
        # 备份原文件
        if backup:
            backup_path = backup_dir / img_file.name
            import shutil
            if not backup_path.exists():
                shutil.copy2(img_file, backup_path)
        
        # 处理图片
        if remove_background(img_file):
            processed_count += 1
        print()
    
    print(f"完成！共处理了 {processed_count} 个文件")
    if backup:
        print(f"原文件已备份到: {backup_dir}")

def main():
    import sys
    
    # 设置输出编码
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except:
            pass
    
    # 目标目录
    target_dir = Path(r"E:\Maa_HLR\assets\resource\image\scratch_sprits")
    
    if not target_dir.exists():
        print(f"错误: 目录不存在 {target_dir}")
        return
    
    print("开始处理背景去除...")
    print(f"目标目录: {target_dir}\n")
    
    # 处理目录
    process_directory(target_dir, backup=True)

if __name__ == "__main__":
    main()
