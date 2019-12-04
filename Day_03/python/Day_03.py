from wire import Wire
from math_utils import get_intersection


def get_all_intersections(wire_a, wire_b):
        intersections = []
        for line_1 in wire_a.lines:
                for line_2 in wire_b.lines:
                        intersections += get_intersection(line_1, line_2)
        return intersections


def get_closest_intersect(intersections):
    closest_distance = float('inf')
    for intersection in intersections:
        distance = intersection.manhattan_distance()
        if 0 < distance < closest_distance:
            closest_distance = distance
    return closest_distance


def parse_file(filename):
    with open(filename, 'r') as input_file:
        wires = [Wire(line.split(',')) for line in input_file]
    return wires


if __name__ == "__main__":
    wires = parse_file("../input.txt")

    intersections = get_all_intersections(wires[0], wires[1])

    closest_distance = get_closest_intersect(intersections)
    print("Star_one: {}".format(closest_distance))
