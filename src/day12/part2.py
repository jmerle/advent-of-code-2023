import sys
from functools import *
from multiprocessing import *

@cache
def count_options(pattern: str, groups: tuple[int]) -> int:
    if len(pattern) == 0:
        return int(len(groups) == 0)

    if len(groups) == 0:
        return int("#" not in pattern)

    if pattern[0] == "?":
        return count_options_hashtag(pattern, groups) + count_options(pattern[1:], groups)
    elif pattern[0] == "#":
        return count_options_hashtag(pattern, groups)
    else:
        return count_options(pattern[1:], groups)

@cache
def count_options_hashtag(pattern: str, groups: tuple[int]) -> int:
    g = groups[0]
    if len(pattern) < g or "." in pattern[:g] or (len(pattern) > g and pattern[g] == "#"):
        return 0

    return count_options(pattern[g + 1:], groups[1:])

def process(line: str) -> int:
    pattern, groups = line.split(" ")
    groups = tuple(map(int, groups.split(",")))

    pattern = "?".join([pattern] * 5)
    groups = groups * 5

    return count_options(pattern, groups)

def main() -> None:
    data = sys.stdin.read().strip()

    with Pool(15) as pool:
        print(sum(pool.map(process, data.split("\n"))))

if __name__ == "__main__":
    main()
