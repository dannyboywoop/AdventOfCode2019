import Intcode
import numpy as np
import cv2
RGB_COLOURS = {
        0: [0, 0, 0],
        1: [255, 255, 255],
        2: [0, 0, 255],
        3: [0, 255, 0],
        4: [255, 0, 0]
        }
ESC_KEY = 27
UP_KEY = 2490368
LEFT_KEY = 2424832
RIGHT_KEY = 2555904
JOYSTICK_OPTIONS = {
        UP_KEY: 0,
        LEFT_KEY: -1,
        RIGHT_KEY: 1
        }


class Screen:
    CELL_CONTENT = {
            "empty": 0,
            "wall": 1,
            "block": 2,
            "paddle": 3,
            "ball": 4
            }

    def __init__(self):
        self.current_score = 0
        self.pixels = {}

    def process_pixel_data(self, data):
        for i in range(0, len(data), 3):
            x_pos = int(data[i])
            y_pos = int(data[i+1])
            if (x_pos, y_pos) == (-1, 0):
                self.current_score = int(data[i+2])
            else:
                self.pixels[(x_pos, y_pos)] = int(data[i+2])
        self._get_bounds()

    def _get_bounds(self):
        self.x_max = float("-inf")
        self.y_max = float("-inf")
        for x_pos, y_pos in self.pixels.keys():
            self.x_max = max(self.x_max, x_pos)
            self.y_max = max(self.y_max, y_pos)
        self.x_max = int(self.x_max + 1)
        self.y_max = int(self.y_max + 1)

    def display(self, scale=30):
        size = (self.x_max*scale, self.y_max*scale)
        pixels = np.zeros((self.y_max, self.x_max, 3))
        for (x, y), colour in self.pixels.items():
            pixels[y, x, :] = RGB_COLOURS[colour]
        img = cv2.resize(pixels, dsize=size, interpolation=cv2.INTER_NEAREST)
        print("\rCurrent Score: {}".format(self.current_score), end='')
        cv2.imshow("Screen", img)

    def count_blocks(self):
        count = 0
        for pixel_value in self.pixels.values():
            if pixel_value == self.CELL_CONTENT["block"]:
                count += 1
        return count

    def get_ball_pos(self):
        for pos, val in self.pixels.items():
            if val == self.CELL_CONTENT["ball"]:
                return pos

    def get_paddle_pos(self):
        for pos, val in self.pixels.items():
            if val == self.CELL_CONTENT["paddle"]:
                return pos


class Game_Controller:
    def __init__(self, game, cheat=False):
        self.game = game
        self.pixel_data = []
        self.screen = Screen()
        self.cheat = cheat

    def run_game(self):
        Intcode.print = lambda s: self.pixel_data.append(s)
        Intcode.input = self._get_move
        self.game.process_all()
        self.screen.process_pixel_data(self.pixel_data)

    def _get_move(self, request=None):
        self.screen.process_pixel_data(self.pixel_data)
        self.screen.display()
        if self.cheat:
            move = self._AI_move()
        else:
            move = self._joystick_output()
        self.pixel_data = []
        return move

    def _AI_move(self):
        cv2.waitKey(1)
        return int(np.sign(
                self.screen.get_ball_pos()[0]
                -self.screen.get_paddle_pos()[0]))

    def _joystick_output(self):
        key = -1
        while key not in JOYSTICK_OPTIONS:
            key = cv2.waitKey()
        return JOYSTICK_OPTIONS[key]


def star_one(program):
    computer = Intcode.Intcode_Computer(program)
    pixel_data = []
    Intcode.print = lambda s: pixel_data.append(s)
    computer.process_all()
    screen = Screen()
    screen.process_pixel_data(pixel_data)
    star_one = screen.count_blocks()
    print("Star 1: {}".format(star_one))


def star_two(program):
    computer = Intcode.Intcode_Computer(program)
    computer.program_data[0] = 2
    controller = Game_Controller(computer, True)
    controller.run_game()
    print("\rThe final score was {}".format(controller.screen.current_score))


if __name__ == "__main__":
    program = Intcode.get_program_data("../input.txt")
    star_one(program)
    star_two(program)
    cv2.destroyAllWindows()
