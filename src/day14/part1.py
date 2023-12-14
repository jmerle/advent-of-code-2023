import sys

def main() -> None:
    data = sys.stdin.read().strip()

    grid = [list(line) for line in data.split("\n")]

    width = len(grid[0])
    height = len(grid)

    for _ in range(100):
        for y in range(height - 1, 0, -1):
            for x in range(width):
                if grid[y][x] == "O" and grid[y - 1][x] == ".":
                    grid[y][x], grid[y - 1][x] = grid[y - 1][x], grid[y][x]

    t = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "O":
                t += height - y

    print(t)

if __name__ == "__main__":
    main()
