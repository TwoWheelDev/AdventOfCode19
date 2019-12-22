from aoc.intcomp import IntComp

computer = IntComp('day19_input.txt')

affected_points = []

for y in range(50):
    for x in range(50):
        computer.run_program([x, y])

        if computer.get_output()[0]:
            affected_points.append((x, y))

        computer.reset()

print("Part 1:", len(affected_points))
