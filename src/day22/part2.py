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

        new_bricks = [brick[:] for brick in bricks if brick != a]
        fallen_bricks = set()

        changed = True
        while changed:
            changed = False
            new_new_occupied_cubes = new_occupied_cubes

            for i, brick in enumerate(new_bricks):
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
                    if any(z <= 0 for x, y, z in required_empty) or any(cube in new_occupied_cubes for cube in required_empty):
                        z_modifier -= 1
                        break

                if z_modifier == 0:
                    continue

                for j in range(len(brick)):
                    brick[j] = (brick[j][0], brick[j][1], brick[j][2] - z_modifier)

                changed = True
                fallen_bricks.add(i)

                new_new_occupied_cubes = (new_new_occupied_cubes - set(old_brick)) | set(brick)

            new_occupied_cubes = new_new_occupied_cubes

        t += len(fallen_bricks)

    print(t)

if __name__ == "__main__":
    main()
