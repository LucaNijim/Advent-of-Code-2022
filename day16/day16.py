from collections import defaultdict, deque
from itertools import permutations
import time


# I'm still trying to get a handle on decorators, this is a pretty straightforward one
# We use it to decorate the main function, but we could also use it on any internal function, which is pretty handy
def timeit(func):
    def helper():
        start_time = time.time()
        func()
        print('Time elapsed: '+str(time.time()-start_time))
    return helper


# The floyd warshall algorithm is used to calculate the shortest path between every point in a graph.
def floyd_warshall(graph, subset):
    # spg stands for shortest path graph
    spg = defaultdict(lambda: float('inf'))
    for node in graph.keys():
        spg[(node, node)] = 0
        for new_node in graph[node]:
            spg[(node, new_node)] = spg[(new_node, node)] = 1
    for i, j, k in permutations(graph.keys(), 3):
        if spg[(i, j)] + spg[(j, k)] < spg[(i, k)]:
            spg[(i, k)] = spg[(k, i)] = spg[(i, j)] + spg[(j, k)]
    return {x: spg[x] for x in spg.keys() if x[0] in subset and x[1] in subset}


# We make this class PipeNetwork to represent the space of our problem
class PipeNetwork:
    def __init__(self, file):
        # Here, we initialize a list of valves, and dictionaries to represent the valve flow rates and valve connections
        self.valves = set()
        self.valve_flow_rates = {}
        self.connections = {}

        # We loop through each line of the file and appropriately update the three properties
        input_lines = open(file).readlines()
        for line in input_lines:
            valve = line.split()[1]
            self.valves.add(valve)
            self.valve_flow_rates[valve] = int(line.split()[4].strip('rate=;'))
            connected_valves = [x for x in line.split('valve')[1].strip('s \n').split(', ')]
            self.connections[valve] = set(connected_valves)

        # The useful valves are the ones which have flow rates > 0
        self.useful_valves = {x for x in self.valves if self.valve_flow_rates[x] > 0} | {'AA'}
        self.spg = floyd_warshall(self.connections, self.useful_valves)

    def highest_flow(self, T, elephant=False):  # T is the max time
        def add(queue, open_valves, cv, time_remaining, score):
            if time_remaining >= 0:
                queue.append((open_valves, cv, time_remaining))
                if saved_max_score[(open_valves, cv, time_remaining)] < score:
                    saved_max_score[(open_valves, cv, time_remaining)] = score
        # This function should return the highest possible flow
        q = deque()
        q.append((frozenset({'AA'}), 'AA', T))
        saved_max_score = defaultdict(lambda: 0)  # We store potential maxes for each state in the state space here
        # We will write states in as ({open valves}, current_valve, time_remaining) and assign them to an int score
        while len(q) > 0:
            current_state = q.popleft()
            # Get the next state, initialize these current values
            current_open, current_valve, current_time = current_state
            current_score = saved_max_score[(current_open, current_valve, current_time)]
            if current_time > 0:
                add(q,
                    current_open,
                    current_valve,
                    0,
                    current_score + sum(
                        {current_time * self.valve_flow_rates[open_valve] for open_valve in current_open}))
            for new_valve in self.useful_valves.difference(current_open):
                new_open = frozenset(current_open | {new_valve})
                dist = self.spg[(current_valve, new_valve)] + 1
                new_time = current_time - dist
                new_score = current_score + sum({dist * self.valve_flow_rates[open_valve] for open_valve in current_open})
                add(q, new_open, new_valve, new_time, new_score)
        return max(saved_max_score.values())


@timeit
def main():
    our_network = PipeNetwork('day16input.txt')
    print(our_network.highest_flow(30))
    print(our_network.highest_flow(26, True))


if __name__ == '__main__':
    main()