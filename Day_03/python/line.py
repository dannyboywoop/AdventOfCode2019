class Line:
    def __init__(self, start, end):
        if start == end:
            raise Exception(
                    "Start and end of a line cannot be the same point!"
                    )
        self.start = start
        self.end = end

    def is_vertical(self):
        return self.end.y != self.start.y

    def is_horizontal(self):
        return not self.is_vertical()

    def parallel(line_a, line_b):
        both_vertical = line_a.is_vertical() and line_b.is_vertical()
        both_horizontal = line_a.is_horizontal() and line_b.is_horizontal()
        return both_vertical or both_horizontal

    def length(self):
        return self.start.manhattan_distance(self.end)
