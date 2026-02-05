from pathlib import Path
import shutil
from typing import List
from .config import (
    UNNECESSARY_DIRS,
    UNNECESSARY_PREFIXES,
    UNNECESSARY_EXTENSIONS,
)
from .logger import logger

def scan_cleanup(project_path: Path) -> List[Path]:
    """
    Scan project and return a list of files/folders
    that will be deleted.
    """
    targets = []

    for item in project_path.rglob("*"):
        if item.is_dir():
            if (
                item.name in UNNECESSARY_DIRS
                or item.name.startswith(UNNECESSARY_PREFIXES)
            ):
                targets.append(item)

        elif item.is_file() and item.suffix in UNNECESSARY_EXTENSIONS:
            targets.append(item)

    return targets

def apply_cleanup(targets: List[Path]):
    """
    Actually delete scanned files/folders.
    """
    logger.info("Applying cleanup")

    for item in targets:
        if not item.exists():
            continue

        if item.is_dir():
            logger.info(f"Removing directory → {item}")
            shutil.rmtree(item, ignore_errors=True)
        else:
            logger.info(f"Removing file → {item}")
            item.unlink(missing_ok=True)
