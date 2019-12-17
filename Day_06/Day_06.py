orbits = {}


def read_orbits(filename="input.txt"):
    with open(filename, "r") as input_file:
        for orbit in input_file:
            add_orbit(orbit)


def add_orbit(orbit):
    centre, satellite = orbit.rstrip().split(')')
    if centre not in orbits:
        orbits[centre] = [satellite]
    else:
        orbits[centre] += [satellite]


def count_orbits(centre="COM", depth=0):
    count = depth
    if centre not in orbits:
        return count

    satellites = orbits[centre]
    for satellite in satellites:
        count += count_orbits(satellite, depth+1)
    return count


if __name__ == "__main__":
    read_orbits()
    print("Star 1: {}".format(count_orbits()))
