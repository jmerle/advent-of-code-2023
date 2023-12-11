import sys

def main() -> None:
    data = sys.stdin.read().strip()

    lines = []
    for line in data.split("\n"):
        if "#" in line:
            lines.append(line)
        else:
            lines.extend([line, line])

    doubled_cols = []
    for x in range(len(lines[0])):
        col = [line[x] for line in lines]
        if "#" not in col:
            doubled_cols.append(x)

    grid = []
    for line in lines:
        row = []
        for x in range(len(line)):
            if x in doubled_cols:
                row.extend([line[x], line[x]])
            else:
                row.append(line[x])

        grid.append(row)

    width = len(grid[0])
    height = len(grid)

    galaxies = []
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "#":
                galaxies.append((x, y))

    t = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ax, ay = galaxies[i]
            bx, by = galaxies[j]

            t += abs(ax - bx) + abs(ay - by)

    print(t)

if __name__ == "__main__":
    main()
