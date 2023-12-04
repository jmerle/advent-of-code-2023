import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    copies = {i: 1 for i in range(data.count("\n") + 1)}

    for i, card in enumerate(data.split("\n")):
        parts = [v for v in card.split(" ") if v != ""]
        sep = parts.index("|")

        wins = list(map(int, parts[2:sep]))
        have = list(map(int, parts[sep + 1:]))

        score = 0
        for v in have:
            if v in wins:
                score += 1

        for j in range(i + 1, i + score + 1):
            copies[j] += copies[i]

        t += copies[i]

    print(t)

if __name__ == "__main__":
    main()
