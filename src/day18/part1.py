import sys

def fill(lava, visited, width, height, x, y):
    seen = set()
    is_lava = True

    queue = [(x, y)]

    while len(queue) > 0:
        x, y = queue.pop()

        if (x, y) in seen:
            continue

        if lava[y][x]:
            continue

        if x == 0 or x == width - 1 or y == 0 or y == height - 1:
            is_lava = False
            continue

        seen.add((x, y))

        if x > 0:
            queue.append((x - 1, y))

        if x < width - 1:
            queue.append((x + 1, y))

        if y > 0:
            queue.append((x, y - 1))

        if y < height - 1:
            queue.append((x, y + 1))

    for x, y in seen:
        lava[y][x] = is_lava
        visited[y][x] = True

def main() -> None:
    data = sys.stdin.read().strip()

    x, y = 0, 0
    loop = set()

    min_x = 1e9
    max_x = -1e9
    min_y = 1e9
    max_y = -1e9

    for line in data.split("\n"):
        direction, distance, _ = line.split(" ")
        distance = int(distance)

        dx = {"R": 1, "L": -1}.get(direction, 0)
        dy = {"D": 1, "U": -1}.get(direction, 0)

        for i in range(distance):
            x += dx
            y += dy

            loop.add((x, y))

            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    loop = [(x + abs(min_x), y + abs(min_y)) for x, y in loop]

    lava = [[False] * width for _ in range(height)]
    visited = [[False] * width for _ in range(height)]

    for x, y in loop:
        lava[y][x] = True
        visited[y][x] = True

    for y in range(height):
        for x in range(width):
            if not visited[y][x]:
                fill(lava, visited, width, height, x, y)

    print(sum(sum(row) for row in lava))

if __name__ == "__main__":
    main()
