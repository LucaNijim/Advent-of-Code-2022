import re

import numpy as np


def main():
    with open('day22input.txt') as file:
        board_string = list(x.rstrip('\n ') for x in file.readlines())
        instructions, _ = board_string.pop(-1), board_string.pop(-1)
        maxrowlen = max(len(y) for y in board_string)
        for index, x in enumerate(board_string):
            for _ in range(maxrowlen - len(x)): board_string[index] += ' '
        # It also uses a regex to split the instructions list around each letter
        instructions = re.sub(r'[A-Z]', ' \g<0> ', instructions).split()
    board_arr = np.zeros((len(board_string), maxrowlen))
    pos, inc = None, np.array([0, 1])
    for index, val in np.ndenumerate(board_arr):
        if (char := board_string[index[0]][index[1]]) != ' ':
            if pos is None:
                pos = np.array(index)
            board_arr[index] += 1
            if char == '#':
                board_arr[index] += 1
    print(board_arr)
    print(pos, inc)






if __name__ == '__main__':
    main()