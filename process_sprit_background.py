# 创建绿色背景
import cv2
import numpy as np
import os
from pathlib import Path

# 输入与输出目录（相对当前脚本运行位置）
INPUT_DIR = Path(r".\assets\resource\image\scratch_sprits\backup_original")

OUTPUT_DIR = Path(r".\assets\resource\image\scratch_sprits")

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith('.png'):
        continue

    input_path = os.path.join(INPUT_DIR, filename)
    src = cv2.imread(input_path)
    if src is None:
        continue

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 0, 0), (94, 255, 255))  # 目标区域为白色

    green_bg = np.full(src.shape, (0, 255, 0), dtype=np.uint8)  # 绿色背景

    # 使用掩膜合成：白色区域用原图，黑色区域用绿色
    result = np.where(mask[:, :, None] == 255, src, green_bg)

    # 例如：backup_original/decide.png -> assets/resource/image/decide.png
    output_path = os.path.join(OUTPUT_DIR, filename)
    cv2.imwrite(output_path, result)

# print("完成！backup_original 目录下所有 PNG 已处理并输出到 assets/resource/image")