import logging
from pathlib import Path
from rich.logging import RichHandler
from rich.tree import Tree
from rich.console import Console

console = Console()

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[RichHandler(console=console)]
)

logger = logging.getLogger("pyshare")

def build_tree(path: Path) -> Tree:
    tree = Tree(f"[bold cyan]{path.name}[/]")
    for item in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name)):
        if item.is_dir():
            tree.add(f"[blue]{item.name}/[/]")
        else:
            tree.add(item.name)
    return tree

def log_structure(title: str, path: Path):
    console.rule(f"[bold yellow]{title}")
    console.print(build_tree(path))
