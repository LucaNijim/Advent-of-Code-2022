class ElfRanges(str):
    def contains_range(self):
        arr = self.replace('-', ',').replace('\n', '').split(',')
        for i in range(len(arr)):
            arr[i] = int(arr[i])

        if (arr[0] <= arr[2] and arr[1] >= arr[3]) or (arr[0] >= arr[2] and arr[1] <= arr[3]):
            return True
        else:
            return False

    def overlaps_range(self):
        arr = self.replace('-', ',').replace('\n', '').split(',')
        for i in range(len(arr)):
            arr[i] = int(arr[i])

        if arr[1] < arr[2] or arr[0] > arr[3]:
            return False
        else:
            return True


#    def isIncluded(self):
# we want each string to have class elf_ranges, which has the method is_included
# we want this method to return true if one range is in the other

def main():
    targetString = 'day4input.txt'
    input_lines = open(targetString).readlines()

    ElfRanges('1')

    # for day 1:
    sum_day1, sum_day2 = 0, 0
    for y in input_lines:
        if ElfRanges(y).contains_range():
            sum_day1 += 1
        if ElfRanges(y).overlaps_range():
            sum_day2 += 1
    print(f'Part 1 solution: {sum_day1}\nPart 2 solution: {sum_day2}')


if __name__ == '__main__':
    main()