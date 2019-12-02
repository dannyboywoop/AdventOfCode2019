def get_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def add(data, i):
    value = data[data[i+1]] + data[data[i+2]]
    data[data[i+3]] = value
    return False


def multiply(data, i):
    value = data[data[i+1]] * data[data[i+2]]
    data[data[i+3]] = value
    return False


def halt(data, i):
    return True


operations = {
        1: add,
        2: multiply,
        99: halt
}


def process(data):
    i = 0
    should_halt = False
    while i < len(data) and not should_halt:
        opcode = data[i]
        should_halt = operations[opcode](data, i)
        i += 4
    return data[0]


def initialise(input_data, noun, verb):
    data = input_data.copy()
    data[1] = noun
    data[2] = verb
    return data


if __name__ == "__main__":
    program_data = get_input()

    star_one = process(initialise(program_data, 12, 2))
    print("Star_01 Answer: {}".format(star_one))
