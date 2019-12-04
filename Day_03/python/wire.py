from line import Line
from point import Point


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
