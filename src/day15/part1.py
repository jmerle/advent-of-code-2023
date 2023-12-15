import sys

def main() -> None:
    data = sys.stdin.read().strip()

    t = 0
    for step in data.split(","):
        v = 0
        for ch in step:
            v += ord(ch)
            v *= 17
            v %= 256

        t += v

    print(t)

if __name__ == "__main__":
    main()
