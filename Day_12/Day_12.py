from re import match
from itertools import combinations
from numpy import sign
from math import gcd
from copy import deepcopy


class Body:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    @property
    def energy(self):
        return self.potential_energy * self.kinetic_energy

    @property
    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, body):
        return (self.x == body.x
                and self.y == body.y
                and self.z == body.z
                and self.vx == body.vx
                and self.vy == body.vy
                and self.vz == body.vz)

    def __ne__(self, body):
        return not self.__eq__(body)


def read_file(filename="input.txt"):
    expression = "<x=(?P<x>-?\d+),\s*y=(?P<y>-?\d+),\s*z=(?P<z>-?\d+)>\s*"
    bodies = []
    with open(filename, "r") as input_file:
        for line in input_file:
            matchObj = match(expression, line)
            if not match:
                continue
            bodies.append(Body(
                    int(matchObj.group("x")),
                    int(matchObj.group("y")),
                    int(matchObj.group("z")))
            )
    return bodies


def apply_gravity(bodies):
    pairs_of_bodies = combinations(bodies, 2)
    for (body_a, body_b) in pairs_of_bodies:
        # apply x-component of gravity
        x_grav_on_a = sign(body_b.x-body_a.x)
        body_a.vx += x_grav_on_a
        body_b.vx -= x_grav_on_a

        # apply y-component of gravity
        y_grav_on_a = sign(body_b.y-body_a.y)
        body_a.vy += y_grav_on_a
        body_b.vy -= y_grav_on_a

        # apply z-component of gravity
        z_grav_on_a = sign(body_b.z-body_a.z)
        body_a.vz += z_grav_on_a
        body_b.vz -= z_grav_on_a


def time_step(bodies):
    apply_gravity(bodies)
    for body in bodies:
        body.apply_velocity()


def calculate_total_energy(bodies):
    total = 0
    for body in bodies:
        total += body.energy
    return total


def star_one(bodies):
    cloned_bodies = deepcopy(bodies)
    for i in range(1000):
        time_step(cloned_bodies)
    energy = calculate_total_energy(cloned_bodies)
    print("Star 1: {}".format(energy))


def lowest_common_multiple(numbers):
    lcm = numbers[0]
    for number in numbers[1:]:
        lcm = lcm * number // gcd(lcm, number)
    return lcm


def star_two(bodies):
    cloned_bodies = deepcopy(bodies)
    steps = 0
    x_steps = -1
    y_steps = -1
    z_steps = -1
    while True:
        time_step(cloned_bodies)
        steps += 1
        x_matches = True
        y_matches = True
        z_matches = True
        for i in range(len(bodies)):
            x_matches &= cloned_bodies[i].x == bodies[i].x
            x_matches &= cloned_bodies[i].vx == bodies[i].vx
            y_matches &= cloned_bodies[i].y == bodies[i].y
            y_matches &= cloned_bodies[i].vy == bodies[i].vy
            z_matches &= cloned_bodies[i].z == bodies[i].z
            z_matches &= cloned_bodies[i].vz == bodies[i].vz
        if x_matches and x_steps < 0:
            x_steps = steps
            print("x loops every {} steps".format(steps))
        if y_matches and y_steps < 0:
            y_steps = steps
            print("y loops every {} steps".format(steps))
        if z_matches and z_steps < 0:
            z_steps = steps
            print("z loops every {} steps".format(steps))
        if x_steps > 0 and y_steps > 0 and z_steps > 0:
            break
    cycle_length = lowest_common_multiple([x_steps, y_steps, z_steps])
    print("Star 2: {}".format(cycle_length))


if __name__ == "__main__":
    bodies = read_file()
    star_one(bodies)
    star_two(bodies)
