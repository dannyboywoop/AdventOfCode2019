"""
Completed Intcode Computer!
"""

def get_program_data(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def pad_parameter_modes(param_modes, expected_length):
    param_modes += [0]*(expected_length-len(param_modes))


class Intcode_Computer:
    def __init__(self, program_data):
        self.program_data = {i: program_data[i]
                             for i in range(len(program_data))}
        self.index = 0
        self.relative_base = 0

    def _get_operation(self):
        code = self.program_data[self.index]
        opcode = code % 100
        parameter_modes = [int(digit) for digit in str(code)[-3::-1]]
        return opcode, parameter_modes

    def _get_value(self, i, param_mode):
        if param_mode == 0:
            index_to_read = self.program_data[i]
        elif param_mode == 1:
            index_to_read = i
        elif param_mode == 2:
            index_to_read = self.relative_base+self.program_data[i]
        else:
            raise Exception("Invalid parameter read mode!")

        if index_to_read not in self.program_data:
            self.program_data[index_to_read] = 0

        return self.program_data[index_to_read]

    def _set_value(self, i, param_mode, value):
        if param_mode == 0:
            index_to_write = self.program_data[i]
        elif param_mode == 2:
            index_to_write = self.relative_base+self.program_data[i]
        else:
            raise Exception("Invalid parameter write mode!")

        self.program_data[index_to_write] = value

    def _add(self, param_modes):
        pad_parameter_modes(param_modes, 3)
        value = (self._get_value(self.index+1, param_modes[0])
                 + self._get_value(self.index+2, param_modes[1]))
        self._set_value(self.index+3, param_modes[2], value)
        self.index += 4

    def _multiply(self, param_modes):
        pad_parameter_modes(param_modes, 3)
        value = (self._get_value(self.index+1, param_modes[0])
                 * self._get_value(self.index+2, param_modes[1]))
        self._set_value(self.index+3, param_modes[2], value)
        self.index += 4

    def _get_input(self, param_modes):
        pad_parameter_modes(param_modes, 1)
        value = int(input("Input integer:"))
        self._set_value(self.index+1, param_modes[0], value)
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
        self._set_value(self.index+3, param_modes[2], value)
        self.index += 4

    def _equals(self, param_modes):
        pad_parameter_modes(param_modes, 3)
        value = int(self._get_value(self.index+1, param_modes[0])
                    == self._get_value(self.index+2, param_modes[1]))
        self._set_value(self.index+3, param_modes[2], value)
        self.index += 4

    def _adjust_relative_base(self, param_modes):
        pad_parameter_modes(param_modes, 1)
        self.relative_base += self._get_value(self.index+1, param_modes[0])
        self.index += 2

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
            9: _adjust_relative_base,
            99: _halt
    }

    def process_all(self):
        while not self.halted:
            opcode, param_modes = self._get_operation()
            self._operations[opcode](self, param_modes)

    def process_until_output(self):
        outputted = False
        while not self.halted and not outputted:
            opcode, param_modes = self._get_operation()
            self._operations[opcode](self, param_modes)
            if self._operations[opcode].__name__ == self._output.__name__:
                outputted = True

    @property
    def halted(self):
        return (self.index < 0 or self.index >= len(self.program_data))


if __name__ == "__main__":
    program = get_program_data()
    computer = Intcode_Computer(program)
    computer.process_all()
