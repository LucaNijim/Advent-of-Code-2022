class Tail:
    def __init__(self, tail=False):
        self.position = [0, 0]
        self.trail = [(0, 0)]
        self.tail = tail


    def update_position(self, new_head_position):
        if abs(new_head_position[0]-self.position[0])+abs(new_head_position[1]-self.position[1]) > 2:
            if new_head_position[0]-self.position[0] == 2:
                self.position[0] += 1
                self.position[1] = new_head_position[1]
            elif new_head_position[0]-self.position[0] == -2:
                self.position[0] += -1
                self.position[1] = new_head_position[1]
            elif new_head_position[1]-self.position[1] == 2:
                self.position[1] += 1
                self.position[0] = new_head_position[0]
            else:
                self.position[1] += -1
                self.position[0] = new_head_position[0]
        else:
            for x in (0, 1):
                if abs(new_head_position[x] - self.position[x]) > 1:
                    if new_head_position[x] > self.position[x]:
                        self.position[x] += 1
                    else:
                        self.position[x] -= 1
        self.trail.append(tuple(self.position.copy()))
        if self.tail:
            self.tail.update_position(self.position)


class Head:
    def __init__(self, tail):
        self.position = [0, 0]
        self.tail = tail

    def command(self, textline):
        direction, count = textline.strip(' \n').split(' ')
        sign = -1 if direction == 'D' or direction == 'L' else 1
        index = 1 if direction == 'U' or direction == 'D' else 0
        for x in range(int(count)):
            self.position[index] += sign
            self.tail.update_position(self.position)


def main():
    text_input = open('day9input.txt').readlines()

    tail9 = Tail()
    tail8 = Tail(tail9)
    tail7 = Tail(tail8)
    tail6 = Tail(tail7)
    tail5 = Tail(tail6)
    tail4 = Tail(tail5)
    tail3 = Tail(tail4)
    tail2 = Tail(tail3)
    tail1 = Tail(tail2)
    head = Head(tail1)

    for line in text_input:
        head.command(line)

    print(len(set(tail9.trail)))


if __name__ == '__main__':
    main()