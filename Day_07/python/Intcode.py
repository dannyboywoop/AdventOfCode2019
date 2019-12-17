from copy import deepcopy


def get_program_data(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def pad_parameter_modes(param_modes, expected_length):
    param_modes += [0]*(expected_length-len(param_modes))


class Intcode_Computer:
    def __init__(self, program_data):
        self.program_data = deepcopy(program_data)
        self.index = 0

    def _get_operation(self):
        code = self.program_data[self.index]
        opcode = code % 100
        parameter_modes = [int(digit) for digit in str(code)[-3::-1]]
        return opcode, parameter_modes

    def _get_value(self, i, param_mode):
        if param_mode == 0:
            return self.program_data[self.program_data[i]]
        elif param_mode == 1:
            return self.program_data[i]
        else:
            raise Exception("Invalid parameter mode!")

    def _add(self, param_modes):
        pad_parameter_modes(param_modes, 3)
        value = (self._get_value(self.index+1, param_modes[0])
                 + self._get_value(self.index+2, param_modes[1]))
        self.program_data[self.program_data[self.index+3]] = value
        self.index += 4

    def _multiply(self, param_modes):
        pad_parameter_modes(param_modes, 3)
        value = (self._get_value(self.index+1, param_modes[0])
                 * self._get_value(self.index+2, param_modes[1]))
        self.program_data[self.program_data[self.index+3]] = value
        self.index += 4

    def _get_input(self, param_modes):
        pad_parameter_modes(param_modes, 1)
        value = int(input("Input integer:"))
        self.program_data[self.program_data[self.index+1]] = value
        self.index += 2

    def _output(self, param_modes):
        pad_parameter_modes(param_modes, 1)
        print(self._get_value(self.index+1, param_modes[0]))
        self.index += 2

    def _jump_if_true(self, param_modes):
        pad_parameter_modes(param_modes, 2)
        if self._get_value(self.index+1, param_modes[0]):
            self.index = self._get_value(self.index+2, param_modes[1])
        else:
            self.index += 3

    def _jump_if_false(self, param_modes):
        pad_parameter_modes(param_modes, 2)
        if not(self._get_value(self.index+1, param_modes[0])):
            self.index = self._get_value(self.index+2, param_modes[1])
        else:
            self.index += 3

    def _less_than(self, param_modes):
        pad_parameter_modes(param_modes, 3)
        value = int(self._get_value(self.index+1, param_modes[0])
                    < self._get_value(self.index+2, param_modes[1]))
        self.program_data[self.program_data[self.index+3]] = value
        self.index += 4

    def _equals(self, param_modes):
        pad_parameter_modes(param_modes, 3)
        value = int(self._get_value(self.index+1, param_modes[0])
                    == self._get_value(self.index+2, param_modes[1]))
        self.program_data[self.program_data[self.index+3]] = value
        self.index += 4

    def _halt(self, param_modes):
        self.index = -1

    _operations = {
            1: _add,
            2: _multiply,
            3: _get_input,
            4: _output,
            5: _jump_if_true,
            6: _jump_if_false,
            7: _less_than,
            8: _equals,
            99: _halt
    }

    def process_all(self):
        while 0 <= self.index < len(self.program_data):
            opcode, param_modes = self._get_operation()
            self._operations[opcode](self, param_modes)
        return self.program_data[0]
