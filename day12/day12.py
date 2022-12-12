import numpy as np
from collections import defaultdict
import heapq as heap


def lucas_dijkstra_algorithm(graph: dict, start_node):



class HeightMap:
    def __init__(self, file):
        input_lines = [x.strip(' \n') for x in open(file).readlines()]
        self.nodes = np.zeros((len(input_lines), len(input_lines[0])))
        for index, x in np.ndenumerate(self.nodes):
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
        self.shortest_path_length =


map = HeightMap('day12input.txt')
print(map.graph)

