import sys
from collections import *

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for line in data.split("\n"):
        parts = line.split(": ")[1].split("; ")

        possible = True
        for part in parts:
            d = Counter()
            for p in part.split(", "):
                amount, color = p.split(" ")
                d[color] += int(amount)

            for k, v in d.items():
                if k not in ["red", "green", "blue"]:
                    possible = False
                    break

                if (k == "red" and v > 12) or (k == "green" and v > 13) or (k == "blue" and v > 14):
                    possible = False
                    break

        if possible:
            t += int(line.split(": ")[0].split(" ")[1])

    print(t)

if __name__ == "__main__":
    main()
