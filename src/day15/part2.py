import sys

def main() -> None:
    data = sys.stdin.read().strip()

    boxes = [[] for _ in range(256)]
    for step in data.split(","):
        if "=" in step:
            label, length = step.split("=")
            length = int(length)

            v = 0
            for ch in label:
                v += ord(ch)
                v *= 17
                v %= 256

            for arr in boxes[v]:
                if arr[0] == label:
                    arr[1] = length
                    break
            else:
                boxes[v].append([label, length])
        elif step.endswith("-"):
            label = step[:-1]

            v = 0
            for ch in label:
                v += ord(ch)
                v *= 17
                v %= 256

            boxes[v] = [arr for arr in boxes[v] if arr[0] != label]

    t = 0
    for i, box in enumerate(boxes):
        for j, arr in enumerate(box):
            t += (i + 1) * (j + 1) * arr[1]

    print(t)

if __name__ == "__main__":
    main()
