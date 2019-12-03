fh = open("day3_input.txt", 'r')
instruct = fh.readlines()

wire1_instructions = instruct[0].split(",")
wire2_instructions = instruct[1].split(",")

wires = {"wire1": set(),
         "wire2": set()}

wire_steps = {"wire1": {},
              "wire2": {}}


# Calculate wires
def calc_wire(wire_number, instructions):
    x, y = 0, 0
    wire_number = str(wire_number)
    step_counter = 0
    for instruction in instructions:
        direction = instruction[:1]
        distance = int(instruction[1:])

        if direction == "R":
            # Increment X
            for i in range(0, distance):
                x += 1
                step_counter += 1
                wires["wire" + wire_number].add((x, y))
                wire_steps["wire" + wire_number][(x, y)] = step_counter
        elif direction == "L":
            # Decrement X
            for i in range(0, distance):
                x -= 1
                step_counter += 1
                wires["wire" + wire_number].add((x, y))
                wire_steps["wire" + wire_number][(x, y)] = step_counter
        elif direction == "U":
            # Increment Y
            for i in range(0, distance):
                y += 1
                step_counter += 1
                wires["wire" + wire_number].add((x, y))
                wire_steps["wire" + wire_number][(x, y)] = step_counter
        elif direction == "D":
            # Decrement Y
            for i in range(0, distance):
                y -= 1
                step_counter += 1
                wires["wire" + wire_number].add((x, y))
                wire_steps["wire" + wire_number][(x, y)] = step_counter


calc_wire(1, wire1_instructions)
calc_wire(2, wire2_instructions)

match_intersection = wires["wire1"].intersection(wires["wire2"])
match_sums = []
match_steps = []
for intersection in match_intersection:
    ix = intersection[0]
    iy = intersection[1]
    if ix < 0:
        ix = abs(ix)
    if iy < 0:
        iy = abs(iy)

    match_sums.append(ix + iy)
    match_steps.append(wire_steps["wire1"][intersection] + wire_steps["wire2"][intersection])

match_sums = sorted(match_sums)
match_steps = sorted(match_steps)
print("Shortest distance = ", match_sums[0])
print("Lowest amount of steps = ", match_steps[0])
