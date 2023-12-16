import sys

def main() -> None:
    data = sys.stdin.read().strip()

    grid = [list(line) for line in data.split("\n")]

    width = len(grid[0])
    height = len(grid)

    beams = [(0, 0, 1, 0)]
    seen = set()
    energized = set()

    while len(beams) > 0:
        new_beams = []

        for beam in beams:
            x, y, dx, dy = beam

            if (x, y, dx, dy) in seen:
                continue

            if x < 0 or x >= width or y < 0 or y >= height:
                continue

            seen.add((x, y, dx, dy))
            energized.add((x, y))

            if grid[y][x] == "/":
                if dx == 1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == -1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == 0 and dy == 1:
                    dx, dy = -1, 0
                else:
                    dx, dy = 1, 0

                new_beams.append((x + dx, y + dy, dx, dy))
            elif grid[y][x] == "\\":
                if dx == 1 and dy == 0:
                    dx, dy = 0, 1
                elif dx == -1 and dy == 0:
                    dx, dy = 0, -1
                elif dx == 0 and dy == 1:
                    dx, dy = 1, 0
                else:
                    dx, dy = -1, 0

                new_beams.append((x + dx, y + dy, dx, dy))
            elif dy == 0 and grid[y][x] == "|":
                new_beams.append((x, y, 0, -1))
                new_beams.append((x, y, 0, 1))
            elif dx == 0 and grid[y][x] == "-":
                new_beams.append((x, y, -1, 0))
                new_beams.append((x, y, 1, 0))
            else:
                new_beams.append((x + dx, y + dy, dx, dy))

        beams = new_beams

    print(len(energized))

if __name__ == "__main__":
    main()
