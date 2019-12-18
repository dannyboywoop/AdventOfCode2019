from copy import deepcopy
from progressbar import progressbar
from time import sleep


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y)

    def __sub__(self, point):
        return Point(self.x-point.x, self.y-point.y)

    def __eq__(self, point):
        return point and self.x == point.x and self.y == point.y

    def __ne__(self, point):
        return not self.__eq__(point)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def smallest_representation(self):
        for factor in reversed(range(2, max(abs(self.x), abs(self.y))+1)):
            if self.x % factor == self.y % factor == 0:
                return Point(self.x/factor, self.y/factor)
        return self


def get_map_data(filename="input.txt"):
    print("Reading map data...")
    with open(filename, "r") as input_file:
        data = [[point for point in line.rstrip()] for line in input_file]
    return data


def get_asteroid_positions(map_data):
    print("Getting asteroid positions...")
    asteroid_positions = set()
    y_max = len(map_data)
    x_max = len(map_data[0])
    for y in range(y_max):
        for x in range(x_max):
            if map_data[y][x] == "#":
                asteroid_positions.add(Point(x, y))
    return asteroid_positions, x_max, y_max


def get_obstructed_positions(start, obstruction, x_max, y_max):
    obstructed_positions = []
    diff = (obstruction - start).smallest_representation()
    test_point = obstruction + diff
    while 0 <= test_point.x < x_max and 0 <= test_point.y < y_max:
        obstructed_positions.append(test_point)
        test_point += diff
    return obstructed_positions


def remove_obstructed_asteroids(visible_asteroids, x_max, y_max):
    print("Removing obstructed asteroids...")
    sleep(0.5)
    for asteroid, still_visible in progressbar(visible_asteroids.items()):
        still_visible.remove(asteroid)
        others = deepcopy(still_visible)
        for other in others:
            if other not in still_visible:
                continue
            for obstructed in get_obstructed_positions(
                                                asteroid, other, x_max, y_max):
                if obstructed in still_visible:
                    still_visible.remove(obstructed)
                    visible_asteroids[obstructed].discard(asteroid)


def star_one(visible_asteroids):
    most_visible_asteroids = 0
    for visible in visible_asteroids.values():
        most_visible_asteroids = max(most_visible_asteroids, len(visible))
    print("Star 1: Max detectable asteroids = {} of {}".format(
                            most_visible_asteroids, len(visible_asteroids)))

if __name__ == "__main__":
    map_data = get_map_data()
    asteroid_positions, x_max, y_max = get_asteroid_positions(map_data)
    visible_asteroids = {asteroid: deepcopy(asteroid_positions)
                         for asteroid in asteroid_positions}
    remove_obstructed_asteroids(visible_asteroids, x_max, y_max)
    star_one(visible_asteroids)