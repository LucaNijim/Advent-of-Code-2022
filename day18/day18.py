from collections import deque


def connection_list(cube):
    key_x, key_y, key_z = cube
    vals_to_check = ((key_x + 1, key_y, key_z), (key_x - 1, key_y, key_z), (key_x, key_y + 1, key_z),
                     (key_x, key_y - 1, key_z), (key_x, key_y, key_z + 1), (key_x, key_y, key_z - 1))
    return vals_to_check


def cube_in_box(cube, box):
    return all({box[0][0] <= cube[0] <= box[1][0],
                box[0][1] <= cube[1] <= box[1][1],
                box[0][2] <= cube[2] <= box[1][2]})


class LavaBomb:
    def __init__(self, file):
        input_lines = open(file).readlines()
        self.coordinates = set()
        for line in input_lines:
            self.coordinates.add(tuple([int(x) for x in line.strip(' \n').split(',')]))

    def get_surface_area(self):
        surface_area = 0
        for key in self.coordinates:
            coord_increment = 0
            key_x, key_y, key_z = key[0], key[1], key[2]
            vals_to_check = ((key_x+1, key_y, key_z), (key_x-1, key_y, key_z), (key_x, key_y+1, key_z),
                             (key_x, key_y-1, key_z), (key_x, key_y, key_z+1), (key_x, key_y, key_z-1))
            for val in vals_to_check:
                if val not in self.coordinates:
                    coord_increment += 1
            surface_area += coord_increment
        return surface_area

    def get_diameter(self):
        x_coords = {x[0] for x in self.coordinates}
        y_coords = {x[1] for x in self.coordinates}
        z_coords = {x[2] for x in self.coordinates}
        return (min(x_coords), min(y_coords), min(z_coords)), \
               max(max(x_coords) - min(x_coords),
                   max(y_coords)-min(y_coords),
                   max(z_coords)-min(z_coords))

    def new_outside_area(self):
        box = ((-3, -3, -3), (26, 26, 26))
        start_node = (0, 0, 0)
        q = deque()
        q.append(start_node)
        visited_air = set()
        surface_area = 0

        while len(q) > 0:
            current_node = q.popleft()
            visited_air.add(current_node)

            for adjacent_node in connection_list(current_node):
                if cube_in_box(adjacent_node, box) and adjacent_node not in visited_air:
                    if adjacent_node in self.coordinates:
                        surface_area += 1
                    else:
                        visited_air.add(adjacent_node)
                        q.append(adjacent_node)
        return surface_area


def main():
    our_obsidian = LavaBomb('day18input.txt')
    print(our_obsidian.get_surface_area())
    print(our_obsidian.new_outside_area())


if __name__ == '__main__':
    main()