from itertools import permutations
from copy import deepcopy
import Intcode
PHASE_SETTINGS = range(5)
FEEDBACK_PHASE_SETTINGS = range(5, 10)


class Amplifier():
    def __init__(self, program, phase):
        self.program = program
        self.phase = phase
        self.phase_set = False

    def amplify(self, initial_val):
        output = []

        def mock_input(input_request):
            if not self.phase_set:
                self.phase_set = True
                return self.phase
            return initial_val

        Intcode.input = mock_input
        Intcode.print = lambda s: output.append(s)
        Intcode.process(program)
        return output[0]


def run_amplification_circuit(program, phase_data, initial_val=0):
    output = initial_val
    for phase in phase_data:
        amplifier = Amplifier(deepcopy(program), phase)
        output = amplifier.amplify(output)
    return output


def star_one(program):
    highest_signal = 0
    phase_combinations = permutations(PHASE_SETTINGS)
    for phase_setting in phase_combinations:
        signal = run_amplification_circuit(program, phase_setting)
        highest_signal = max(highest_signal, signal)
    return highest_signal


if __name__ == "__main__":
    program = Intcode.get_program_data("../input.txt")
    print("Star 1: {}".format(star_one(program)))
