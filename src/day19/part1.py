import re
import sys

def main() -> None:
    data = sys.stdin.read().strip()

    sections = data.split("\n\n")

    workflows = {}
    for line in sections[0].split("\n"):
        id, steps = line.split("{")
        workflows[id] = []

        for step in steps[:-1].split(","):
            done = False

            for ch in "xmas":
                for op in "<>":
                    if step.startswith(ch + op):
                        value = int(step[2:].split(":")[0])
                        nxt = step.split(":")[1]
                        workflows[id].append((ch, op, value, nxt))
                        done = True

            if not done:
                workflows[id].append((step,))

    t = 0
    for part in sections[1].split("\n"):
        nums = list(map(int, re.findall(r"(\d+)", part)))
        d = {"x": nums[0], "m": nums[1], "a": nums[2], "s": nums[3]}

        workflow = "in"
        while workflow != "A" and workflow != "R":
            for step in workflows[workflow]:
                if len(step) == 4 and step[1] == "<" and d[step[0]] < step[2]:
                    workflow = step[3]
                    break
                elif len(step) == 4 and step[1] == ">" and d[step[0]] > step[2]:
                    workflow = step[3]
                    break
                elif len(step) == 1:
                    workflow = step[0]
                    break

        if workflow == "A":
            t += sum(nums)

    print(t)

if __name__ == "__main__":
    main()
