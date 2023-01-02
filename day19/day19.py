import re
from collections import deque
from math import ceil


class Blueprint:
    def __init__(self, string):
        numbers = [x for x in [y.strip(':') for y in string.split()] if x.isnumeric()]
        print(numbers)
        self.index = int(numbers[0])
        self.ore_bot_cost = int(numbers[1])
        self.clay_bot_cost = int(numbers[2])
        self.obsidian_bot_cost = tuple(int(x) for x in numbers[3:5])
        self.geode_bot_cost = tuple(int(x) for x in numbers[4:])
        print(self.obsidian_bot_cost)

        # The order for the inventory will be ore, clay, obsidian, geodes
        # then ore bots, clay bots, obsidian bots, and geode bots.

        self.inventory = (0, 0, 0, 0, 1, 0, 0, 0)

    def max_geodes(self, time):
        q = deque()
        q.append(self.inventory + (time,))
        memo = set()
        while q:
            cs = q.popleft()  # cs is current state
            if cs in memo:
                print('memoed')
                continue
            memo.add(cs)
            if cs[-1] > 0:
                # This loop will only run if there's time left
                ore_time = 1 + max(0, ceil((self.ore_bot_cost - cs[0]) / cs[4]))

                q.append((cs[0] + ore_time * cs[4] - self.ore_bot_cost,
                          cs[1] + ore_time * cs[5],
                          cs[2] + ore_time * cs[6],
                          cs[3] + ore_time * cs[7],
                          cs[4] + 1, cs[5], cs[6], cs[7],
                          cs[-1] - ore_time))

                clay_time = 1 + max(0, ceil((self.clay_bot_cost - cs[0]) / cs[4]))
                q.append((cs[0] + clay_time * cs[4] - self.clay_bot_cost,
                          cs[1] + clay_time * cs[5],
                          cs[2] + clay_time * cs[6],
                          cs[3] + clay_time * cs[7],
                          cs[4], cs[5] + 1, cs[6], cs[7],
                          cs[-1] - clay_time))
                if cs[5] > 0:
                    obs_time = 1 + max(0, ceil((self.obsidian_bot_cost[0] - cs[0]) / cs[4]),
                                       ceil((self.obsidian_bot_cost[1] - cs[1])) / cs[5])
                    q.append((cs[0] + obs_time * cs[4] - self.obsidian_bot_cost[0],
                              cs[1] + obs_time * cs[5] - self.obsidian_bot_cost[1],
                              cs[2] + obs_time * cs[6],
                              cs[3] + obs_time * cs[7],
                              cs[4], cs[5], cs[6] + 1, cs[7],
                              cs[-1] - obs_time))
                if cs[6] > 0:

                    geode_time = 1 + max(0, ceil((self.geode_bot_cost[0] - cs[0]) / cs[4]),
                                         ceil((self.geode_bot_cost[1] - cs[2]) / cs[6]))

                    q.append((cs[0] + geode_time * cs[4] - self.obsidian_bot_cost[0],
                              cs[1] + geode_time * cs[5],
                              cs[2] + geode_time * cs[6] - self.obsidian_bot_cost[1],
                              cs[3] + geode_time * cs[7],
                              cs[4], cs[5], cs[6], cs[7] + 1,
                              cs[-1] - geode_time))
        print(max(x[3] for x in memo))


def main():
    blueprints = []
    with open('day19practiceinput.txt') as f:
        for line in f.readlines():
            blueprints.append(Blueprint(line))
    blueprints[0].max_geodes(18)
    # print('Part 1 result: ' + str(sum(x.index * x.max_geodes(24) for x in blueprints)))


if __name__ == '__main__':
    main()

# For part one, we need to print the sum of the product of a blueprint's index with its max score for 24
