import sys
from z3 import *

def main() -> None:
    data = sys.stdin.read().strip()

    stones = []
    for line in data.split("\n"):
        pos, vel = line.split(" @ ")
        pos = list(map(int, pos.split(", ")))
        vel = list(map(int, vel.split(", ")))

        stones.append((pos, vel))

    solver = Solver()

    x = Real("x")
    y = Real("y")
    z = Real("z")

    vx = Real("vx")
    vy = Real("vy")
    vz = Real("vz")

    for i, stone in enumerate(stones):
        t_intercept = Real(f"t_{i}")

        sp = stone[0]
        sv = stone[1]

        solver.add(x + vx * t_intercept == sp[0] + sv[0] * t_intercept)
        solver.add(y + vy * t_intercept == sp[1] + sv[1] * t_intercept)
        solver.add(z + vz * t_intercept == sp[2] + sv[2] * t_intercept)

    solver.check()
    print(solver.model().eval(x + y + z))

if __name__ == "__main__":
    main()
