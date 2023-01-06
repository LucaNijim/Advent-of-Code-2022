def main():
    with open('day20practiceinput.txt') as file:
        list_of_numbers = [int(x.strip('\n ')) for x in file.readlines()]
    length = len(list_of_numbers)
    list_of_indexes = list(range(length))
    print(list_of_numbers)
    print(list_of_indexes, '\n'*2)

    # Let's write out what's happening here.



    # this wraps the list


if __name__ == '__main__':
    main()