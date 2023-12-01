import sys

def main() -> None:
    data = sys.stdin.read().strip()

    a = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    for i in range(1, 10):
        a[str(i)] = i

    t = 0
    for line in data.split("\n"):
        first = None
        first_index = len(line) + 1

        last = None
        last_index = -1

        for k, v in a.items():
            if k not in line:
                continue

            x = line.index(k)
            y = line.rindex(k)

            if x < first_index:
                first = v
                first_index = x

            if y > last_index:
                last = v
                last_index = y

        if first is not None and last is not None:
            t += int(str(first) + str(last))

    print(t)

if __name__ == "__main__":
    main()
