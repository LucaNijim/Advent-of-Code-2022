import numpy as np
from collections import defaultdict
import heapq as heap


def lucas_dijkstra_algorithm(graph: dict, start_node):
    visited_nodes = set()
    parents_map = defaultdict(lambda: None)
    node_costs = defaultdict(lambda: float('inf'))
    node_costs[start_node] = 0
    priority_queue = []
    heap.heappush(priority_queue, (0, start_node))

    while len(priority_queue) > 0:
        _, node = heap.heappop(priority_queue)
        visited_nodes.add(node)

        for adjacent_node in graph[node]:
            if adjacent_node in visited_nodes:
                continue

            new_cost = node_costs[node] + 1

            if node_costs[adjacent_node] > new_cost:
                parents_map[adjacent_node] = node
                visited_nodes.add(adjacent_node)
                node_costs[adjacent_node] = new_cost
                heap.heappush(priority_queue, (new_cost, adjacent_node))
    return parents_map, node_costs


class HeightMap:
    def __init__(self, file):
        input_lines = [line.strip(' \n') for line in open(file).readlines()]
        self.nodes = np.zeros((len(input_lines), len(input_lines[0])))
        for index, _ in np.ndenumerate(self.nodes):
            self.nodes[index] = ord(input_lines[index[0]][index[1]]) - 97
            if self.nodes[index] == 83 - 97:
                self.start_node = index
                self.nodes[index] = 0
            if self.nodes[index] == 69 - 97:
                self.end_node = index
                self.nodes[index] = 25
        self.graph = {index: None for index, _ in np.ndenumerate(self.nodes)}
        for key in self.graph:
            nodes_attached = []
            threshold = self.nodes[key] + 1
            if key[0] >= 1:
                if self.nodes[key[0] - 1, key[1]] <= threshold:
                    nodes_attached.append((key[0] - 1, key[1]))
            if key[0] <= self.nodes.shape[0] - 2:
                if self.nodes[key[0] + 1, key[1]] <= threshold:
                    nodes_attached.append((key[0] + 1, key[1]))
            if key[1] >= 1:
                if self.nodes[key[0], key[1] - 1] <= threshold:
                    nodes_attached.append((key[0], key[1] - 1))
            if key[1] <= self.nodes.shape[1] - 2:
                if self.nodes[key[0], key[1] + 1] <= threshold:
                    nodes_attached.append((key[0], key[1] + 1))
            self.graph[key] = tuple(nodes_attached)

        self.shortest_path = lucas_dijkstra_algorithm(self.graph, self.start_node)[1][self.end_node]

        a_distances = []
        for index, height in np.ndenumerate(self.nodes):
            if height == 0:
                a_distances.append(lucas_dijkstra_algorithm(self.graph, index)[1][self.end_node])
        a_distances.sort()
        self.nearest_a = a_distances[0]


def main():
    height_map = HeightMap('day12input.txt')
    print(height_map.shortest_path)
    print(height_map.nearest_a)


if __name__ == '__main__':
    main()
