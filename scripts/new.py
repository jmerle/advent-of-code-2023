from argparse import ArgumentParser
from pathlib import Path

PYTHON_TEMPLATE = """
import sys

def main() -> None:
    data = sys.stdin.read().strip()

if __name__ == "__main__":
    main()
""".strip() + "\n"

def main() -> None:
    parser = ArgumentParser(description="Create skeleton files for a day.")
    parser.add_argument("day", type=int, help="the day to create files for")

    args = parser.parse_args()

    project_root = Path(__file__).parent.parent

    day_directory = project_root / "src" / f"day{args.day:02}"
    if day_directory.is_dir():
        raise RuntimeError(f"{day_directory} already exists")

    for file, content in [
        (day_directory / "example.txt", ""),
        (day_directory / "input.txt", ""),
        (day_directory / "part1.py", PYTHON_TEMPLATE),
        (day_directory / "part2.py", PYTHON_TEMPLATE)
    ]:
        file.parent.mkdir(parents=True, exist_ok=True)
        with file.open("w+", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully created {file.relative_to(project_root)}")

if __name__ == "__main__":
    main()
