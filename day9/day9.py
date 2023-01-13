def sup_norm(input_list):
    """This returns the conventional inf-norm used in analysis"""
    return max([abs(x) for x in input_list])


class RopeKnot:
    """This class represents each knot in the rope"""

    def __init__(self, tail=None):
        """Each knot, when initiated, sets its position to 0, 0 and gives itself a tail whom it commands"""
        self.position = [0, 0]
        if tail is None:
            print('oh shit')
        self.tail = tail
        self.trail = [tuple(self.position.copy())]

    def command(self, text_line):
        """Only the head of the rope will receive commands. When it does, it forces its tail to update its position."""
        direction, distance = text_line.strip(' \n').split(' ')
        index = 0 if direction == 'U' or direction == 'D' else 1
        for x in range(int(distance)):
            self.position[index] += 1 if direction == 'U' or direction == 'R' else -1
            self.tail.update_position(self.position)
            self.trail.append(tuple(self.position.copy()))

    def update_position(self, head_position=(0, 0)):
        """It updates its trail and its tail"""
        try:
            differential = (head_position[0] - self.position[0], head_position[1] - self.position[1])
            if sup_norm(differential) > 1:  # here we're checking if the head isn't adjacent to the tail
                if 0 in differential:
                    if differential[1] == 0:
                        self.position[0] += 1 if differential[0] > 0 else -1
                    else:
                        self.position[1] += 1 if differential[1] > 0 else -1
                else:
                    self.position[0] += 1 if differential[0] > 0 else -1
                    self.position[1] += 1 if differential[1] > 0 else -1
            if self.tail is not None:
                self.tail.update_position(self.position.copy())
            self.trail.append(tuple(self.position.copy()))
        except AttributeError:
            pass


def main():
    final_tail = RopeKnot
    rope = [final_tail]
    for x in range(10):
        rope.append(RopeKnot(rope[-1]))

    input_lines = open('day9input.txt').readlines()

    for line in input_lines:
        rope[-1].command(line)

    print(f'Part 1 solution: {len(set(rope[-2].trail))}')
    print(f'Part 2 solution: {len(set(rope[1].trail))}')


if __name__ == '__main__':
    main()
