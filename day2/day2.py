import numpy as np
class rockPaperScissorsMatch:
    def __init__(self, score):
        p_1=self[0]
        p_1_possibilities=['A', 'B', 'C']

        p_2=self[-1]
        p_2_possibilities=['X', 'Y', 'Z']

        def stringtonumber(p, possList:)
            for i in np.arange(len(possList)):
                if p==possList(i):
                    p=i

        p_1, p_2=stringtonumber(p_1, p_1_possibilities), stringtonumber(p_2, p_2_possibilities)
        if


day2inputlines=open('day2input.txt').readlines()
print(day2inputlines[0])