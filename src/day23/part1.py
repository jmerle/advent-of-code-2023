import sys

def main() -> None:
    data = sys.stdin.read().strip()

    grid = data.split("\n")

    width = len(grid[0])
    height = len(grid)

    source = (1, 0)
    queue = [(source, set([source]))]

    max_length = 0

    directions = {
        ">": [(1, 0)],
        "<": [(-1, 0)],
        "v": [(0, 1)],
        "^": [(0, -1)],
        ".": [(-1, 0), (1, 0), (0, -1), (0, 1)]
    }

    while len(queue) > 0:
        (x, y), visited = queue.pop()

        if x == width - 2 and y == height - 1:
            max_length = max(max_length, len(visited) - 1)
            continue

        for dx, dy in directions[grid[y][x]]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue

            if grid[ny][nx] == "#":
                continue

            if (nx, ny) in visited:
                continue

            queue.append(((nx, ny), visited | set([(nx, ny)])))

    print(max_length)

if __name__ == "__main__":
    main()
