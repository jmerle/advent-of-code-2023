from argparse import ArgumentParser
from common import get_requests_session
from pathlib import Path

def main() -> None:
    parser = ArgumentParser(description="Download input data for a day.")
    parser.add_argument("day", type=int, help="the day to download input data for")

    args = parser.parse_args()

    project_root = Path(__file__).parent.parent

    input_file = project_root / "src" / f"day{args.day:02}" / "input.txt"
    if not input_file.is_file():
        raise RuntimeError(f"{input_file} does not exist")

    input_response = get_requests_session().get(f"https://adventofcode.com/2023/day/{args.day}/input")
    input_response.raise_for_status()

    input_file.write_text(input_response.text, encoding="utf-8")
    print(f"Successfully wrote input data to {input_file.relative_to(project_root)}")

if __name__ == "__main__":
    main()
