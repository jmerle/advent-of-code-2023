import itertools
import sys
from multiprocessing import *

def matches_pattern(arrangement: str, pattern: str) -> bool:
    for i, ch in enumerate(pattern):
        if ch != "?" and arrangement[i] != ch:
            return False

    return True

def is_valid(arrangement: str, groups: list[int]) -> bool:
    idx = 0

    current_length = 0

    for ch in arrangement:
        if ch == "#":
            current_length += 1
        elif current_length > 0:
            if idx >= len(groups) or current_length != groups[idx]:
                return False

            idx += 1
            current_length = 0

    if current_length > 0:
        if idx >= len(groups) or current_length != groups[idx]:
            return False

        idx += 1
        current_length = 0

    return current_length == 0 and idx == len(groups)

def process(line: str) -> int:
    pattern, groups = line.split(" ")
    groups = list(map(int, groups.split(",")))

    t = 0
    for arrangement in itertools.product("#.", repeat=len(pattern)):
        if matches_pattern(arrangement, pattern) and is_valid(arrangement, groups):
            t += 1

    return t

def main() -> None:
    data = sys.stdin.read().strip()

    with Pool(15) as pool:
        print(sum(pool.map(process, data.split("\n"))))

if __name__ == "__main__":
    main()
