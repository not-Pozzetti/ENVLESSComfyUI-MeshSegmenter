"""ENVLESSComfyUI-MeshSegmenter Prestartup Script."""

import logging
import shutil
from pathlib import Path
from comfy_3d_viewers import copy_viewer

log = logging.getLogger("meshsegmenter")

def setup():
    SCRIPT_DIR = Path(__file__).resolve().parent
    COMFYUI_DIR = SCRIPT_DIR.parent.parent
    
    # Copy text report viewer (JS widget + utils)
    try:
        copy_viewer("text_report", SCRIPT_DIR / "web")
    except Exception as e:
        log.warning(f"Failed to copy text_report viewer: {e}")

    # Copy dynamic widgets JS
    try:
        from comfy_dynamic_widgets import get_js_path
        src = Path(get_js_path())
        if src.exists():
            dst = SCRIPT_DIR / "web" / "js" / "dynamic_widgets.js"
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime:
                shutil.copy2(src, dst)
    except ImportError:
        pass

    # Copy example 3D assets
    src_assets = SCRIPT_DIR / "assets"
    dst_assets = COMFYUI_DIR / "input" / "3d"
    if src_assets.exists():
        dst_assets.mkdir(parents=True, exist_ok=True)
        # Replicating copy_files(..., "**/*")
        for item in src_assets.rglob("*"):
            if item.is_file():
                relative_path = item.relative_to(src_assets)
                target = dst_assets / relative_path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target)
        log.info(f"Copied assets from {src_assets} to {dst_assets}")

if __name__ == "__main__":
    setup()
