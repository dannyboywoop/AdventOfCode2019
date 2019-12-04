class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def up(point, distance):
        return Point(point.x, point.y+distance)

    def down(point, distance):
        return Point(point.x, point.y-distance)

    def right(point, distance):
        return Point(point.x+distance, point.y)

    def left(point, distance):
        return Point(point.x-distance, point.y)

    TRANSLATIONS = {
        'U': up,
        'D': down,
        'R': right,
        'L': left
    }

    def follow_instruction(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])
        return Point.TRANSLATIONS[direction](self, distance)

    def manhattan_distance(self, point=None):
        if not point:
            point = Point(0, 0)
        return abs(self.x-point.x) + abs(self.y-point.y)
