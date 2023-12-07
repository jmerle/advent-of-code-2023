import sys
from collections import *

def get_score(item: tuple[str, int]) -> tuple[int, list[int]]:
    hand, bid = item

    counts = list(Counter(hand).values())
    if 5 in counts:
        type = 10
    elif 4 in counts:
        type = 9
    elif 3 in counts:
        type = 8 if 2 in counts else 7
    elif 2 in counts:
        type = 6 if counts.count(2) == 2 else 5
    else:
        type = 4

    values = list(map("23456789TJQKA".index, hand))

    return (type, values)

def main() -> None:
    data = sys.stdin.read().strip()

    hands = []
    for line in data.split("\n"):
        hand, bid = line.split(" ")
        hands.append((hand, int(bid)))

    hands = sorted(hands, key=get_score)

    t = 0
    for i, (hand, bid) in enumerate(hands):
        t += bid * (i + 1)

    print(t)

if __name__ == "__main__":
    main()
