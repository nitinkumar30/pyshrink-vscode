"""
Package project into a zip file
"""

import zipfile
from pathlib import Path
from .config import JUNK_FOLDERS, JUNK_FILES
from .console import ConsoleUI

class ProjectPackager:
    """Handles packaging project into a zip file"""
    
    def __init__(self, project_path, ui: ConsoleUI):
        self.project_path = Path(project_path)
        self.ui = ui
    
    def create_zip(self):
        """Create zip file of the project"""
        # Zip file path (outside the project directory)
        parent_dir = self.project_path.parent
        project_name = self.project_path.name
        zip_path = parent_dir / f"{project_name}.zip"
        
        self.ui.print_info(f"Creating zip file: {zip_path}")
        
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                file_count = 0
                
                for root in self.project_path.rglob('*'):
                    # Skip junk directories
                    if any(junk in root.parts for junk in JUNK_FOLDERS):
                        continue
                    
                    # Add files
                    if root.is_file():
                        # Skip junk files
                        if not any(root.match(pattern) for pattern in JUNK_FILES):
                            arcname = root.relative_to(self.project_path.parent)
                            zipf.write(root, arcname)
                            file_count += 1
            
            zip_size = zip_path.stat().st_size / (1024 * 1024)
            self.ui.print_success(f"✅ Created {zip_path.name} ({zip_size:.2f} MB, {file_count} files)")
            
            return str(zip_path)
            
        except Exception as e:
            self.ui.print_error(f"Failed to create zip: {e}")
            return None
