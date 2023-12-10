import sys
from collections import *

def main() -> None:
    data = sys.stdin.read().strip()

    neighbors = defaultdict(list)

    grid = data.split("\n")

    width = len(grid[0])
    height = len(grid)

    source = None

    for y in range(height):
        for x in range(width):
            coord = (x, y)

            if grid[y][x] == "S":
                source = coord
            elif grid[y][x] == "|":
                neighbors[coord].extend([(x, y - 1), (x, y + 1)])
            elif grid[y][x] == "-":
                neighbors[coord].extend([(x - 1, y), (x + 1, y)])
            elif grid[y][x] == "L":
                neighbors[coord].extend([(x, y - 1), (x + 1, y)])
            elif grid[y][x] == "J":
                neighbors[coord].extend([(x, y - 1), (x - 1, y)])
            elif grid[y][x] == "7":
                neighbors[coord].extend([(x, y + 1), (x - 1, y)])
            elif grid[y][x] == "F":
                neighbors[coord].extend([(x, y + 1), (x + 1, y)])

    for coord in list(neighbors.keys()):
        if source in neighbors[coord]:
            neighbors[source].append(coord)

    visited = set()
    q = deque()
    q.append((source, 0))
    max_distance = 0

    while len(q) > 0:
        node, distance = q.popleft()

        if node in visited:
            continue

        visited.add(node)

        x, y = node
        if x < 0 or x >= width or y < 0 or y >= height:
            continue

        max_distance = max(max_distance, distance)

        for neighbor in neighbors[node]:
            q.append((neighbor, distance + 1))

    print(max_distance)

if __name__ == "__main__":
    main()
