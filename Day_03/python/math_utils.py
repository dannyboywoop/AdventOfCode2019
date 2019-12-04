from point import Point


def is_between(value, boundaries):
    start, end = sorted(boundaries)
    return start <= value <= end


def is_point_on_line(point, line):
    if line.is_vertical() and point.x == line.start.x:
        return is_between(point.y, (line.start.y, line.end.y))
    elif line.is_horizontal() and point.y == line.start.y:
        return is_between(point.x, (line.start.x, line.end.x))
    else:
        return False


def get_perp_intersection(vertical, horizontal):
    if (is_between(vertical.start.x,
                   (horizontal.start.x, horizontal.end.x))
            and is_between(horizontal.start.y,
                           (vertical.start.y, vertical.end.y))):
        return [Point(vertical.start.x, horizontal.start.y)]
    else:
        return []


def get_intersection(line_a, line_b):
    if line_a.is_vertical() and line_b.is_horizontal():
        return get_perp_intersection(line_a, line_b)
    elif line_a.is_horizontal() and line_b.is_vertical():
        return get_perp_intersection(line_b, line_a)
    return []
