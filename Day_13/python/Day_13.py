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


class Screen:
    def __init__(self, pixel_data):
        self.process_pixel_data(pixel_data)

    def process_pixel_data(self, data):
        self.pixels = {}
        self.x_max = float("-inf")
        self.y_max = float("-inf")
        for i in range(0, len(data), 3):
            x_pos = int(data[i])
            y_pos = int(data[i+1])
            self.pixels[(x_pos, y_pos)] = int(data[i+2])
            self.x_max = max(self.x_max, x_pos)
            self.y_max = max(self.y_max, y_pos)
        self.x_max += 1
        self.y_max += 1

    def display(self):
        scale = 30
        size = (self.x_max*scale, self.y_max*scale)
        pixels = np.zeros((self.y_max, self.x_max, 3))
        for (x, y), colour in self.pixels.items():
            pixels[y, x, :] = RGB_COLOURS[colour]
        img = cv2.resize(pixels, dsize=size, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("Screen", img)


def star_one(program):
    computer = Intcode.Intcode_Computer(program)
    pixel_data = []
    Intcode.print = lambda s: pixel_data.append(s)
    computer.process_all()
    screen = Screen(pixel_data)
    star_one = 0
    for pixel_value in screen.pixels.values():
        if pixel_value == 2:
            star_one += 1
    print("Star 1: {}".format(star_one))


def star_two(program):
    program[0] = 2


if __name__ == "__main__":
    program = Intcode.get_program_data("../input.txt")
    star_one(program)
    cv2.destroyAllWindows()
