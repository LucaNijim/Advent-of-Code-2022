input_string: str = open('day6input.txt', 'r').readline()


def locate_packet(string, n):
    index = 0
    while index < len(input_string):
        potential_packet = set(x for x in string[index:index + n])
        if len(potential_packet) == n:
            break
        index += 1
    return index + n


def main():
    print(str(locate_packet(input_string, 4)) + '\n' + str(locate_packet(input_string, 14)))


if __name__ == '__main__':
    main()