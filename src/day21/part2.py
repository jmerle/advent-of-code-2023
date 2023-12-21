import sys
from collections import *

def main() -> None:
    data = sys.stdin.read().strip()

    grid = data.split("\n")

    width = len(grid[0])
    height = len(grid)

    seen = set()
    garden = defaultdict(set)
    queue = []

    for y in range(height):
        for x in range(width):
            if grid[y][x] == "S":
                queue.append((x, y, 0))

    while len(queue) > 0:
        x, y, step = queue.pop()

        if (x, y, step) in seen:
            continue

        seen.add((x, y, step))

        if grid[y % height][x % width] in ".S":
            if (step - 65) % 131 == 0:
                garden[step].add((x, y))
        else:
            continue

        if step == 327:
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            queue.append((x + dx, y + dy, step + 1))

    # This one took quite a while to find, the general idea is:
    # After a while, every <width> steps the difference between the answer
    # at steps <n> and <n - width> increases by a constant amount

    # for i in range(65, 459 - width, width):
    #     print(i, i + width, len(garden[i + width]) - len(garden[i]))

    steps = 327
    score = len(garden[steps])
    increment = len(garden[steps]) - len(garden[steps - width])

    while steps != 26501365:
        increment += 30188
        score += increment
        steps += width

    print(score)

if __name__ == "__main__":
    main()
