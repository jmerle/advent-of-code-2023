import re
import sys
from math import *

def main() -> None:
    data = sys.stdin.read().strip()

    instrs = data.split("\n")[0]
    nodes = {}

    for node in data.split("\n\n")[1].split("\n"):
        src, left, right = re.findall(r"([A-Z]{3})", node)
        nodes[src] = (left, right)

    current = "AAA"
    idx = 0

    t = 0
    while current != "ZZZ":
        move = instrs[idx]
        idx = (idx + 1) % len(instrs)
        current = nodes[current][0 if move == "L" else 1]
        t += 1

    print(t)

if __name__ == "__main__":
    main()
