def main():
    # These two variables should both be set to 1 for part 1
    dec_key = 811589153
    repeats = 10

    with open('day20input.txt') as file:
        original_numbers = [int(x.strip(' \n'))*dec_key for x in file.readlines()]
    reorder_nums = list(enumerate(original_numbers.copy()))
    length = len(original_numbers)

    for i in range(repeats):
        for index, val in enumerate(original_numbers):
            j_index = reorder_nums.index((index, val))
            j = reorder_nums.pop(reorder_nums.index((index, val)))
            new_j_index = (j[1] + j_index) % (length - 1)
            reorder_nums.insert(new_j_index, (index, val))
    reorder_nums = [x[1] for x in reorder_nums]

    print(sum([reorder_nums[x] for x in [(y+reorder_nums.index(0)) % length for y in [1000, 2000, 3000]]]))


if __name__ == '__main__':
    main()