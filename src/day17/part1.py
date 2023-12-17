import sys
from heapq import *

def main() -> None:
    data = sys.stdin.read().strip()

    grid = tuple(data.split("\n"))

    width = len(grid[0])
    height = len(grid)

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    heap = [(0, 0, 0, 0, 0), (0, 0, 0, 1, 0)]
    seen = set()

    while len(heap) > 0:
        heat, x, y, direction, streak = heappop(heap)

        if (x, y, direction, streak) in seen:
            continue

        seen.add((x, y, direction, streak))

        if x == width - 1 and y == height - 1:
            print(heat)
            return

        dx, dy = directions[direction]
        x += dx
        y += dy

        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        heat += int(grid[y][x])

        if streak < 2:
            heappush(heap, (heat, x, y, direction, streak + 1))

        heappush(heap, (heat, x, y, (direction + 1) % 4, 0))
        heappush(heap, (heat, x, y, (direction - 1) % 4, 0))

if __name__ == "__main__":
    main()
