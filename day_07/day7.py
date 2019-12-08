stored_output = None


def run_program(program, pinput = None):
    program = program.split(',')
    intme = lambda x: int(x)
    program = list(map(intme, program))
    i = 0
    input_counter = 0
    while i < len(program):
        operation = str(program[i]).rjust(5, "0")
        opcode = operation[3:]
        paramode = {1: int(operation[2]), 2: int(operation[1]), 3: int(operation[0])}

        # Get values based on parameter mode
        if opcode in ["01", "02", "05", "06", "07", "08"]:
            if paramode[1]:
                val1 = program[i + 1]
            else:
                val1 = program[program[i + 1]]

            if paramode[2]:
                val2 = program[i + 2]
            else:
                val2 = program[program[i + 2]]
        elif opcode in ["04"]:
            if paramode[1]:
                addr = program[i + 1]
            else:
                addr = program[program[i + 1]]
        # Main computer operations
        if opcode == "01":
            # Addition
            save_in = program[i + 3]
            result = val1 + val2
            program[save_in] = val1 + val2
            i += 4
        elif opcode == "02":
            # Multiplication
            save_in = program[i + 3]
            result = val1 * val2
            program[save_in] = result
            i += 4
        elif opcode == "03":
            # Input Value
            save_in = program[i + 1]
            if not(pinput):
                value = int(input("Enter value: "))
            else:
                value = pinput[input_counter]
                input_counter += 1

            program[save_in] = value
            i += 2
        elif opcode == "04":
            # Print Output
            global stored_output
            stored_output = addr
            print(addr)
            i += 2
        elif opcode == "05":
            # Jump if true
            if val1 > 0:
                i = val2
            else:
                i += 3
        elif opcode == "06":
            # Jump if false
            if val1 == 0:
                i = val2
            else:
                i += 3
        elif opcode == "07":
            # Less than
            save_in = program[i + 3]
            if val1 < val2:
                program[save_in] = 1
            else:
                program[save_in] = 0
            i += 4
        elif opcode == "08":
            # Equals
            save_in = program[i + 3]
            if val1 == val2:
                program[save_in] = 1
            else:
                program[save_in] = 0
            i += 4
        else:
            break

def load_program():
    with open("day7_program.txt", 'r') as f:
        return f.read()

def generate_phases():
    good_phases = []
    dcounter = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        phase = (a, b, c, d, e)
                        for digit in range(5):
                            dcounter.append(phase.count(digit))
                        if max(dcounter) == 1:
                            good_phases.append(phase)
                        dcounter.clear()
    return good_phases

pcode = load_program()
phase2output = {}
thruster_output = []
phases = generate_phases()

for phase in phases:
    prog_input = (phase[0], 0)
    run_program(pcode, prog_input)
    for i in range(1, 5):
        prog_input = (phase[i], stored_output)
        run_program(pcode, prog_input)
    phase2output[phase] = stored_output
    thruster_output.append(stored_output)

print("Max Thruster Output:", max(thruster_output))
