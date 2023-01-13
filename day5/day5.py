class Instruction(str):
    def __init__(self, string):
        self.quantity, self.target, self.destination = [int(x) for x in self.replace('move ', '').replace('from ', '').replace('to ', '').replace('\n', '').split(' ')]


class BoxState():
    def __init__(self, list_of_rows):
        rows_right_order = list_of_rows
        rows_right_order.reverse()
        indexes_list = [int(x) - 1 for x in rows_right_order[0].split()]
        rows_right_order = rows_right_order[1:]
        nice_list = []
        for i in indexes_list:
            nice_list.append([])
        for row in rows_right_order:
            if len(row) < 4 * len(indexes_list):
                row += ' ' * (4 * len(indexes_list) - len(row))
            for entry in indexes_list:
                newAddition = row[4 * (entry) + 1]
                if newAddition == ' ':
                    pass
                else:
                    nice_list[entry].append(row[4 * (entry) + 1])
        self.list_of_stacks = nice_list

    def Operation(self, quantity, target, destination):
        var = self.list_of_stacks[target][-quantity:]
        var.reverse()
        self.list_of_stacks[destination] += var
        self.list_of_stacks[target] = self.list_of_stacks[target][0:-quantity]

    def Day2Operation(self, quantity, target, destination):
        var = self.list_of_stacks[target][-quantity:]
        self.list_of_stacks[destination] += var
        self.list_of_stacks[target] = self.list_of_stacks[target][0:-quantity]


def main():
    practice = True
    if practice:
        target_string = 'day5practiceinput.txt'
    else:
        target_string = 'day5input.txt'
    input_lines = open(target_string).readlines()

    start_state_pt1, start_state_pt2, instruction_list = [], [], []
    targ_list = (start_state_pt1, start_state_pt2)

    for line in input_lines:
        if line == '\n':
            targ_list = instruction_list
        else:
            if type(targ_list) == tuple:
                for x in targ_list:
                    x.append(line)
            else:
                targ_list.append(line)

    instruction_list = [Instruction(x) for x in instruction_list]
    start_state_pt1 = BoxState(start_state_pt1)
    start_state_pt2 = BoxState(start_state_pt2)
    for line in targ_list:
        line = Instruction(line)
        start_state_pt1.Operation(line.quantity, line.target - 1, line.destination - 1)
        start_state_pt2.Day2Operation(line.quantity, line.target - 1, line.destination - 1)

    day_1_submit_string = ''
    day_2_submit_string = ''
    for stack in start_state_pt1.list_of_stacks:
        day_1_submit_string += stack[-1]
    for stack in start_state_pt2.list_of_stacks:
        day_2_submit_string += stack[-1]
    print(f'Part 1 solution: {day_1_submit_string}\nPart 2 solution: {day_2_submit_string}')


if __name__ == '__main__':
    main()
