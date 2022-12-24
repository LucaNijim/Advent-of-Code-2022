from itertools import cycle
import time
from math import floor


# This is a helper function for the default dict that I made. Its purpose is to assign 0s to empty space
# and 1s to the spaces outside the board game (walls, floor).

def default_dict_helper(key):
    if key[1] <= 0:
        return 1
    if key[0] <= 0 or key[0] >= 8:
        return 1
    return 0


# I didn't think that the build in default dict class had the functionality I needed, so I reworked it here so the
# helper function could take arguments instead of literally being a default value.
class LucaDefaultDict(dict):
    def __init__(self, func):
        self.func = func

    def __missing__(self, key):
        return self.func(key)


def timeit(func):
    def helper():
        start_time = time.time()
        func()
        print('Time elapsed: '+str(time.time()-start_time))
    return helper


def move_side(board: dict, coords: set, direction: str):
    increment = -1 if direction == '<' else 1
    potential_new_coords = {(x+increment, y) for x, y in coords}
    works = True
    for coord in potential_new_coords:
        if board[coord] > 0:
            works = False
    return potential_new_coords if works else coords


class TetrisBoard:
    def __init__(self, shapes_file):
        # First, we initialize a tuple of the types of blocks that will fall.
        self.blocks = []
        dummy_arr = []
        for line in open(shapes_file).readlines() + ['\n']:
            if line == '\n':
                self.blocks.append(tuple(dummy_arr))
                dummy_arr = []
            else:
                dummy_arr.append(tuple([0 if x == '.' else 1 for x in line.strip(' \n')]))
        self.blocks = tuple(self.blocks)

        self.game_board = LucaDefaultDict(default_dict_helper)
        self.height = [0]

    def play_tetris(self, inputs, count):
        # This function will simulate dropping in [count] blocks.
        wind_dir = cycle(enumerate(inputs))
        state_dict = dict()
        block = cycle(self.blocks)
        for i in range(count):
            # Here, we initialize the next block. We get its shape.
            block_num, shape = next(enumerate(block))
            block_coords = set()
            # We get the set of coordinates for the block.
            for col_index, col in enumerate(reversed(shape)):
                # We iterate through the rows of the shape, going from bottom up (that's why we reverse it)
                y_coord = 4 + col_index + self.height[i] # plus four because it's three up from the previous height
                for row_index, row in enumerate(col):
                    x_coord = 3 + row_index
                    if row > 0:
                        block_coords.add((x_coord, y_coord))  # Add an x-y pair to block coords


            while True:
                instruct_num, direction = next(wind_dir)
                block_coords = (move_side(self.game_board, block_coords, direction))
                pot_new_coords = {(x, y-1) for x, y in block_coords}
                if all({self.game_board[coord] == 0 for coord in pot_new_coords}):
                    block_coords = pot_new_coords
                else:
                    break
            for coord in block_coords:
                self.game_board[coord] = 1
            self.height.append(max({y for x, y in self.game_board.keys()}))


            # This is where we update the state space with block index, wind index, and last couple lines (10?)
            # its entry in the dict is its i value and its height
            # then if we find another with same state, we keep track of the difference in i values and height
            last_10_rows = []
            for y in range(self.height[i]-10, self.height[i]+1):
                for x in range(1, 8):
                    last_10_rows.append(self.game_board[(x, y)])

            if (instruct_num, block_num, tuple(last_10_rows)) in state_dict.keys():
                # This is what it does when it detects a cycle
                cycle_start = state_dict[(instruct_num, block_num, tuple(last_10_rows))][0]
                cycle_len = i-cycle_start
                cycle_height_inc = self.height[i]-state_dict[(instruct_num, block_num, tuple(last_10_rows))][1]
                return floor((count - cycle_start )/ cycle_len) * cycle_height_inc + self.height[(count-cycle_start)%cycle_len+cycle_start]
            else:
                state_dict[(instruct_num, block_num, tuple(last_10_rows))] = (i, self.height[i])
        return max(self.height)


@timeit
def main():
    our_board_pt1 = TetrisBoard('day17blockshapes.txt')
    print('Part 1 solution: ' + str(our_board_pt1.play_tetris(open('day17input.txt').read(), 2022)))
    our_board_pt2 = TetrisBoard('day17blockshapes.txt')
    print('Part 2 solution: ' + str(our_board_pt2.play_tetris(open('day17input.txt').read(), 1000000000000)))

    # 13345
    # 19819641
    # 50455

if __name__ == '__main__':
    main()