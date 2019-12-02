def get_input(filename):
    with open(filename, "r") as file:
        data = [int(x) for x in file]
    return data


def calculate_fuel(mass):
    return mass//3 - 2


def calculate_fuel_recursive(mass):
    fuel = calculate_fuel(mass)
    if fuel < 0:
        return 0
    else:
        return fuel + calculate_fuel_recursive(fuel)


if __name__ == "__main__":
    masses = get_input("input.txt")

    fuel_needed = [calculate_fuel(mass) for mass in masses]
    print("Fuel needed = {} units".format(sum(fuel_needed)))

    fuel_needed_recursive = [calculate_fuel_recursive(mass) for mass in masses]
    print("Recursive fuel needed = {} units".format(sum(fuel_needed_recursive)))
