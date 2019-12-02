memory_orig = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 1, 9, 19, 23, 2, 13, 23, 27, 2, 27, 13, 31, 2,
          31, 10, 35, 1, 6, 35, 39, 1, 5, 39, 43, 1, 10, 43, 47, 1, 5, 47, 51, 1, 13, 51, 55, 2, 55, 9, 59, 1, 6, 59,
          63, 1, 13, 63, 67, 1, 6, 67, 71, 1, 71, 10, 75, 2, 13, 75, 79, 1, 5, 79, 83, 2, 83, 6, 87, 1, 6, 87, 91, 1,
          91, 13, 95, 1, 95, 13, 99, 2, 99, 13, 103, 1, 103, 5, 107, 2, 107, 10, 111, 1, 5, 111, 115, 1, 2, 115, 119, 1,
          119, 6, 0, 99, 2, 0, 14, 0]

memory = memory_orig[:]

memory[1] = 12
memory[2] = 2

def run_progrom():
    for i in range(0, len(memory), 4):
        operation = memory[i]

        if operation == 1:
            # Addition
            val1 = memory[memory[i + 1]]
            val2 = memory[memory[i + 2]]
            save_in = memory[i + 3]
            result = val1 + val2
            memory[save_in] = val1 + val2
        elif operation == 2:
            # Multiplication
            val1 = memory[memory[i + 1]]
            val2 = memory[memory[i + 2]]
            save_in = memory[i + 3]
            result = val1 * val2
            memory[save_in] = result
        else:
            break


noun = 0
verb = 0
for x in range(0, 100):
    for y in range(0, 100):
        memory = memory_orig[:]
        memory[1] = x
        memory[2] = y
        run_progrom()

        if memory[0] == 19690720:
            noun = x
            verb = y
            break

print(100 * noun + verb)
