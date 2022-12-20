import math


def bubble_sort(input_arr):
    for i in range(len(input_arr)):
        for j in range(0, len(input_arr)-i-1):
            if compare_lists(input_arr[j+1], input_arr[j]):
                input_arr[j], input_arr[j+1] = input_arr[j+1], input_arr[j]


def compare_lists(arr1, arr2):
    index_func = 0
    while True:
        if index_func == len(arr1) == len(arr2):
            return None
        try:
            arr1[index_func]
        except IndexError:
            return True
        try:
            arr2[index_func]
        except IndexError:
            return False
        if arr1[index_func] == arr2[index_func]:
            index_func += 1
            continue
        if isinstance(arr1[index_func], int) and isinstance(arr2[index_func], int):
            return arr2[index_func] > arr1[index_func]
        elif isinstance(arr1[index_func], int) and isinstance(arr2[index_func], list):
            return compare_lists([arr1[index_func]], arr2[index_func])
        elif isinstance(arr1[index_func], list) and isinstance(arr2[index_func], int):
            return compare_lists(arr1[index_func], [arr2[index_func]])
        else:
            return compare_lists(arr1[index_func], arr2[index_func])


def main():
    input_lines = [x.strip() for x in open('day13input.txt').readlines()]
    input_arr_pairs = [input_lines[3 * x:3 * x + 2] for x in range(math.ceil(len(input_lines) / 3))]
    sum_of_indexes = 0
    correct_order = []
    for pair in input_arr_pairs:
        correct_order.append(compare_lists(eval(pair[0]), eval(pair[1])))
    for index, val in enumerate(correct_order, 1):
        if val:
            sum_of_indexes += index
    print(sum_of_indexes)

    all_arrs = [[[2]], [[6]]]
    for pair in input_arr_pairs:
        for x in pair:
            all_arrs.append(eval(x))
    bubble_sort(all_arrs)
    decoder_key = 1
    for k, v in enumerate(all_arrs, 1):
        if v == [[2]] or v == [[6]]:
            decoder_key *= k

    print(decoder_key)


if __name__ == '__main__':
    main()