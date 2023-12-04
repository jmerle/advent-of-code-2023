import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for card in data.split("\n"):
        parts = [v for v in card.split(" ") if v != ""]
        sep = parts.index("|")

        wins = list(map(int, parts[2:sep]))
        have = list(map(int, parts[sep + 1:]))

        score = 0
        for v in have:
            if v in wins:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        t += score

    print(t)

if __name__ == "__main__":
    main()
