def get_program_data(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def get_operation(code):
    opcode = code % 100
    parameter_modes = [int(digit) for digit in str(code)[-3::-1]]
    return opcode, parameter_modes


def pad_parameter_modes(param_modes, expected_length):
    param_modes += [0]*(expected_length-len(param_modes))


def get_value(data, index, param_mode):
    if param_mode == 0:
        return data[data[index]]
    elif param_mode == 1:
        return data[index]
    else:
        raise Exception("Invalid parameter mode!")


def add(data, i, param_modes):
    pad_parameter_modes(param_modes, 3)
    value = (get_value(data, i+1, param_modes[0])
             + get_value(data, i+2, param_modes[1]))
    data[data[i+3]] = value
    return i+4


def multiply(data, i, param_modes):
    pad_parameter_modes(param_modes, 3)
    value = (get_value(data, i+1, param_modes[0])
             * get_value(data, i+2, param_modes[1]))
    data[data[i+3]] = value
    return i+4


def get_input(data, i, param_modes):
    pad_parameter_modes(param_modes, 1)
    value = int(input("Input integer:"))
    data[data[i+1]] = value
    return i+2


def output(data, i, param_modes):
    pad_parameter_modes(param_modes, 1)
    print(get_value(data, i+1, param_modes[0]))
    return i+2


def halt(data, i, param_modes):
    return -1


operations = {
        1: add,
        2: multiply,
        3: get_input,
        4: output,
        99: halt
}


def process(data):
    index = 0
    while 0 <= index < len(data):
        opcode, param_modes = get_operation(data[index])
        index = operations[opcode](data, index, param_modes)
    return data[0]


if __name__ == "__main__":
    program_data = get_program_data()

    star_one = process(program_data)
