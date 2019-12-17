from itertools import permutations
import Intcode
PHASE_SETTINGS = range(5)
FEEDBACK_PHASE_SETTINGS = range(5, 10)


class Amplifier():
    def __init__(self, program, phase):
        self.computer = Intcode.Intcode_Computer(program)
        self.phase = phase
        self.phase_set = False
        self.output = []

    def amplify(self, initial_val):

        def mock_input(input_request):
            if not self.phase_set:
                self.phase_set = True
                return self.phase
            return initial_val

        Intcode.input = mock_input
        Intcode.print = lambda s: self.output.append(s)
        self.computer.process_until_output()
        return self.output[-1]


def run_amplification_circuit(program, phase_data, initial_val=0):
    output = initial_val
    for phase in phase_data:
        amplifier = Amplifier(program, phase)
        output = amplifier.amplify(output)
    return output


def run_feedback_circuit(program, phase_data, initial_val=0):
    amplifiers = [Amplifier(program, phase) for phase in phase_data]
    output = initial_val
    while not amplifiers[-1].computer.halted:
        for amplifier in amplifiers:
            output = amplifier.amplify(output)
    return output


def star_one(program):
    highest_signal = 0
    phase_combinations = permutations(PHASE_SETTINGS)
    for phase_setting in phase_combinations:
        signal = run_amplification_circuit(program, phase_setting)
        highest_signal = max(highest_signal, signal)
    return highest_signal


def star_two(program):
    highest_signal = 0
    phase_combinations = permutations(FEEDBACK_PHASE_SETTINGS)
    for phase_setting in phase_combinations:
        signal = run_feedback_circuit(program, phase_setting)
        highest_signal = max(highest_signal, signal)
    return highest_signal


if __name__ == "__main__":
    program = Intcode.get_program_data("../input.txt")
    print("Star 1: {}".format(star_one(program)))
    print("Star 2: {}".format(star_two(program)))
