"""
Core orchestrator - coordinates all operations
"""
import shutil
from datetime import datetime
import sys
from pathlib import Path
from .cli import parse_args
from .console import ConsoleUI
from .cleaner import ProjectCleaner
from .inspector import ProjectInspector
from .packager import ProjectPackager

class PyShrinkCore:
    """Main application orchestrator"""
    
    def __init__(self):
        self.ui = ConsoleUI()
        self.args = parse_args()

        # Normalize path (handles paths with spaces)
        if isinstance(self.args.path, list):
            self.args.path = " ".join(self.args.path)
    
    def run(self):
        """Run the application"""
        # Print banner
        self.ui.print_banner()
        
        # Get project path
        if self.args.path:
            project_path = Path(self.args.path).resolve()
        else:
            # Interactive mode - ask for path
            path_input = self.ui.ask_input("Enter project path")
            project_path = Path(path_input).resolve()
        
        # Validate path
        if not project_path.exists():
            self.ui.print_error(f"Path does not exist: {project_path}")
            sys.exit(1)
        
        if not project_path.is_dir():
            self.ui.print_error(f"Path is not a directory: {project_path}")
            sys.exit(1)
        
        self.ui.print_info(f"📂 Project: {project_path}")
        print()

        # Create clone directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        clone_path = project_path.parent / f"{project_path.name}_pyshrink_{timestamp}"

        self.ui.print_info(f"📄 Creating working copy: {clone_path}")

        try:
            shutil.copytree(
                project_path,
                clone_path,
                ignore=shutil.ignore_patterns(
                    ".git",
                    ".venv",
                    "venv",
                    "__pycache__",
                    ".pytest_cache"
                )
            )
        except Exception as e:
            self.ui.print_error(f"Failed to clone project: {e}")
            sys.exit(1)

        print()

        # 🔁 IMPORTANT: use clone_path from here onward
        inspector = ProjectInspector(clone_path, self.ui)
        cleaner = ProjectCleaner(clone_path, self.ui)
        packager = ProjectPackager(clone_path, self.ui)

        
        # if args.full:
        #     generate_readme = False
        #     generate_requirements = False
        # else:
        #     generate_readme = args.readme
        #     generate_requirements = args.req

        # --- FULL CLEANUP MODE ---
        if self.args.full:
            self.ui.print_info("Running full cleanup (no README, no requirements)")
            # self.ui.print_info("🧹 Cleaning junk files...")
            cleaner.clean()
            # return

        
        # Check/create requirements.txt
        if self.args.req or not inspector.check_requirements():
            if self.args.req or self.ui.ask_yes_no("Create/validate requirements.txt?"):
                inspector.create_requirements()
        
        # Check/create README.md
        if self.args.readme or not inspector.check_readme():
            if self.args.readme or self.ui.ask_yes_no("Create README.md if missing?"):
                inspector.create_readme()
        
        print()
        
        # Clean junk files
        self.ui.print_info("🧹 Cleaning junk files...")
        cleaner.clean()
        
        print()
        
        # Create zip file
        self.ui.print_info("📦 Creating zip file...")
        zip_path = packager.create_zip()
        
        print()
        
        if zip_path:
            self.ui.print_success("🎉 All done!")
            self.ui.print_info(f"Zip file: {zip_path}")
        else:
            self.ui.print_error("Failed to create zip file")
            sys.exit(1)
