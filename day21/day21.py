from math import floor
from time import time


def timeit(func):
    def helper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print('Time elapsed: '+ str(time()-start_time))

    return helper


class MonkeyGroup:
    def __init__(self, file):
        self.monkeys = dict()
        for line in open(file).readlines():
            self.monkeys[line[0:4]] = line.split()[1:]

    def eval_monkey(self, monkey):
        if isinstance(self.monkeys[monkey], int):
            return self.monkeys[monkey]
        if len(self.monkeys[monkey]) == 1:
            self.monkeys[monkey] = int(self.monkeys[monkey][0])
            return self.monkeys[monkey]
        if self.monkeys[monkey][1] == '+':
            return self.eval_monkey(self.monkeys[monkey][0]) + self.eval_monkey(self.monkeys[monkey][2])
        elif self.monkeys[monkey][1] == '-':
            return self.eval_monkey(self.monkeys[monkey][0]) - self.eval_monkey(self.monkeys[monkey][2])
        elif self.monkeys[monkey][1] == '*':
            return self.eval_monkey(self.monkeys[monkey][0]) * self.eval_monkey(self.monkeys[monkey][2])
        elif self.monkeys[monkey][1] == '/':
            return int(self.eval_monkey(self.monkeys[monkey][0]) / self.eval_monkey(self.monkeys[monkey][2]))

    def binary_search(self, low, high, comp_val):
        mid = floor((low + high) / 2)
        self.monkeys['humn'] = mid
        val = self.eval_monkey(self.monkeys['root'][0])
        if val == comp_val:
            return mid
        if val < comp_val:
            return self.binary_search(low, mid, comp_val)
        if val > comp_val:
            return self.binary_search(mid, high, comp_val)


def main():
    our_group = MonkeyGroup('day21input.txt')
    print('Part 1 result: ' + str(timeit(our_group.eval_monkey)('root')))
    print('Part 2 result: ' + str(timeit(our_group.binary_search)(1, 10 ** 15,
                                                          our_group.eval_monkey(our_group.monkeys['root'][2]))))


if __name__ == '__main__':
    main()
