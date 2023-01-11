from collections import deque


def bfs(board, start_pos, seek_pos):
    width = len(board[0]) - 2
    height = len(board) - 4  # We subtract because of padding

    bsl = [x[1:-1] for x in board[2:-2]]  # bsl is board slice
    goals = deque([seek_pos, start_pos, seek_pos])

    locs = {0: {start_pos}}
    t = 1
    while True:
        locs[t] = set()
        for px, py in ((x+dx, y+dy) for x, y in locs[t-1] for dx, dy in ((0, 0), (0, -1), (0, 1), (1, 0), (-1, 0))):
            if board[py][px] == '#':
                continue
            if (px, py) == (1, 1) or (px, py) == seek_pos:  # special case for start and end so don't need sim
                locs[t].add((px, py))
                continue
            if not any([bsl[py - 2][(px - 1 - t) % width] == '>',
                        bsl[py - 2][(px - 1 + t) % width] == '<',
                        bsl[(py - 2 - t) % height][px - 1] == 'v',
                        bsl[(py - 2 + t) % height][px - 1] == '^']):
                locs[t].add((px, py))

        if goals[0] in locs[t]:
            locs[t].clear()
            locs[t].add(goals[0])
            yield t
            goals.popleft()
            if not goals:
                break
        t += 1


def main():
    # Step one of the project:
    with open('day24input.txt') as file:
        our_board = [x.strip(' \n') for x in file.readlines()]
        our_board.insert(0, '#' * len(our_board[0]))
        our_board.append('#' * len(our_board[0]))

    part1_answer, _, part2_answer = bfs(our_board, (1, 1), (len(our_board[0]) - 2, len(our_board) - 2))
    print(f'Part 1 solution: {part1_answer}\nPart 2 solution: {part2_answer}')


if __name__ == '__main__':
    main()
