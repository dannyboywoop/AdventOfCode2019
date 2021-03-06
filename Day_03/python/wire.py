from line import Line
from point import Point
from math_utils import is_point_on_line


class Wire:
    def __init__(self, instructions, start_point=Point(0, 0)):
        self.instructions = instructions
        self.lines = []
        self._get_all_lines(start_point)

    def _get_all_lines(self, start_point):
        current_point = start_point
        for instruction in self.instructions:
            next_point = current_point.follow_instruction(instruction)
            self.lines.append(Line(current_point, next_point))
            current_point = next_point

    def number_of_steps(self, point):
        steps = 0
        for line in self.lines:
            if is_point_on_line(point, line):
                return steps+point.manhattan_distance(line.start)
            steps += line.length()
        return None
