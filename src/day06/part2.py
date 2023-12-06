import re
import sys

def main() -> None:
    data = sys.stdin.read().strip()

    lines = data.split("\n")
    times = [int("".join(re.findall(r"(\d+)", lines[0])))]
    distances = [int("".join(re.findall(r"(\d+)", lines[1])))]

    out = 1

    for t, d in zip(times, distances):
        count = 0
        for speed in range(1, t):
            total = (t - speed) * speed

            if total > d:
                count += 1

        out *= count

    print(out)

if __name__ == "__main__":
    main()
