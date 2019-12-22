from aoc.intcomp import IntComp

computer = IntComp('day17_input.txt')
computer.run_program()

output = computer.get_output()

view = [[]]

for x in output:
    c = chr(x)
    if c == "\n":
        view.append([])
    else:
        view[-1].append(c)

inters = 0
for y in range(1, len(view)-3):
    for x in range(len(view[y])-2):
        if view[y][x] != '.' \
                and view[y - 1][x] != '.' \
                and view[y + 1][x] != '.' \
                and view[y][x + 1] != '.' \
                and view[y][x - 1] != '.':
            inters += x * y

print('Part 1:', inters)

computer.reset()
computer.memory[0] = 2
routine = [ord(a) for a in "A,B,A,C,A,B,C,B,C,A\n"]
function_a = [ord(a) for a in "L,12,R,4,R,4,L,6\n"]
function_b = [ord(a) for a in "L,12,R,4,R,4,R,12\n"]
function_c = [ord(a) for a in "L,10,L,6,R,4\n"]

other = [ord(a) for a in "n\n"]
computer_input = [*routine, *function_a, *function_b, *function_c, *other]
computer.run_program(computer_input)
print("Part 2:", computer.get_output()[-1])
