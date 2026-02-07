"""
CLI argument parser for PyShrink
"""

import argparse
import sys

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="PyShrink - Clean and package Python projects",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --path /path/to/project
  python main.py --path /path/to/project --req --readme
        """
    )
    
    parser.add_argument(
        "--path",
        # type=str,
        nargs="+",
        help="Path to the Python project to clean"
    )
    
    parser.add_argument(
        "--req",
        action="store_true",
        help="Automatically create/validate requirements.txt"
    )
    
    parser.add_argument(
        "--readme",
        action="store_true",
        help="Automatically create README.md if missing"
    )

    parser.add_argument(
        "--full",
        action="store_true",
        help="Full cleanup (no README, no requirements)"
    )
    args = parser.parse_args()

    if args.path:
        args.path = " ".join(args.path)

    return parser.parse_args()
