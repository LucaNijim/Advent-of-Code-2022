from collections import defaultdict
import os


def printstuff(elfset):
    xcoords, ycoords = {x.real for x in elfset}, {x.imag for x in elfset}
    minx, miny, maxx, maxy = (int(val) for val in [min(xcoords), min(ycoords), max(xcoords), max(ycoords)])
    print(f'Min x: {minx}\nMin y: {miny}\nMax x: {maxx}\nMax y: {maxy}')


def update_locations(elfset, dirs):
    elves_target = {}
    counter = defaultdict(lambda: 0)
    for elf in elfset:
        neighbors = {elf+x+y*1j for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)} & elfset
        if neighbors:
            elves_target[elf] = elf
            for inc in dirs:
                dirneighbors = {elf + inc + x*inc*1j for x in range(-1, 2)}
                if not neighbors & dirneighbors:
                    elves_target[elf] = elf+inc
                    break
        else:
            elves_target[elf] = elf
        counter[elves_target[elf]] += 1
    for elf in elves_target:
        if counter[elves_target[elf]] > 1:
            elves_target[elf] = elf

    retset = set(elves_target.values())
    if len(retset) != len(elfset):
        raise TypeError('something bad happened')
    return retset


def store(elfset, framenum):
    if len(elfset) == 22:
        minx, miny, maxx, maxy = -3, -3, 10, 8
    else:
        minx, miny, maxx, maxy = -12, -51, 123, 83
    lines = ['' for _ in range(maxy-miny+1)]
    for ynum in range(miny, maxy+1):
        for xnum in range(minx, maxx+1):
            lines[ynum-miny] += '#' if xnum+ynum*1j in elfset else ' '
        lines[ynum-miny] += '\n'

    lines.reverse()
    with open(f'./animation_frames/{framenum}.txt', 'w') as file:
        file.writelines(lines)
    # for line in lines: print(line)


def score_positions(elves):
    xcoords, ycoords = [x.real for x in elves], [x.imag for x in elves]
    minx, miny, maxx, maxy = min(xcoords), min(ycoords), max(xcoords), max(ycoords)
    score = (maxx-minx+1)*(maxy-miny+1)-len(elves)
    return score


def main():
    for file in os.listdir('./animation_frames/'):
        os.remove(f'./animation_frames/{file}')
    direction_list = [0 + 1j, 0 - 1j, -1, 1]  # we're gonna iterate through like for i in range(4):  lasi

    elf_locations = set()
    with open('day23input.txt') as file:
        for ycoord, line in enumerate(file.readlines()[::-1]):
            for xcoord, char in enumerate(line):
                if char == '#':
                    elf_locations.add(xcoord + ycoord * 1j)
    pelf = set()
    counter = 0
    while pelf != elf_locations:
        store(elf_locations, counter)
        pelf = elf_locations
        elf_locations = update_locations(elf_locations, direction_list)
        direction_list.append(direction_list.pop(0))

        counter += 1
        if counter == 10:
            print(f'Part 1 solution: {score_positions(elf_locations)}')

    print(f'Part 2 solution: {counter}')
    # printstuff(elf_locations)


if __name__ == '__main__':
    main()