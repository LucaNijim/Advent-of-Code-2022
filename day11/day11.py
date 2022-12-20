import math


class Monkey:
    def __init__(self, monkey_text):
        monkey_text = [x.strip('Starting items: \n') for x in monkey_text]
        self.items = [int(x) for x in monkey_text[1].split(', ')]
        self.operation = monkey_text[2].split(' ')[-2], monkey_text[2].split(' ')[-1]
        self.divis_test = int(monkey_text[3].split(' ')[-1])
        self.target = tuple([int(monkey_text[x].split(' ')[-1]) for x in (4, 5)])
        self.items_inspected = 0
        self.outgoing_mail = []

    def take_turn(self, mod_val):
        self.items_inspected += len(self.items)
        ret_list = []
        to_monkey = []
        for x in range(len(self.items)):
            if self.operation[0] == '*':
                if self.operation[1] == 'old':
                    self.items[0] *= self.items[0]
                else:
                    self.items[0] *= int(self.operation[1])
            else:
                if self.operation[1] == 'old':
                    self.items[0] += self.items[0]
                else:
                    self.items[0] += int(self.operation[1])
            #for the first round, leave the next line, for the second, comment it out
            #self.items[0] /= 3
            #self.items[0] = math.floor(self.items[0])

            self.items[0] = self.items[0] % mod_val
            ret_list.append(self.items[0])
            to_monkey.append(self.target[0] if self.items[0] % self.divis_test == 0 else self.target[1])
            self.items.pop(0)

        self.outgoing_mail = list(zip(ret_list, to_monkey))


class MonkeyPack:
    def __init__(self, file):
        input_lines = open(file).readlines()
        chunks = [input_lines[7*x:7+7*x] for x in range(math.ceil(len(input_lines)/7))]
        self.monkeys = []
        for chunk in chunks:
            self.monkeys.append(Monkey(chunk))
        self.mod_val = 1
        for monkey in self.monkeys:
            self.mod_val *= monkey.divis_test

    def take_turn(self):
        for monkey in self.monkeys:
            monkey.take_turn(self.mod_val)
            for package in monkey.outgoing_mail:
                self.monkeys[package[1]].items.append(package[0])
            monkey.outgoing_mail = []


def main():
    monkey_in_middle = MonkeyPack('day11input.txt')
    for x in range(10000):
        monkey_in_middle.take_turn()

    print([x.items_inspected for x in monkey_in_middle.monkeys])
    most_used_monkeys = sorted([x.items_inspected for x in monkey_in_middle.monkeys], reverse=True)
    print(most_used_monkeys[0] * most_used_monkeys[1])


if __name__ == '__main__':
    main()