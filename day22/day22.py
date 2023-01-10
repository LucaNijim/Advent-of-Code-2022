import re
from math import sqrt
import numpy as np


def move_forward(position, direction, terrain, num):
    newpos = position
    for _ in range(num):
        potential_newpos = newpos + direction
        try:
            if terrain[potential_newpos[1]][potential_newpos[0]] == '.':
                pass
                print(terrain[potential_newpos[1]][potential_newpos[0]])
                newpos = potential_newpos
            elif terrain[potential_newpos[1]][potential_newpos[0]] == '#':
                print('#')
                break
        except IndexError:
            print('off the grid')
            pass

    return newpos




'''class Face:
    def __init__(self):
        # These names are left, up, right, down adjacent.
        self.ladj, self.uadj, self.radj, self.dadj = None
    
    


class Cube:
    def __init__(self, input_str):'''


def main():
    lrot = np.array([[0, -1], [1, 0]])
    rrot = -1*lrot

    with open('day22practiceinput.txt') as file:
        terrain = [x.strip('\n') for x in file.readlines()]
    directions = re.sub(r'[A-Z]', ' \g<0> ', terrain.pop(-1)).split()
    terrain.pop(-1)


    print(terrain)

    side_length = int(sqrt(sum(len(x.strip(' \n')) for x in terrain) / 6))

    pos = np.array([len(terrain[0]) - len(terrain[0].lstrip()), 0])
    d = np.array([1, 0])  # d is short for direction
    # We let the position equal a numpy

    while directions:
        nxt_dir = directions.pop(0)
        match nxt_dir:
            case 'L':
                d = np.matmul(lrot, d)
                print(d)
            case 'R':
                d = np.matmul(rrot, d)
                print(d)
            case _:
                pos = move_forward(pos, d, terrain, 10)


if __name__ == '__main__':
    main()
