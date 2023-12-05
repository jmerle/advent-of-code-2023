import sys
from dataclasses import *
from multiprocessing import *

@dataclass
class Range:
    start: int
    length: int

    def contains(self, value: int) -> bool:
        return self.start <= value < self.start + self.length

def check(loc: int) -> int | None:
    global seed_ranges
    global maps

    value = loc

    for m in maps:
        for trg_range, src_start in m:
            if trg_range.contains(value):
                value = src_start + (value - trg_range.start)
                break

    return loc if any(r.contains(value) for r in seed_ranges) else None

def main() -> None:
    global seed_ranges
    global maps

    data = sys.stdin.read().strip()

    raw_seeds = list(map(int, data.split("\n")[0].split(": ")[1].split(" ")))
    seed_ranges = []
    for i in range(0, len(raw_seeds), 2):
        seed_ranges.append(Range(raw_seeds[i], raw_seeds[i + 1]))

    maps = []

    for sec in data.split("\n\n")[1:]:
        lines = sec.split("\n")

        m = []
        for line in lines[1:]:
            trg_start, src_start, length = map(int, line.split(" "))
            m.append((Range(trg_start, length), src_start))

        maps.append(m)

    maps = maps[::-1]

    with Pool(15) as pool:
        for loc in pool.imap(check, range(int(1e9)), int(1e6)):
            if loc is not None:
                print(loc)
                return

if __name__ == "__main__":
    main()
