import re
import sys
from math import *

def main() -> None:
    data = sys.stdin.read().strip()

    instrs = data.split("\n")[0]
    nodes = {}

    current = []

    for node in data.split("\n\n")[1].split("\n"):
        src, left, right = re.findall(r"([A-Z0-9]{3})", node)
        nodes[src] = (left, right)

        if src.endswith("A"):
            current.append(src)

    lens = []
    for v in current:
        node = v
        idx = 0

        t = 0
        while node[2] != "Z":
            move = instrs[idx]
            idx = (idx + 1) % len(instrs)
            node = nodes[node][0 if move == "L" else 1]
            t += 1

        lens.append(t)

    print(lcm(*lens))

if __name__ == "__main__":
    main()
