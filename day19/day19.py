from collections import deque
from math import ceil
import time


def timeit(func):
    def helper():
        start_time = time.time()
        func()
        print('Time elapsed: '+str(time.time()-start_time))
    return helper


def comparison_func(cost, mat, prod):
    if prod == 0:
        return 0 if cost == 0 else float('inf')
    return (ceil(max(0, cost - mat) / prod)) + 1


class Blueprint:
    def __init__(self, string):
        numbers = [int(x) for x in [y.strip(':') for y in string.split()] if x.isdigit()]
        self.index = numbers[0]
        self.costs = ((numbers[1], 0, 0, 0),
                      (numbers[2], 0, 0, 0),
                      (numbers[3], numbers[4], 0, 0),
                      (numbers[5], 0, numbers[6], 0))
        self.max_costs = tuple(map(max, self.costs[0], self.costs[1], self.costs[2], self.costs[3]))

    def __str__(self):
        return str(self.costs)

    def max_geodes(self, num):
        q = deque()
        q.append((((0, 0, 0, 0), (1, 0, 0, 0)), num))
        memo = {}
        geode_max_num = 0
        while q:
            current_state = q.popleft()
            if current_state[0] in memo.keys():
                continue
            memo.update({current_state[0]: current_state[1]})
            times = []
            for index, val in enumerate(self.costs):
                if current_state[0][1][index] >= self.max_costs[index] and index != 3:
                    continue
                times.append(max(map(comparison_func, val, current_state[0][0], current_state[0][1])))
                if times[-1] <= current_state[1]:
                    new_mats = tuple(map(lambda mats, prod, cost: mats - cost + times[-1] * prod,
                                         current_state[0][0], current_state[0][1], val))
                    new_bots = list(current_state[0][1])
                    new_bots[index] += 1
                    if new_bots[index] >= self.max_costs[index] and index != 3:
                        new_bots[index] == float('inf')
                        new_mats[index] == float('inf')
                    new_bots = tuple(new_bots)

                    new_time = current_state[1] - times[-1]

                    q.append(((new_mats, new_bots), new_time))
            if min(times) >= current_state[1]:
                final_mats = tuple(map(lambda x, y: x + current_state[1]*y, current_state[0][0], current_state[0][1]))
                final_geode = final_mats[-1]
                memo.update({(final_mats, current_state[0][1]): 0})
                if final_geode > geode_max_num:
                    geode_max_num = final_geode

        return geode_max_num


@timeit
def main():
    blueprints = []
    part1_number = 0
    with open('day19input.txt') as file:
        for line in file.readlines():
            blueprints.append(Blueprint(line))
    my_list = [x.max_geodes(24)*x.index for x in blueprints]
    print('Part 1 solution: ' + str(sum(my_list)))

    print('Part 2 solution: ' + str(blueprints[0].max_geodes(32)*blueprints[1].max_geodes(32)*blueprints[2].max_geodes(32)))


if __name__ == '__main__':
    main()