from itertools import permutations
from aoc.intcomp import IntComp


thruster_output = []
phases = permutations(range(5))


for phase in phases:
    prog_input = [[phase[0], 0]]
    for i in range(5):
        amp = IntComp("day7_program.txt")
        amp.run_program(prog_input[i])
        if i < 4:
            prog_input.append([phase[i+1], amp.get_output()[0]])
        else:
            thruster_output.append(amp.get_output()[0])

print("Max Thruster Output:", max(thruster_output))
