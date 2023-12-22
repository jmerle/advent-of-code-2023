import sys

def main() -> None:
    data = sys.stdin.read().strip()

    bricks = []
    occupied_cubes = set()

    for line in data.split("\n"):
        lhs, rhs = line.split("~")
        lhs = list(map(int, lhs.split(",")))
        rhs = list(map(int, rhs.split(",")))

        cubes = []
        for x in range(lhs[0], rhs[0] + 1):
            for y in range(lhs[1], rhs[1] + 1):
                for z in range(lhs[2], rhs[2] + 1):
                    cubes.append((x, y, z))

        bricks.append(cubes)
        occupied_cubes = occupied_cubes | set(cubes)

    changed = True
    while changed:
        changed = False
        new_occupied_cubes = occupied_cubes

        for brick in bricks:
            old_brick = brick[:]

            min_z = {}
            for x, y, z in brick:
                if (x, y) in min_z:
                    min_z[(x, y)] = min(min_z[(x, y)], z)
                else:
                    min_z[(x, y)] = z

            z_modifier = 0
            while True:
                z_modifier += 1

                required_empty = {(x, y, min_z[(x, y)] - z_modifier) for x, y, z in brick}
                if any(z <= 0 for x, y, z in required_empty) or any(cube in occupied_cubes for cube in required_empty):
                    z_modifier -= 1
                    break

            if z_modifier == 0:
                continue

            for i in range(len(brick)):
                brick[i] = (brick[i][0], brick[i][1], brick[i][2] - z_modifier)

            changed = True
            new_occupied_cubes = (new_occupied_cubes - set(old_brick)) | set(brick)

        occupied_cubes = new_occupied_cubes

    t = 0
    for a in bricks:
        new_occupied_cubes = occupied_cubes - set(a)

        can_disintegrate = True
        for b in bricks:
            if a == b:
                continue

            min_z = {}
            for x, y, z in b:
                if (x, y) in min_z:
                    min_z[(x, y)] = min(min_z[(x, y)], z)
                else:
                    min_z[(x, y)] = z

            required_empty = {(x, y, min_z[(x, y)] - 1) for x, y, z in b}

            if all(z > 0 for x, y, z in required_empty) and all(cube not in new_occupied_cubes for cube in required_empty):
                can_disintegrate = False
                break

        if can_disintegrate:
            t += 1

    print(t)

if __name__ == "__main__":
    main()
