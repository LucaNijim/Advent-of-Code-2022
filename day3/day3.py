def letters_to_numbers(num, list):
    if ord(num) <= 97:
        list.append(ord(num) - 38)
    else:
        list.append(ord(num) - 96)


class Rucksack(str):
    def priority(self):
        first_half, second_half = set(self[:len(self) // 2]), set(self[len(self) // 2:])
        chars_in_common = []
        for y in first_half:
            if y in second_half:
                letters_to_numbers(y, chars_in_common)
        return sum(chars_in_common)


def priority_group(list_of_strings):
    chars_in_common = []
    for y in set(list_of_strings[0]).difference({'\n'}):
        if y in set(list_of_strings[1]) and y in set(list_of_strings[2]):
            letters_to_numbers(y, chars_in_common)
    return sum(chars_in_common)


day3input_lines = open('day3input.txt').readlines()

print(day3input_lines[0])

# for part 1
sum_vals = 0
for x in day3input_lines:
    sum_vals += Rucksack(x).priority()
print(sum_vals)

# for part 2
sum_vals = 0
for z in range(len(day3input_lines) // 3):
    sum_vals += priority_group(day3input_lines[3 * z:3 * z + 3])
print(sum_vals)

# Maybe classes would have worked better! Big lesson learned:
# It's strictly less than for the upper bound of a slice.
