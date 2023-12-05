import sys
from collections import *

def main() -> None:
    data = sys.stdin.read().strip()

    seeds = list(map(int, data.split("\n")[0].split(": ")[1].split(" ")))

    d = defaultdict(dict)
    trgs = []

    for sec in data.split("\n\n")[1:]:
        lines = sec.split("\n")

        parts = lines[0].split("-")
        src = parts[0]
        trg = parts[2].split(" ")[0]

        d[src][trg] = []
        trgs.append(trg)

        for line in lines[1:]:
            trg_start, src_start, length = map(int, line.split(" "))
            d[src][trg].append((trg_start, src_start, length))

    min_loc = 1e9
    for seed in seeds:
        current = "seed"
        value = seed

        for trg in trgs:
            for trg_start, src_start, length in d[current][trg]:
                if src_start <= value < src_start + length:
                    value = trg_start + (value - src_start)
                    break

            current = trg

        min_loc = min(min_loc, value)

    print(min_loc)

if __name__ == "__main__":
    main()
