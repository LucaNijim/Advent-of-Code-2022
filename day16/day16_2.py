#Ideas for this program
#First, we should create a dictionary with each node name and its flow rate
#We should make a graph of each node and its connections
def floyd_warshall(graph):
    shortest_path = dict()
    for x in graph:
        for y in graph:
            if x == y:
                shortest_path[(x, y)] = 0
            elif y in graph[x]:
                shortest_path[(x, y)] = 1
            else:
                shortest_path[(x, y)] = float('inf')
    while float('inf') in shortest_path.values():
        for i in graph:
            for j in graph:
                for k in graph:
                    shortestij = shortest_path[(i, j)]
                    shortestjk = shortest_path[(j, k)]
                    if shortestij + shortestjk < shortest_path[(i, k)]:
                        shortest_path[(i, k)] = shortestij + shortestjk
    return shortest_path
    # we wish to return a dictionary with tuples for keys


def calc_max(nodes, distances, flow_rates):
    possible_paths = set()
    possible_scores = set()
    for x in possible_paths:
        possible_score = 0
        for index, node in enumerate(x):
            pass
    return max(possible_scores)

class PipeNetwork:
    def __init__(self, file):
        input_lines = open(file).readlines()
        self.valves = set()
        self.valve_flow_rates = dict()
        self.valve_graph = dict()
        for line in input_lines:
            new_val = line.split(' ')[1]
            self.valves.add(new_val)
            self.valve_flow_rates[new_val] = int(line.split('=')[1].split(';')[0])
            connections = []
            for valve in line.split('to valve')[1].strip('s \n').split(', '):
                connections.append(valve)
            self.valve_graph[new_val] = tuple(connections)
        self.useful_valves = set([x for x in self.valves if self.valve_flow_rates[x] > 0 or x == 'AA'])
        fw = floyd_warshall(self.valve_graph)
        self.weighted_graph = {k: v for (k, v) in fw.items() if k[0] and k[1] in self.useful_valves}
        calc_max(self.useful_valves, self.weighted_graph, self.valve_flow_rates)





our_network = PipeNetwork('day16input.txt')
