import sys

def main() -> None:
    data = sys.stdin.read().strip()

    grid = []
    for row in data.split("\n"):
        if "#" in row:
            grid.append((row, False))
        else:
            grid.append((row, True))

    expanded_cols = set()
    for x in range(len(grid[0][0])):
        col = [row[x] for row, _ in grid]
        if "#" not in col:
            expanded_cols.add(x)

    galaxies = []

    ry = 0
    for y, (row, row_expanded) in enumerate(grid):
        rx = 0
        for x in range(len(row)):
            if grid[y][0][x] == "#":
                galaxies.append((rx, ry))

            rx += int(1e6) if x in expanded_cols else 1

        ry += int(1e6) if row_expanded else 1

    t = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ax, ay = galaxies[i]
            bx, by = galaxies[j]

            t += abs(ax - bx) + abs(ay - by)

    print(t)

if __name__ == "__main__":
    main()
