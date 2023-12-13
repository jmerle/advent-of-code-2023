import sys

def horizontal_mirror(pattern: list[str]) -> int:
    width = len(pattern[0])
    height = len(pattern)

    for y in range(height - 1, 0, -1):
        error = 0
        for x in range(width):
            col = "".join([row[x] for row in pattern])

            for i in range(y):
                if y + i >= len(col):
                    break

                if col[y + i] != col[y - i - 1]:
                    error += 1

        if error == 1:
            return y

    return 0

def vertical_mirror(pattern: list[str]) -> int:
    width = len(pattern[0])
    height = len(pattern)

    for x in range(width - 1, 0, -1):
        error = 0
        for row in pattern:
            for i in range(x):
                if x + i >= len(row):
                    break

                if row[x + i] != row[x - i - 1]:
                    error += 1

        if error == 1:
            return x

    return 0

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for pattern in data.split("\n\n"):
        pattern = pattern.split("\n")
        t += vertical_mirror(pattern) + horizontal_mirror(pattern) * 100

    print(t)

if __name__ == "__main__":
    main()
