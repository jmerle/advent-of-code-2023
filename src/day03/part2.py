import sys
from collections import *

def get_adjacents(x, y, width, height):
    out = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue

            nx = x + dx
            ny = y + dy

            if nx >= 0 and nx < width and ny >= 0 and ny < height:
                out.append((nx, ny))

    return out

def main() -> None:
    data = sys.stdin.read().strip()

    grid = data.split("\n")

    width = len(grid[0])
    height = len(grid)

    d = defaultdict(list)

    t = 0
    for y in range(height):
        x = 0
        while x < width:
            if not grid[y][x].isdigit():
                x += 1
                continue

            checks = get_adjacents(x, y, width, height)
            num = grid[y][x]

            for i in range(x + 1, width):
                if not grid[y][i].isdigit():
                    break

                num += grid[y][i]
                checks.extend(get_adjacents(i, y, width, height))
                x += 1

            for nx, ny in checks:
                if grid[ny][nx] == "*":
                    d[(nx, ny)].append(int(num))
                    break

            x += 1

    for nums in d.values():
        if len(nums) > 1:
            result = 1
            for num in nums:
                result *= num
            t += result

    print(t)

if __name__ == "__main__":
    main()
