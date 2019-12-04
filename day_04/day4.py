input_lower = 206938
input_upper = 679128
valid_passes = []


def check_password(password):
    has_adjacent_digits = False
    has_trip = False
    does_not_decrement = True
    pairs = []

    for i in range(1, 6):
        if password[i] == password[i - 1]:
            has_adjacent_digits = True
            pairs.append(password[i])

        if int(password[i]) < int(password[i-1]):
            does_not_decrement = False

    for x in pairs:
        if pairs.count(x) == 1:
            has_trip = True

    if has_trip and has_adjacent_digits and does_not_decrement:
        return True
    else:
        return False


for code in range(input_lower, input_upper + 1):
    code = str(code)

    if check_password(code):
        valid_passes.append(code)

print(len(valid_passes))
