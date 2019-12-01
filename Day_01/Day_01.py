def get_input(filename):
    with open(filename, "r") as file:
        data = [int(x) for x in file]
    return data


def calculate_fuel(mass):
    return mass//3 - 2


if __name__ == "__main__":
    mass_measurements = get_input("input.txt")
    fuel_needs = [calculate_fuel(mass) for mass in mass_measurements]
    print("Total fuel required = {} units".format(sum(fuel_needs)))
