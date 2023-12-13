import sys

def horizontal_mirror(pattern: list[str]) -> int:
    width = len(pattern[0])
    height = len(pattern)

    for y in range(height - 1, 0, -1):
        possible = True
        for x in range(width):
            col = "".join([row[x] for row in pattern])
            a = col[:y]
            b = col[y:]
            if len(a) < len(b):
                if not b.startswith(a[::-1]):
                    possible = False
                    break
            else:
                if not a.endswith(b[::-1]):
                    possible = False
                    break

        if possible:
            return y

    return 0

def vertical_mirror(pattern: list[str]) -> int:
    width = len(pattern[0])
    height = len(pattern)

    for x in range(width - 1, 0, -1):
        possible = True
        for row in pattern:
            a = row[:x]
            b = row[x:]
            if len(a) < len(b):
                if not b.startswith(a[::-1]):
                    possible = False
                    break
            else:
                if not a.endswith(b[::-1]):
                    possible = False
                    break

        if possible:
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
