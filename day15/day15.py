from collections import defaultdict
import re


def taxicab_distance(list):
    return abs(list[2]-list[0]) + abs(list[3]-list[1])


class SensorField:
    def __init__(self, file):
        self.field = defaultdict(lambda: 0)
        self.beacon_locations = set()
        self.sensor_locations = set()
        self.sensors_distances = dict()

        self.min_x = float('inf')
        self.max_x = float('-inf')

        input_lines = open(file).readlines()

        for line in input_lines:
            line_numbers = [int(i.split('=')[1].strip('\n')) for i in re.split(',|:', line)]
            dist = taxicab_distance(line_numbers)
            self.beacon_locations.add((line_numbers[2], line_numbers[3]))
            self.sensor_locations.add((line_numbers[0], line_numbers[1]))
            self.sensors_distances.update({(line_numbers[0], line_numbers[1]): dist})
            if self.min_x > line_numbers[0] - dist:
                self.min_x = line_numbers[0] - dist
            if self.max_x < line_numbers[0] + dist:
                self.max_x = line_numbers[0] + dist

    def print_sum(self, line_num):
        our_sum = 0
        for x_coord in range(self.min_x, self.max_x + 1):
            ticker = False
            for sensor in self.sensor_locations:
                if taxicab_distance([x_coord, line_num] + list(sensor)) <= self.sensors_distances[sensor]:
                    ticker = True
            if ticker:
                our_sum += 1
        return our_sum - 1

    def find_mine(self):
        set_boundaries = {key: set() for key in self.sensor_locations}
        for key in self.sensor_locations:
            for x in range(key[0]-self.sensors_distances[key]-1, key[0]+self.sensors_distances[key]+2):
                ymod = self.sensors_distances[key]+1-abs(key[0]-x)
                y = (key[1] - ymod, key[1] + ymod)
                for yv in y:
                    set_boundaries[key].add((x, yv))
        boundary_overlap = set()
        for sensor in set_boundaries:
            for second_sensor in set_boundaries:
                boundary_overlap.update(set_boundaries[sensor].intersection(set_boundaries[second_sensor]))
        for item in boundary_overlap:
            bool_list = []
            for sensor in self.sensor_locations:
                if taxicab_distance([item[0], item[1], sensor[0], sensor[1]]) > self.sensors_distances[sensor] and \
                        0 <= item[0] <= 4000000 and 0 <= item[1] <= 4000000:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            if all(bool_list):
                return item[0]*4000000+item[1]


def main():
    our_field = SensorField('day15input.txt')
    print(our_field.print_sum(2000000))
    print(our_field.find_mine())


if __name__ == '__main__':
    main()