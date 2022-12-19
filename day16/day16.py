from collections import defaultdict


def luca_bfs(graph: dict, start_node):
    visited_nodes = set()
    queue = [start_node]
    distance_from_start = defaultdict(lambda: float('inf'))
    distance_from_start[start_node] = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        visited_nodes.add(current_node)

        for node in graph[current_node]:
            if node in visited_nodes:
                continue

            new_distance = distance_from_start[current_node] + 1
            if new_distance < distance_from_start[node]:
                distance_from_start[node] = new_distance
                queue.append(node)
    return distance_from_start


def all_possible_choices(graph: dict, start_node, length):
    possible_paths = set((start_node,))
    for i in range(length):
        x = max([len(x) for x in possible_paths])
        for path in {path for path in possible_paths if len(path) == x}:
            if type(path) == str:
                for new_node in graph[path] + (path,):
                    possible_paths.add(tuple((path,) + (new_node,)))
            else:
                for new_node in graph[path[-1]] + (path[-1],):
                    possible_paths.add(tuple(path)+(new_node,))
    ret_val = {path for path in possible_paths if len(path) == length}
    print(ret_val)
    return ret_val


class PipeNetwork:
    def __init__(self, file):
        input_lines = open(file).readlines()
        self.valve_names = [y.split(' ')[1] for y in input_lines]
        self.valve_connections = dict.fromkeys(self.valve_names, None)
        self.valve_flow_rates = dict.fromkeys(self.valve_names, None)
        for index, line in enumerate(input_lines):
            connections = line.split('to valve')[1].split(', ')
            connections = tuple([x.strip('s \n') for x in connections])
            self.valve_connections[self.valve_names[index]] = connections

            flow_rate = int(line.split('=')[1].split(';')[0])
            self.valve_flow_rates[self.valve_names[index]] = flow_rate

        self.useful_valves = ['AA']

        for key in self.valve_flow_rates:
            if self.valve_flow_rates[key] > 0:
                self.useful_valves.append(key)

        self.useful_distances = dict.fromkeys(self.useful_valves, None)

        for key in self.useful_distances:
            self.useful_distances[key] = luca_bfs(self.valve_connections, key)
            unwanted_keys = set(self.valve_names) - set(self.useful_valves)
            for unwanted_key in unwanted_keys:
                del self.useful_distances[key][unwanted_key]

        print(self.useful_distances)

    def get_max_flow(self):
        all_possible_games = all_possible_choices(self.valve_connections, 'AA', 30)
        print(all_possible_games)
        # what do we actually need to do here?
        # First, we need to find every possible path of length 30 in the graph
        # Then, we need a score function that takes a path as input, and returns the score


our_network = PipeNetwork('day16practiceinput.txt')
