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


def find_path_to(satellite, start="COM", ):
    if start == satellite:
        return [satellite]
    if start not in orbits:
        return []

    path = []
    for body in orbits[start]:
        path += find_path_to(satellite, body)

    if path:
        return [start] + path
    return []


def count_transfers(body_A, body_B):
    path_to_body_A = find_path_to(body_A)
    path_to_body_B = find_path_to(body_B)

    count = 0
    for body in reversed(path_to_body_A[:-1]):
        if body in path_to_body_B:
            break
        count += 1
    for body in reversed(path_to_body_B[:-1]):
        if body in path_to_body_A:
            break
        count += 1
    return count


if __name__ == "__main__":
    read_orbits()
    print("Star 1: {}".format(count_orbits()))
    print("Star 2: {}".format(count_transfers("YOU", "SAN")))
