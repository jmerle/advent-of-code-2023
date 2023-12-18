import sys
from shapely.geometry.polygon import *

def main() -> None:
    data = sys.stdin.read().strip()

    x, y = 0, 0
    loop = []

    for line in data.split("\n"):
        color = line.split(" ")[-1]
        distance = int(color[2:-2], 16)
        direction = int(color[-2])

        dx = [1, 0, -1, 0][direction]
        dy = [0, 1, 0, -1][direction]

        x += dx * distance
        y += dy * distance

        loop.append((x, y))

    poly = Polygon(loop)
    print(int(poly.area + poly.length // 2 + 1))

if __name__ == "__main__":
    main()
