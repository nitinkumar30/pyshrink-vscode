"""
File cleaning logic
"""

import os
import shutil
from pathlib import Path
from .config import JUNK_FOLDERS, JUNK_FILES
from .console import ConsoleUI

class ProjectCleaner:
    """Handles cleaning of junk files and folders"""
    
    def __init__(self, project_path, ui: ConsoleUI):
        self.project_path = Path(project_path)
        self.ui = ui
        self.removed_items = []
        self.removed_size = 0
    
    def scan_junk(self):
        """Scan for junk files and folders"""
        junk_items = []
        
        for root, dirs, files in os.walk(self.project_path):
            root_path = Path(root)
            
            # Check folders
            for folder in dirs:
                if folder in JUNK_FOLDERS or folder.startswith('.venv'):
                    folder_path = root_path / folder
                    size = self._get_folder_size(folder_path)
                    junk_items.append({
                        'path': folder_path,
                        'type': 'folder',
                        'size': size
                    })
            
            # Check files
            for file in files:
                if any(Path(file).match(pattern) for pattern in JUNK_FILES):
                    file_path = root_path / file
                    size = file_path.stat().st_size if file_path.exists() else 0
                    junk_items.append({
                        'path': file_path,
                        'type': 'file',
                        'size': size
                    })
        
        return junk_items
    
    def clean(self):
        """Clean junk files and folders"""
        junk_items = self.scan_junk()
        
        if not junk_items:
            self.ui.print_info("No junk files found. Project is already clean!")
            return
        
        self.ui.print_info(f"Found {len(junk_items)} items to remove")
        
        for item in junk_items:
            try:
                if item['type'] == 'folder':
                    # shutil.rmtree(item['path'])
                    shutil.rmtree(item['path'], ignore_errors=True)
                    self.ui.print_success(f"Removed folder: {item['path'].name}")
                else:
                    # item['path'].unlink()
                    if item['path'].exists():
                        item['path'].unlink()
                        self.ui.print_success(f"Removed file: {item['path'].name}")
                
                self.removed_items.append(item)
                self.removed_size += item['size']
            except Exception as e:
                self.ui.print_error(f"Failed to remove {item['path']}: {e}")
        
        # Print summary
        size_mb = self.removed_size / (1024 * 1024)
        self.ui.print_success(f"\n🎉 Cleaned {len(self.removed_items)} items ({size_mb:.2f} MB freed)")
    
    def _get_folder_size(self, folder_path):
        """Calculate total size of a folder"""
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    filepath = Path(dirpath) / filename
                    if filepath.exists():
                        total_size += filepath.stat().st_size
        except:
            pass
        return total_size
