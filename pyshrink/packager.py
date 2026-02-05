from pathlib import Path
import zipfile
from .logger import logger

def zip_project(project_path: Path):
    zip_path = project_path.parent / f"{project_path.name}.zip"
    logger.info(f"Creating zip → {zip_path}")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in project_path.rglob("*"):
            zipf.write(file, arcname=file.relative_to(project_path))
