"""
Project inspection - check for requirements.txt and README.md
"""

import os
from pathlib import Path
from .console import ConsoleUI

class ProjectInspector:
    """Inspects project for requirements.txt and README.md"""
    
    def __init__(self, project_path, ui: ConsoleUI):
        self.project_path = Path(project_path)
        self.ui = ui
    
    def check_requirements(self):
        """Check if requirements.txt exists"""
        req_file = self.project_path / "requirements.txt"
        return req_file.exists()
    
    def check_readme(self):
        """Check if README.md exists"""
        readme_file = self.project_path / "README.md"
        return readme_file.exists()
    
    def create_requirements(self):
        """Create basic requirements.txt"""
        req_file = self.project_path / "requirements.txt"
        
        if req_file.exists():
            self.ui.print_info("requirements.txt already exists")
            return
        
        # Try to detect imports (basic implementation)
        imports = self._detect_imports()
        
        if imports:
            with open(req_file, 'w') as f:
                for imp in sorted(imports):
                    f.write(f"{imp}\n")
            self.ui.print_success(f"Created requirements.txt with {len(imports)} packages")
        else:
            # Create empty requirements.txt
            with open(req_file, 'w') as f:
                f.write("# Add your dependencies here\n")
            self.ui.print_success("Created empty requirements.txt")
    
    def create_readme(self):
        """Create basic README.md"""
        readme_file = self.project_path / "README.md"
        
        if readme_file.exists():
            self.ui.print_info("README.md already exists")
            return
        
        project_name = self.project_path.name
        
        content = f"""# {project_name}

                    ## Description

                    Add your project description here.

                    ## Installation

                    ```bash
                    pip install -r requirements.txt
                    ```

                    ## Usage

                    Add usage instructions here.

                    ## License

                    Add license information here.
                    """
        
        with open(readme_file, 'w') as f:
            f.write(content)
        
        self.ui.print_success("Created README.md")
    
    def _detect_imports(self):
        """Detect Python imports in the project (basic implementation)"""
        imports = set()
        
        for root, dirs, files in os.walk(self.project_path):
            # Skip common directories
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.venv', 'venv', 'node_modules']]
            
            for file in files:
                if file.endswith('.py'):
                    file_path = Path(root) / file
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            for line in f:
                                line = line.strip()
                                if line.startswith('import ') or line.startswith('from '):
                                    parts = line.split()
                                    if len(parts) >= 2:
                                        module = parts[1].split('.')[0]
                                        # Skip standard library modules
                                        if module not in ['os', 'sys', 'json', 'time', 'datetime', 
                                                         're', 'math', 'random', 'collections',
                                                         'itertools', 'functools', 'pathlib']:
                                            imports.add(module)
                    except:
                        pass
        
        return imports
