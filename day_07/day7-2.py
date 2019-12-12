from itertools import permutations
from aoc.intcomp import IntComp


thruster_output = []
phases = permutations(range(5, 10))

amp = []
for x in range(5):
    amp.append(IntComp("day7_program.txt"))

for phase in phases:
    output = 0
    for i in range(5):
        amp[i].run_program([phase[i], output])
        output = amp[i].get_output()[0]
        amp[i].clear_output()

    while amp[4].state != 'HALT':
        for i in range(5):
            amp[i].run_program([output])
            output = amp[i].get_output()[0]
            amp[i].clear_output()
    thruster_output.append(output)
    for x in range(5):
        amp[x].reset()


print("Max Thruster Output:", max(thruster_output))
