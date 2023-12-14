import sys

def update(grid: list[list[str]]) -> None:
    width = len(grid[0])
    height = len(grid)

    for _ in range(100):
        for y in range(height - 1, 0, -1):
            for x in range(width):
                if grid[y][x] == "O" and grid[y - 1][x] == ".":
                    grid[y][x], grid[y - 1][x] = grid[y - 1][x], grid[y][x]

    for _ in range(100):
        for x in range(width - 1, 0, -1):
            for y in range(height):
                if grid[y][x] == "O" and grid[y][x - 1] == ".":
                    grid[y][x], grid[y][x - 1] = grid[y][x - 1], grid[y][x]

    for _ in range(100):
        for y in range(height - 1):
            for x in range(width):
                if grid[y][x] == "O" and grid[y + 1][x] == ".":
                    grid[y][x], grid[y + 1][x] = grid[y + 1][x], grid[y][x]

    for _ in range(100):
        for x in range(width - 1):
            for y in range(height):
                if grid[y][x] == "O" and grid[y][x + 1] == ".":
                    grid[y][x], grid[y][x + 1] = grid[y][x + 1], grid[y][x]

def get_load(grid: list[list[str]]) -> int:
    width = len(grid[0])
    height = len(grid)

    load = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "O":
                load += height - y

    return load

def main() -> None:
    data = sys.stdin.read().strip()

    grid = [list(line) for line in data.split("\n")]
    last_seen = {}

    iterations = int(1e9)
    for i in range(iterations):
        update(grid)

        key = "".join("".join(row) for row in grid)
        if key in last_seen:
            remaining = iterations - i - 1
            cycle_length = i - last_seen[key]

            for _ in range(remaining - (remaining // cycle_length * cycle_length)):
                update(grid)

            print(get_load(grid))
            break

        last_seen[key] = i

if __name__ == "__main__":
    main()
