import ast
import sys
from pathlib import Path
from .logger import logger
from .console import ask_confirm

def discover_dependencies(project_path: Path):
    imports = set()

    for py_file in project_path.rglob("*.py"):
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    imports.add(n.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])

    stdlib = set(sys.builtin_module_names)
    return sorted(i for i in imports if i not in stdlib)

def handle_requirements(project_path: Path, auto: bool):
    req = project_path / "requirements.txt"

    if req.exists():
        logger.info("requirements.txt found ✔")
        return

    logger.warning("requirements.txt missing")

    if not auto and not ask_confirm("Create requirements.txt automatically?"):
        return

    deps = discover_dependencies(project_path)
    if deps:
        req.write_text("\n".join(deps))
        logger.info("requirements.txt created")

def handle_readme(project_path: Path, auto: bool):
    readme = project_path / "README.md"

    if readme.exists():
        logger.info("README.md found ✔")
        return

    logger.warning("README.md missing")

    if not auto and not ask_confirm("Create README.md?"):
        return

    readme.write_text(
        f"# {project_path.name}\n\nPackaged using **pyshare** 🚀"
    )
    logger.info("README.md created")
