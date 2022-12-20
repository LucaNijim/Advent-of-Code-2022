class CathodeRayTube:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.signal = 0
        self.screen = []

    def noop(self):
        if self.cycle % 40 == 0:
            self.screen.append('')
        self.screen[-1] += '#' if self.x-1 <= self.cycle%40 <= self.x+1 else ' '
        self.cycle += 1
        self.signal += self.cycle * self.x if self.cycle % 40 == 20 else 0

    def addx(self, val):
        self.noop()
        self.noop()
        self.x += val

    def execute(self, file):
        file_unpack = open(file).readlines()
        for line in file_unpack:
            command = line.strip(' \n').split()
            if command[0] == 'noop':
                self.noop()
            elif command[0] == 'addx':
                self.addx(int(command[1]))


def main():
    crt = CathodeRayTube()
    crt.execute('day10input.txt')
    print(crt.signal)
    screen_string = ''
    for line in crt.screen:
        screen_string += line
        screen_string += '\n'
    print(screen_string)


if __name__ == '__main__':
    main()