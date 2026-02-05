from pathlib import Path
import shutil
from .cli import parse_args
from .console import banner, ask_path, ask_confirm
from .logger import log_structure, console
from .inspector import handle_requirements, handle_readme
from .cleaner import scan_cleanup, apply_cleanup
from .packager import zip_project

def run():
    banner()
    args = parse_args()

    project_path = Path(args.path or ask_path()).resolve()
    safe_copy_path = project_path.parent / f"{project_path.name}_PYSHARE"

    # Step 1: Copy project to a new folder
    if safe_copy_path.exists():
        console.print(f"[yellow]Folder {safe_copy_path} already exists, removing it first...[/]")
        shutil.rmtree(safe_copy_path)

    console.print(f"[green]Creating a safe copy at {safe_copy_path}[/]")
    shutil.copytree(project_path, safe_copy_path)

    # Step 2: Show before structure
    log_structure("Project Structure Before Cleanup", safe_copy_path)

    # Step 3: Handle requirements & README
    handle_requirements(safe_copy_path, args.req)
    handle_readme(safe_copy_path, args.readme)

    # Step 4: Scan files/folders to delete
    targets = scan_cleanup(safe_copy_path)

    if not targets:
        console.print("[green]No unnecessary files found 🎉[/]")
    else:
        console.rule("[bold red]Files & folders that WILL be deleted")
        for item in targets:
            console.print(f"[red]- {item.relative_to(safe_copy_path)}[/]")

        if not ask_confirm("Proceed with cleanup?"):
            console.print("[yellow]Cleanup aborted by user[/]")
            return

        apply_cleanup(targets)

    # Step 5: Show after cleanup
    log_structure("Project Structure After Cleanup", safe_copy_path)

    # Step 6: Zip the safe copy
    zip_project(safe_copy_path)
