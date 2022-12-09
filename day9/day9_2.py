def supnorm(input_list):
    return max([abs(x) for x in input_list])


class RopeKnot:
    def __init__(self, tail=None):
        self.position = [0, 0]
        if tail == None:
            print('oh shit')
        self.tail = tail
        self.trail = [tuple(self.position.copy())]

    def command(self, textline):
        direction, distance = textline.strip(' \n').split(' ')
        index = 0 if direction == 'U' or direction == 'D' else 1
        for x in range(int(distance)):
            self.position[index] += 1 if direction == 'U' or direction == 'R' else -1
            self.tail.update_position(self.position)
            self.trail.append(tuple(self.position.copy()))

    def update_position(self, head_position=[0, 0]):
        try:
            differential = (head_position[0] - self.position[0], head_position[1] - self.position[1])
            if supnorm(differential) > 1:  # here we're checking if the head isn't adjacent to the tail
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
        except:
            pass


finalTail = RopeKnot
rope = [finalTail]
for x in range(10):
    rope.append(RopeKnot(rope[-1]))


input_lines = open('day9input.txt').readlines()


for line in input_lines:
    rope[-1].command(line)

print(len(set(rope[-2].trail)))
print(len(set(rope[1].trail)))