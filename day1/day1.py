input_lines = open("day1_1input.txt").readlines()


def countCalories(list):
    elfsums = [0]
    for val in list:
        if val == "\n":
            elfsums.append(0)
        else:
            elfsums[-1] += int(val[:-1])
    return elfsums


def main():
    caloriesPerElf = countCalories(input_lines)

    top3 = {0, 1, 2}
    for elf in caloriesPerElf:
        if elf > min(top3):
            top3.add(elf)
            top3.remove(min(top3))

    print(f'Part 1 solution: {max(top3)}\nPart 2 solution: {sum(top3)}')


if __name__ == '__main__':
    main()
