class IntComp:
    def __init__(self, program):
        self._program = program
        self._params = []
        self._save = None
        self.memory = self._loadprogram()
        self._output = None

    def _loadprogram(self):
        with open(self._program, 'r') as f:
            return [int(x) for x in f.read().split(",")]

    def _get_parameters(self, opcode, paramode, pointer):
        self._params.clear()
        if opcode in ["01", "02", "05", "06", "07", "08"]:
            if paramode[1]:
                self._params.append(self.memory[pointer + 1])
            else:
                self._params.append(self.memory[self.memory[pointer + 1]])

            if paramode[2]:
                self._params.append(self.memory[pointer + 2])
            else:
                self._params.append(self.memory[self.memory[pointer + 2]])
        elif opcode in ["04"]:
            if paramode[1]:
                self._params.append(pointer + 1)
            else:
                self._params.append(self.memory[pointer + 1])

    def _get_save_addr(self, opcode, pointer):
        self._save = None
        if opcode in ["01", "02", "07", "08"]:
            self._save = self.memory[pointer + 3]
        elif opcode == "03":
            self._save = self.memory[pointer + 1]

    def get_output(self):
        return self._output

    def run_program(self, pinput=None):
        i = 0
        input_counter = 0
        while i < len(self.memory):
            operation = str(self.memory[i]).rjust(5, "0")
            opcode = operation[3:]
            paramode = {1: int(operation[2]), 2: int(operation[1]), 3: int(operation[0])}
            self._get_parameters(opcode, paramode, i)
            self._get_save_addr(opcode, i)

            if opcode == "01":
                # Addition
                self.memory[self._save] = sum(self._params)
                i += 4
            elif opcode == "02":
                # Multiplication
                self.memory[self._save] = self._params[0] * self._params[1]
                i += 4
            elif opcode == "03":
                # Input
                if not pinput:
                    value = int(input("Enter value: "))
                else:
                    value = pinput[input_counter]
                    input_counter += 1

                self.memory[self._save] = value
                i += 2
            elif opcode == "04":
                # Output
                self._output = self.memory[self._params[0]]
                i += 2
            elif opcode == "05":
                # Jump if true
                if self._params[0] > 0:
                    i = self._params[1]
                else:
                    i += 3
            elif opcode == "06":
                # Jump if false
                if self._params[0] == 0:
                    i = self._params[1]
                else:
                    i += 3
            elif opcode == "07":
                # Less than
                if self._params[0] < self._params[1]:
                    self.memory[self._save] = 1
                else:
                    self.memory[self._save] = 0
                i += 4
            elif opcode == "08":
                # Equals
                if self._params[0] == self._params[1]:
                    self.memory[self._save] = 1
                else:
                    self.memory[self._save] = 0
                i += 4
            else:
                # Opcode 99 - Halt
                break



