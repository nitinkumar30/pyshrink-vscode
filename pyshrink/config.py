"""
Configuration constants for PyShrink
"""

# Files and folders to remove
JUNK_FOLDERS = [
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
    "node_modules",
    ".DS_Store",
    "*.egg-info",
    ".git",

    # --- Optional / aggressive cleanup (commented by default) ---
    # "dist",
    # "build",
    # ".mypy_cache",
    # ".ruff_cache",
    # ".coverage",
    # "htmlcov",
    # ".tox",
    # ".nox",
    # ".eggs",
    ".cache",
]

JUNK_FILES = [
    "*.pyc",
    "*.pyo",
    "*.pyd",
    ".DS_Store",
    "Thumbs.db",

    # --- Optional / aggressive cleanup ---
    "*.log",
    "*.tmp",
    # "*.bak",
    # "*.swp",
    # ".coverage",
]

# Files to always keep
KEEP_FILES = [
    ".gitignore",
    ".env.example",
    "LICENSE",
    "README.md",
    "requirements.txt",
]
