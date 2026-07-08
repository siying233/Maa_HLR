from pathlib import Path

import shutil

from pathlib import Path

def get_project_root() -> Path:
    """动态向上查找包含 .git 或 README.md 的项目根目录"""
    current = Path(__file__).resolve()
    # 循环向上查找，最多找 5 层防止死循环
    for _ in range(5):
        # 如果当前目录下有 .git 或 README.md，说明这就是根目录
        if (current / ".git").exists() or (current / "README.md").exists():
            return current
        current = current.parent
    # 如果没找到，兜底返回当前脚本的 parent
    return Path(__file__).resolve().parent
ROOT_DIR = get_project_root()
assets_dir = ROOT_DIR / "assets"
# assets_dir = Path(__file__).parent.parent.resolve() / "assets"

def configure_ocr_model():
    # assets_ocr_dir = assets_dir / "MaaCommonAssets" / "OCR"
    # if not assets_ocr_dir.exists():
    #     print(f"File Not Found: {assets_ocr_dir}")
    #     exit(1)

    ocr_dir = assets_dir / "resource" / "model" / "ocr"
    if not ocr_dir.exists():   # copy default OCR model only if dir does not exist
        shutil.copytree( 
            assets_dir / "MaaCommonAssets" / "OCR" / "ppocr_v6" / "small",
            # assets_dir / "MaaCommonAssets" / "OCR" / "ppocr_v5" / "zh_cn",
            ocr_dir,
            dirs_exist_ok=True,
        )
    else:
        print("Found existing OCR directory, skipping default OCR model import.")


if __name__ == "__main__":
    configure_ocr_model() 

    print("OCR model configured.")
