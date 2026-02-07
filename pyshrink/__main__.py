#!/usr/bin/env python3
"""
PyShrink - Python Project Cleaner & Packager
Entry point for the CLI tool
"""

import sys
from .core import PyShrinkCore

def main():
    """Main entry point"""
    if sys.platform.startswith("win"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass
    try:
        app = PyShrinkCore()
        app.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("PyShrink __main__ reached")
    main()
