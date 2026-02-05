import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Clean & package Python projects"
    )

    parser.add_argument("--path", help="Project root directory")
    parser.add_argument("--req", action="store_true")
    parser.add_argument("--readme", action="store_true")

    return parser.parse_args()
