"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        
        self.ram = [0] * 256
        self.PC = 0
        self.IR = None
        self.reg = [0] * 8
        self.reg[7] =  0xF4 
        self.FL = 0

    def load(self, programFile):
        """Load a program into memory."""
        print("loading:", programFile)
        address = 0
        try:
            with open(programFile) as f:
                for line in f:
                    num = line.split("#", 1)[0]

                    if num.strip() == '':
                        continue

                    self.ram[address] = int(num, 2)
                    address += 1
        except FileNotFoundError:
            print(f"ERROR: {programFile} not found")
            sys.exit(2)
        except IsADirectoryError:
            print(f"ERROR: {programFile} is a directory")
            sys.exit(3)


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "AND":
            self.reg[reg_a] = self.reg[reg_a] & self.reg[reg_b]
        elif op == "CMP":
            if self.reg[reg_a] == self.reg[reg_b]:
                self.FL = 0b00000001
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.FL = 0b00000100
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.FL = 0b00000010
        elif op == "MOD":
            if self.reg[reg_b] == 0:
                print("Divide by 0 ERROR")
                sys.exit(5)
            else:
                self.reg[reg_a] = self.reg[reg_a] % self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "NOT":
            self.reg[reg_a] = ~ self.reg[reg_a]
        elif op == "OR":
            self.reg[reg_a] = self.reg[reg_a] | self.reg[reg_b]
        elif op == "SHL":
            self.reg[reg_a] = self.reg[reg_a] << self.reg[reg_b]
        elif op == "SHR":
            self.reg[reg_a] = self.reg[reg_a] >> self.reg[reg_b]
        elif op == "XOR":
            self.reg[reg_a] = self.reg[reg_a] ^ self.reg[reg_b]   
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

    
    def ram_read(self, address):
        """ ram_read() should accept the address to read and return the value stored there. """
        return self.ram[address]
        
    def ram_write(self):
        """ raw_write() should accept a value to write, and the address to write it to."""
        pass