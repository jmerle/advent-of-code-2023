import sys
from graph_tool import Graph
from graph_tool.topology import all_paths

def main() -> None:
    data = sys.stdin.read().strip()

    grid = data.split("\n")

    width = len(grid[0])
    height = len(grid)

    edges = []
    for y in range(height):
        for x in range(width):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= width or ny < 0 or ny >= height:
                    continue

                if grid[ny][nx] == "#":
                    continue

                edges.append((y * height + x, ny * height + nx))

    graph = Graph(edges)
    max_length = 0

    for path in all_paths(graph, 1, (height - 1) * height + (width - 2)):
        max_length = max(max_length, len(path) - 1)

    print(max_length)

if __name__ == "__main__":
    main()
