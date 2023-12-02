import sys
from collections import *

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for line in data.split("\n"):
        parts = line.split(": ")[1].split("; ")

        required = Counter()

        for part in parts:
            d = Counter()
            for p in part.split(", "):
                amount, color = p.split(" ")
                d[color] += int(amount)

            for k, v in d.items():
                required[k] = max(required[k], v)

        t += required["red"] * required["green"] * required["blue"]

    print(t)

if __name__ == "__main__":
    main()
