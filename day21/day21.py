from math import floor


class MonkeyGroup:
    def __init__(self, file):
        self.monkeys = dict()
        for line in open(file).readlines():
            self.monkeys[line[0:4]] = line.split()[1:]

        def eval_monkey(monkey):
            if isinstance(self.monkeys[monkey], int):
                return self.monkeys[monkey]
            if len(self.monkeys[monkey]) == 1:
                self.monkeys[monkey] = int(self.monkeys[monkey][0])
                return self.monkeys[monkey]
            if self.monkeys[monkey][1] == '+':
                return eval_monkey(self.monkeys[monkey][0]) + eval_monkey(self.monkeys[monkey][2])
            elif self.monkeys[monkey][1] == '-':
                return eval_monkey(self.monkeys[monkey][0]) - eval_monkey(self.monkeys[monkey][2])
            elif self.monkeys[monkey][1] == '*':
                return eval_monkey(self.monkeys[monkey][0]) * eval_monkey(self.monkeys[monkey][2])
            elif self.monkeys[monkey][1] == '/':
                return eval_monkey(self.monkeys[monkey][0]) / eval_monkey(self.monkeys[monkey][2])

        print(eval_monkey(self.monkeys['root'][2]))

        def binary_search(dictionary, low, high, comp_val):
            mid = floor((low+high)/2)
            dictionary['humn'] = mid
            val = eval_monkey(dictionary['root'][0])
            if val == comp_val:
                return mid
            if val < comp_val:
                return binary_search(dictionary, low, mid, comp_val)
            if val > comp_val:
                return binary_search(dictionary, mid, high, comp_val)

        print(binary_search(self.monkeys, 1, 10**15, eval_monkey(self.monkeys['root'][2])))


def main():
    our_group = MonkeyGroup('day21input.txt')


if __name__ == '__main__':
    main()