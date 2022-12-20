from collections import defaultdict


class CaveSlice:
    def __init__(self, file):
        input_lines = open(file).readlines()
        points_with_rock = []
        for line in input_lines:
            points = [tuple([int(y) for y in x.strip(' \n').split(',')]) for x in line.split('->')]
            for index, point in enumerate(points):
                try:
                    if point[0] == points[index+1][0]:
                        if point[1] < points[index+1][1]:
                            for x in range(point[1], points[index+1][1]+1):
                                points_with_rock.append(tuple([point[0], x]))
                        else:
                            for x in range(points[index+1][1], point[1]+1):
                                points_with_rock.append(tuple([(point[0]), x]))
                    elif point[1] == points[index+1][1]:
                        if point[0] < points[index+1][0]:
                            for x in range(point[0], points[index+1][0]+1):
                                points_with_rock.append(tuple([x, point[1]]))
                        else:
                            for x in range(points[index+1][0], point[0]+1):
                                points_with_rock.append(tuple([x, point[1]]))
                except IndexError:
                    pass
        self.terrain = defaultdict(lambda: 0)
        for point in points_with_rock:
            self.terrain[point] = 1
        my_index = 0
        while True:
            y = SandGrain(self.terrain).sand_fall(False)
            if y[1] == float('inf'):
                break
            self.terrain[tuple(y)] = 2
            my_index += 1
        self.count_sand_grains = my_index

        self.terrain2 = defaultdict(lambda: 0)
        for point in points_with_rock:
            self.terrain2[point] = 1
        my_index2 = 0
        while my_index2 < 50000:
            k = SandGrain(self.terrain2).sand_fall(True)
            if k == [500, 0]:
                break
            self.terrain2[tuple(k)] = 2
            my_index2 += 1
        self.count_sand_grains2 = my_index2+1


class SandGrain:
    def __init__(self, terrain):
        self.position = [500, 0]
        self.terrain = terrain

    def sand_fall(self, part_2):
        highest_y_val = max([key[1] for key in self.terrain if self.terrain[key] == 1])
        while True:
            if part_2:
                if self.position[1] >= (highest_y_val + 1):
                    return self.position
            if self.terrain[(self.position[0], self.position[1]+1)] == 0:
                self.position[1] += 1
                if self.position[1] > highest_y_val and not part_2:
                    return tuple([self.position[0], float('inf')])
            elif self.terrain[(self.position[0]-1, self.position[1]+1)] == 0:
                self.position[1] += 1
                self.position[0] += -1
            elif self.terrain[(self.position[0]+1, self.position[1]+1)] == 0:
                self.position[1] += 1
                self.position[0] += 1
            else:
                return self.position


def main():
    our_slice = CaveSlice('day14input.txt')
    print(our_slice.count_sand_grains)
    print(our_slice.count_sand_grains2)


if __name__ == '__main__':
    main()