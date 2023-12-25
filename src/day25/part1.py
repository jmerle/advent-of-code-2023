import networkx as nx
import sys

def main() -> None:
    data = sys.stdin.read().strip()

    graph = nx.Graph()
    for line in data.split("\n"):
        component, neighbors = line.split(": ")
        for neighbor in neighbors.split(" "):
            graph.add_edge(component, neighbor)

    _, groups = nx.stoer_wagner(graph)
    print(len(groups[0]) * len(groups[1]))

if __name__ == "__main__":
    main()
