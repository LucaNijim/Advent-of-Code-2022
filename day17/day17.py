def default_dict_helper(key):
    print('hi')
    print(key[1])
    if key[0] == 0:
        return 1
    if key[1] == 0 or key[1] == 8:
        return 1
    return 0


class LucaDefaultDict(dict):
    def __init__(self, func):
        self.func = func

    def __missing__(self, key):
        return self.func(key)


class TetrisBoard:
    def __init__(self, shapes_file):
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
        self.max_height = 0

    def play_tetris(self, inputs, count):
        def current_input(string):
            i=0
            while True:
                try:
                    yield string[i]
                    i += 1
                except IndexError:
                    i = 0
                    yield string[i]

        my_gen = current_input(inputs)
        for x in range(100000):
            print(next(my_gen))

        new_ele = TetrisElement(self, (4, 3), self.blocks[1])
        '''for i in range(count):
            next_block = self.blocks[i % len(self.blocks)]
            print(next_block)'''



class TetrisElement:
    def __init__(self, board, bottom_left_corner, shape):
        self.coords = set()
        for row_index, row in enumerate(reversed(shape)):
            row_coord = bottom_left_corner[0] + row_index
            for col_index, col in enumerate(row):
                col_coord = bottom_left_corner[1] + col_index
                if col > 0:
                    self.coords.add((row_coord, col_coord))



def main():
    our_board_pt1 = TetrisBoard('day17blockshapes.txt')
    our_board_pt1.play_tetris(open('day17practiceinput.txt').read(), 1)


if __name__ == '__main__':
    main()