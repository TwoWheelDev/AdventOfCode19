wire1_instructions = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
wire2_instructions = "U62,R66,U55,R34,D71,R55,D58,R83"

wire1_instructions = wire1_instructions.split(",")
wire2_instructions = wire2_instructions.split(",")

wires = {"wire1": [],
         "wire2": []}


# Calculate wires
def calc_wire(wire_number, instructions):
    x, y = 0, 0
    wire_number = str(wire_number)
    for instruction in instructions:
        direction = instruction[:1]
        distance = int(instruction[1:])

        if direction == "R":
            # Increment X
            for i in range(0, distance):
                x += 1
                wires["wire" + wire_number].append((x, y))
        elif direction == "L":
            # Decrement X
            for i in range(0, distance):
                x -= 1
                wires["wire" + wire_number].append((x, y))
        elif direction == "U":
            # Increment Y
            for i in range(0, distance):
                y += 1
                wires["wire" + wire_number].append((x, y))
        elif direction == "D":
            # Decrement Y
            for i in range(0, distance):
                y -= 1
                wires["wire" + wire_number].append((x, y))


calc_wire(1, wire1_instructions)
calc_wire(2, wire2_instructions)
print("Wire 1 points:", len(wires["wire1"]))
print("Wire 2 points:", len(wires["wire2"]))
matches = []
match_sum = []
j = 0
for point in wires["wire1"]:
    if point in wires["wire2"]:
        print("Match found on point", j)
        matches.append(point)
        match_sum.append(sum(point))
    j += 1
match_sum = sorted(match_sum)
print("Shortest distance = ", match_sum[0])
