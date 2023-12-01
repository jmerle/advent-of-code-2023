import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for line in data.split("\n"):
        nums = ""

        for ch in line:
            if ch.isdigit():
                nums += ch
                break

        for ch in reversed(line):
            if ch.isdigit():
                nums += ch
                break

        t += int(nums)

    print(t)

if __name__ == "__main__":
    main()
