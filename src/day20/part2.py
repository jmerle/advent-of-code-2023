import sys
from collections import *
from dataclasses import *
from math import *

check = ["qs", "sv", "pg", "sp"]

@dataclass
class FlipFlopModule:
    id: str
    state: bool
    targets: list[str]

    def update(self, src: str, high: bool, nxt: list[str], cycles: defaultdict[str, list[int]], presses: int) -> None:
        if high:
            return

        self.state = not self.state
        nxt.append(self.id)

    def pulse(self, modules, nxt: list[str], cycles: defaultdict[str, list[int]], presses: int) -> None:
        for trg in self.targets:
            if trg not in modules:
                continue

            modules[trg].update(self.id, self.state, nxt, cycles, presses)

@dataclass
class ConjunctionModule:
    id: str
    high: dict[str, bool]
    targets: list[str]

    def update(self, src: str, high: bool, nxt: list[str], cycles: defaultdict[str, list[int]], presses: int) -> None:
        self.high[src] = high
        nxt.append(self.id)

    def pulse(self, modules, nxt: list[str], cycles: defaultdict[str, list[int]], presses: int) -> None:
        send_high = not all(self.high.values())

        if send_high and self.id in check and self.id not in cycles:
            cycles[self.id] = presses

        for trg in self.targets:
            if trg not in modules:
                continue

            modules[trg].update(self.id, send_high, nxt, cycles, presses)

@dataclass
class BroadcastModule:
    id: str
    targets: list[str]

    last_high: bool = False

    def update(self, src: str, high: bool, nxt: list[str], cycles: defaultdict[str, list[int]], presses: int) -> None:
        self.last_high = high
        nxt.append(self.id)

    def pulse(self, modules, nxt: list[str], cycles: defaultdict[str, list[int]], presses: int) -> None:
        for trg in self.targets:
            if trg not in modules:
                continue

            modules[trg].update(self.id, self.last_high, nxt, cycles, presses)

def main() -> None:
    data = sys.stdin.read().strip()

    modules = {}
    for line in data.split("\n"):
        src, trg = line.split(" -> ")
        trg = trg.split(", ")

        if src[0] == "%":
            module = FlipFlopModule(src[1:], False, trg)
        elif src[0] == "&":
            module = ConjunctionModule(src[1:], {}, trg)
        else:
            module = BroadcastModule(src, trg)

        modules[module.id] = module

    for src_module in modules.values():
        for trg in src_module.targets:
            if trg not in modules:
                continue

            trg_module = modules[trg]
            if isinstance(trg_module, ConjunctionModule):
                trg_module.high[src_module.id] = False

    cycles = defaultdict(list)
    presses = 0

    while len(cycles) < len(check):
        nxt = []
        modules["broadcaster"].update("button", False, nxt, cycles, presses)
        presses += 1

        while len(nxt) > 0:
            new_nxt = []

            for id in nxt:
                modules[id].pulse(modules, new_nxt, cycles, presses)

            nxt = new_nxt

    print(lcm(*cycles.values()))

if __name__ == "__main__":
    main()
