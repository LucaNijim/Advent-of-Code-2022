import numpy as np
from time import time
import re


def timeit(func):
    def helper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print(f'Time elapsed: {time() - start_time}')

    return helper


class Face:
    def __init__(self, str_arr):
        self.img = str_arr

    def __str__(self):
        return self.img


class FaceCollection:
    def __init__(self, faces_coords: dict):
        self.faces = faces_coords
        self.face_adjacencies = dict.fromkeys(faces_coords.keys())
        for facex, facey in self.faces:
            self.face_adjacencies[(facex, facey)] = {}
            incs = (np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1]))
            print(incs)
            for dx, dy in incs:
                if (px:=facex+dx, py:=facey+dy) in self.faces:
                    self.face_adjacencies


class Flat(FaceCollection): pass


class Cube(FaceCollection): pass


# Algorithm design for this project:
# Two parts
# For the first part, we create a smaller array of faces. Then we create a bijection between the coordinates
# The indexes on the thing
@timeit
def main():
    with open('day22input.txt') as file:
        # Inside this with statement, we unpack the file into a list of strings, each with max length
        # This list of strings represents the board
        board = list(x.rstrip('\n ') for x in file.readlines())
        instructions, _ = board.pop(-1), board.pop(-1)
        maxrowlen = max(len(y) for y in board)
        for index, x in enumerate(board):
            for _ in range(maxrowlen - len(x)): board[index] += ' '
        # It also uses a regex to split the instructions list around each letter
        instructions = re.sub(r'[A-Z]', ' \g<0> ', instructions).split()

    faces = {}
    start_pos = None

    side_length = int(np.sqrt(sum(len(row.strip()) for row in board) / 6))
    print(side_length)

    for y_index, col in enumerate(board[::side_length]):
        for x_index, row in enumerate(col[::side_length]):
            urcx, urcy = x_index * side_length, y_index * side_length
            if board[urcy][urcx] != ' ':
                if not start_pos:
                    start_pos = (urcx, urcy)
                faces[(x_index, y_index)] = [row[urcx:urcx + side_length] for row in board[urcy:urcy + side_length]]

    board_wrapped = Flat(faces)
    # print(board_wrapped.faces)
    print(start_pos)


if __name__ == '__main__':
    main()
