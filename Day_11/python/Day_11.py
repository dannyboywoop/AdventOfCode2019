import Intcode
from PIL import Image
RGB_COLOURS = {
        0: (0, 0, 0),
        1: (255, 255, 255)
        }


class Direction():
    def __init__(self, name, deltas):
        self.name = name
        self.delta_x = deltas[0]
        self.delta_y = deltas[1]


class Hull_Painting_Robot():
    directions = [
                Direction("up", (0, 1)),
                Direction("right", (1, 0)),
                Direction("down", (0, -1)),
                Direction("left", (-1, 0))
                ]

    colours = {
            "black": 0,
            "white": 1
            }

    def __init__(self, program, panels_painted):
        self.computer = Intcode.Intcode_Computer(program)
        self.x = 0
        self.y = 0
        self.direction_index = 0
        self.instruction_history = []
        self.panels_painted = panels_painted

    def _move(self, rotation_code):
        self.direction_index += rotation_code*2 - 1
        self.direction_index %= len(self.directions)
        self.x += self.directions[self.direction_index].delta_x
        self.y += self.directions[self.direction_index].delta_y

    def _paint_panel(self, colour_code):
        self.panels_painted[(self.x, self.y)] = int(colour_code)

    def _process_instruction(self, instruction):
        if len(self.instruction_history) % 2 == 0:
            self._paint_panel(instruction)
        else:
            self._move(instruction)
        self.instruction_history.append(instruction)

    def _get_current_panel_colour(self, request=None):
        if (self.x, self.y) in self.panels_painted:
            return self.panels_painted[(self.x, self.y)]
        return self.colours["black"]

    def paint_all(self):
        Intcode.input = self._get_current_panel_colour
        Intcode.print = lambda s: self._process_instruction(s)
        self.computer.process_all()
        return self.panels_painted


def star_one(program):
    panels_painted = {(0, 0): 0}
    robot = Hull_Painting_Robot(program, panels_painted)
    robot.paint_all()
    print("Star 1: {}".format(len(panels_painted)))


if __name__ == "__main__":
    program = Intcode.get_program_data("../input.txt")
    star_one(program)
