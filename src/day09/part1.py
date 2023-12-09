import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for line in data.split("\n"):
        nums = list(map(int, line.split(" ")))

        rows = [nums]
        while rows[-1].count(0) != len(rows[-1]):
            new_row = []

            for i in range(len(rows[-1]) - 1):
                new_row.append(rows[-1][i + 1] - rows[-1][i])

            rows.append(new_row)

        rows[-1].append(0)
        for i in range(len(rows) - 2, -1, -1):
            rows[i].append(rows[i][-1] + rows[i + 1][-1])

        t += rows[0][-1]

    print(t)

if __name__ == "__main__":
    main()
