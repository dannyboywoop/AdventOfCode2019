PUZZLE_INPUT = (172851, 675869)


def always_increasing(value):
    highest_digit = 0
    for digit in str(value):
        int_digit = int(digit)
        if int_digit < highest_digit:
            return False
        highest_digit = int_digit
    return True


def repeated_digit(value):
    previous_digit = ""
    for digit in str(value):
        if digit == previous_digit:
            return True
        previous_digit = digit
    return False


def double_digit(value):
    previous_digit = ""
    repetition_count = 0
    for digit in str(value):
        if digit == previous_digit:
            repetition_count += 1
        else:
            if repetition_count == 2:
                return True
            repetition_count = 1
        previous_digit = digit
    if repetition_count == 2:
        return True
    return False


def meets_star_one_criteria(value):
    return always_increasing(value) and repeated_digit(value)


def meets_star_two_criteria(value):
    return always_increasing(value) and double_digit(value)


def star_one_passwords():
    valid_passwords = []
    for potential_password in range(PUZZLE_INPUT[0], PUZZLE_INPUT[1]):
        if meets_star_one_criteria(potential_password):
            valid_passwords.append(potential_password)
    return valid_passwords


def star_two_passwords():
    valid_passwords = []
    for potential_password in range(PUZZLE_INPUT[0], PUZZLE_INPUT[1]):
        if meets_star_two_criteria(potential_password):
            valid_passwords.append(potential_password)
    return valid_passwords


if __name__ == "__main__":
    star_one = len(star_one_passwords())
    print("Star one: {}".format(star_one))

    star_two = len(star_two_passwords())
    print("Star two: {}".format(star_two))
