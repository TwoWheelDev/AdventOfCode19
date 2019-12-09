from collections import defaultdict


class IntComp:
    def __init__(self, program, debug=False):
        self._program = program
        self._params = []
        self._save = None
        self.memory = defaultdict(int)
        self._output = None
        self._relative_base = 0
        self._debug = debug

        self._loadprogram()

    def _loadprogram(self):
        with open(self._program, 'r') as f:
            counter = 0
            for x in f.read().split(","):
                self.memory[counter] = int(x)
                counter += 1

    def _get_parameters(self, opcode, paramode, pointer):
        # Paramodes
        # 0 - Position Mode
        # 1 - Immediate Mode
        # 2 - Relative Mode
        self._params.clear()
        if opcode in ["01", "02", "05", "06", "07", "08"]:
            if paramode[0] == 1:
                self._params.append(self.memory[pointer + 1])
            elif paramode[0] == 2:
                addr = self.memory[pointer + 1] + self._relative_base
                self._params.append(self.memory[addr])
            else:
                self._params.append(self.memory[self.memory[pointer + 1]])

            if paramode[1] == 1:
                self._params.append(self.memory[pointer + 2])
            elif paramode[1] == 2:
                addr = self.memory[pointer + 2] + self._relative_base
                self._params.append(self.memory[addr])
            else:
                self._params.append(self.memory[self.memory[pointer + 2]])
        elif opcode in ["04", "09"]:
            if paramode[0] == 1:
                self._params.append(self.memory[pointer + 1])
            elif paramode[0] == 2:
                addr = self.memory[pointer + 1] + self._relative_base
                self._params.append(self.memory[addr])
            else:
                self._params.append(self.memory[self.memory[pointer + 1]])

    def _get_save_addr(self, opcode, paramode, pointer):
        self._save = None
        if opcode in ["01", "02", "07", "08"]:
            if paramode[2] == 1:
                self._save = pointer + 3
            elif paramode[2] == 2:
                self._save = self.memory[pointer + 3] + self._relative_base
            else:
                self._save = self.memory[pointer + 3]
        elif opcode == "03":
            if paramode[0] == 1:
                self._save = pointer + 1
            elif paramode[0] == 2:
                self._save = self.memory[pointer + 1] + self._relative_base
            else:
                self._save = self.memory[pointer + 1]

    def get_output(self):
        return self._output

    def run_program(self, pinput=None):
        i = 0
        totalTicks = 0

        while i < len(self.memory):
            totalTicks += 1
            operation = str(self.memory[i]).rjust(5, "0")
            opcode = operation[3:]
            paramode = (int(operation[2]), int(operation[1]), int(operation[0]))
            self._get_parameters(opcode, paramode, i)
            self._get_save_addr(opcode, paramode, i)

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
                    value = pinput[0]
                    pinput.remove(value)

                self.memory[self._save] = value
                i += 2
            elif opcode == "04":
                # Output
                self._output = self._params[0]
                if self._debug:
                    print("Debug: i=", i, "Output:", self._output)
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
            elif opcode == "09":
                # Edit Relative Base
                self._relative_base += self._params[0]
                i += 2
            else:
                # Opcode 99 - Halt
                break



