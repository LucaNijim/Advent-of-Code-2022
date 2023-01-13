import numpy as np


class RockPaperScissorsMatch(str):
    """This is disgusting! Definitely shows how much I've grown over the last month!"""
    @property
    def score(self):
        p_1 = self[0]
        p_1_possibilities = ['A', 'B', 'C']

        for i in np.arange(len(self)):
            if self[-i] == ' ':
                continue
            p_2 = self[-i]
        p_2_possibilities = ['X', 'Y', 'Z']

        if p_1 == 'A':
            p_1 = 1
        if p_1 == 'B':
            p_1 = 2
        if p_1 == 'C':
            p_1 = 3

        # Second Round:
        if p_2 == 'X':
            p_2 = (p_1 - 1) % 3
            p_3 = 1
        if p_2 == 'Y':
            p_2 = p_1 % 3
            p_3 = 2
        if p_2 == 'Z':
            p_2 = (p_1 + 1) % 3
            p_3 = 3
        if p_2 == 0:
            p_2 = 3

        return p_3 + ((p_3 - p_1 + 1) % 3) * 3, p_2 + ((p_2 - p_1 + 1) % 3) * 3


def main():
    day2inputlines = open('day2input.txt').readlines()

    sum = 0
    for x in day2inputlines: sum += RockPaperScissorsMatch(x).score[0]
    print('Score for round 1: ' + str(sum))

    sum = 0
    for x in day2inputlines:
        sum += RockPaperScissorsMatch(x).score[1]
    print('Score for round 2: ' + str(sum))


if __name__ == '__main__':
    main()
