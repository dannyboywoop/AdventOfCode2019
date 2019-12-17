from itertools import permutations
import Intcode
PHASE_SETTINGS = range(5)


def amplify(program, phase, initial_val):
    output = []
    input_vals = [phase, initial_val]

    def mock_input(input_request):
        return input_vals.pop(0)

    Intcode.input = mock_input
    Intcode.print = lambda s: output.append(s)
    Intcode.process(program)
    return output


def run_amplification_circuit(program, phase_data, initial_val=0):
    output = initial_val
    for phase in phase_data:
        output = amplify(program, phase, output)[0]
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
