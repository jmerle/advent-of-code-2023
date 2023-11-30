import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path
from watchfiles import Change, watch

def main() -> None:
    parser = ArgumentParser(description="Automatically run part1.py and part2.py on save.")
    parser.add_argument("data_file_name", type=str, help="the name of the data file to run on")

    args = parser.parse_args()

    print(f"Started runner for {args.data_file_name}")

    project_root = Path(__file__).parent.parent

    process = None
    process_code_file = None
    process_data_file_fd = None

    try:
        for changes in watch(project_root):
            for change, changed_file in changes:
                if change != Change.modified:
                    continue

                changed_file = Path(changed_file)
                if not changed_file.is_file():
                    continue

                if changed_file.name in ["part1.py", "part2.py"]:
                    code_file = changed_file
                elif changed_file.name == args.data_file_name and process_code_file is not None:
                    code_file = process_code_file
                else:
                    continue

                print(f"Running {code_file.relative_to(project_root)} on {args.data_file_name}")

                if process is not None and process.poll() is None:
                    print("Killing previous process")
                    process.kill()
                    process_data_file_fd.close()

                module_name = str(code_file.relative_to(project_root)).replace("/", ".").replace(".py", "")
                data_file = code_file.parent / args.data_file_name
                data_file_fd = data_file.open("r")

                print()

                if len(data_file.read_text(encoding="utf-8")) == 0:
                    print(f"{args.data_file_name} is empty!")

                process = subprocess.Popen([sys.executable, "-m", module_name], cwd=project_root, stdin=data_file_fd)
                process_code_file = code_file
                process_data_file_fd = data_file_fd
    except KeyboardInterrupt:
        if process is not None and process.poll() is None:
            print("Killing current process")
            process.kill()
            process_data_file_fd.close()

        sys.exit(1)

if __name__ == "__main__":
    main()
