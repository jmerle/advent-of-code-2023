import sys
from dataclasses import *

@dataclass
class FlipFlopModule:
    id: str
    state: bool
    targets: list[str]

    def update(self, src: str, high: bool, counts: dict[bool, int], nxt: list[str]) -> None:
        counts[high] += 1

        if high:
            return

        self.state = not self.state
        nxt.append(self.id)

    def pulse(self, modules, counts: dict[bool, int], nxt: list[str]) -> None:
        for trg in self.targets:
            if trg not in modules:
                counts[self.state] += 1
                continue

            modules[trg].update(self.id, self.state, counts, nxt)

@dataclass
class ConjunctionModule:
    id: str
    high: dict[str, bool]
    targets: list[str]

    def update(self, src: str, high: bool, counts: dict[bool, int], nxt: list[str]) -> None:
        counts[high] += 1
        self.high[src] = high
        nxt.append(self.id)

    def pulse(self, modules, counts: dict[bool, int], nxt: list[str]) -> None:
        send_high = not all(self.high.values())
        for trg in self.targets:
            if trg not in modules:
                counts[send_high] += 1
                continue

            modules[trg].update(self.id, send_high, counts, nxt)

@dataclass
class BroadcastModule:
    id: str
    targets: list[str]

    last_high: bool = False

    def update(self, src: str, high: bool, counts: dict[bool, int], nxt: list[str]) -> None:
        counts[high] += 1
        self.last_high = high
        nxt.append(self.id)

    def pulse(self, modules, counts: dict[bool, int], nxt: list[str]) -> None:
        for trg in self.targets:
            if trg not in modules:
                counts[self.last_high] += 1
                continue

            modules[trg].update(self.id, self.last_high, counts, nxt)

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
        if not isinstance(src_module, ConjunctionModule):
            for trg in src_module.targets:
                trg_module = modules[trg]
                if isinstance(trg_module, ConjunctionModule):
                    trg_module.high[src_module.id] = False

    counts = {False: 0, True: 0}

    for _ in range(1000):
        nxt = []
        modules["broadcaster"].update("button", False, counts, nxt)

        while len(nxt) > 0:
            new_nxt = []

            for id in nxt:
                modules[id].pulse(modules, counts, new_nxt)

            nxt = new_nxt

    print(counts[False] * counts[True])

if __name__ == "__main__":
    main()
