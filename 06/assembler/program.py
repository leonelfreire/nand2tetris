# Represents the program being assembled.

from common import PREFIX_A, toInt, toBin

class Program:
    _MSG_UNKNOWN_INSTRUCTION = 'Unknown instruction: %s'

    # Destination codes.
    _C_DEST_TABLE = {
        None  : '000',
        'M'   : '001',
        'D'   : '010',
        'MD'  : '011',
        'A'   : '100',
        'AM'  : '101',
        'AD'  : '110',
        'AMD' : '111',
    }

    # Computation codes.
    _C_COMP_TABLE = {
        '0'   : '0101010',
        '1'   : '0111111',
        '-1'  : '0111010',
        'D'   : '0001100',
        'A'   : '0110000',
        '!D'  : '0001101',
        '!A'  : '0110001',
        '-D'  : '0001111',
        '-A'  : '0110011',
        'D+1' : '0011111',
        'A+1' : '0110111',
        'D-1' : '0001110',
        'A-1' : '0110010',
        'D+A' : '0000010',
        'D-A' : '0010011',
        'A-D' : '0000111',
        'D&A' : '0000000',
        'D|A' : '0010101',
        'M'   : '1110000',
        '!M'  : '1110001',
        '-M'  : '1110011',
        'M+1' : '1110111',
        'M-1' : '1110010',
        'D+M' : '1000010',
        'D-M' : '1010011',
        'M-D' : '1000111',
        'D&M' : '1000000',
        'D|M' : '1010101',
    }

    # Jump codes.
    _C_JUMP_TABLE = {
        None  : '000',
        'JGT' : '001',
        'JEQ' : '010',
        'JGE' : '011',
        'JLT' : '100',
        'JNE' : '101',
        'JLE' : '110',
        'JMP' : '111',
    }

    # Symbols.
    _SYMBOLS_TABLE = {
        'R0'     : 0,
        'R1'     : 1,
        'R2'     : 2,
        'R3'     : 3,
        'R4'     : 4,
        'R5'     : 5,
        'R6'     : 6,
        'R7'     : 7,
        'R8'     : 8,
        'R9'     : 9,
        'R10'    : 10,
        'R11'    : 11,
        'R12'    : 12,
        'R13'    : 13,
        'R14'    : 14,
        'R15'    : 15,
        'SCREEN' : 16384,
        'KBD'    : 24576,
        'SP'     : 0,
        'LCL'    : 1,
        'ARG'    : 2,
        'THIS'   : 3,
        'THAT'   : 4,
    }

    instructions = []
    unresolvedInstructions = []
    instructionCounter = 0 # Current instruction address.
    freeAddressCounter = 16 # Will be allocated for the next symbol.

    def addInstruction(self, instruction):
        if instruction['type'] == 'A':
            self._addA(instruction)
        elif instruction['type'] == 'C':
            self._addC(instruction)
        else:
            raise ProgramException(self._MSG_UNKNOWN_INSTRUCTION % instruction)

        self.instructionCounter += 1

    def addLabel(self, label):
        if label['value'] not in self._SYMBOLS_TABLE:
            # The label is relative to next instruction.
            self._SYMBOLS_TABLE[label['value']] = self.instructionCounter

    # Resolves all the pending symbols
    def resolve(self):
        for i in self.unresolvedInstructions:
            symbol = self.instructions[i][1:]

            if symbol not in self._SYMBOLS_TABLE:
                self._SYMBOLS_TABLE[symbol] = self.freeAddressCounter
                self.freeAddressCounter += 1

            self.instructions[i] = '0' + toBin(self._SYMBOLS_TABLE[symbol], 15)

        self.unresolvedInstructions = []

    def getBinary(self):
        self.resolve()

        return '\n'.join(self.instructions)

    def _addA(self, instruction):
        valueInt = toInt(instruction['value'])

        if valueInt != None:
            self.instructions.append('0' + toBin(valueInt, 15))
            return

        value = instruction['value']

        if value in self._SYMBOLS_TABLE:
            self.instructions.append('0' + toBin(self._SYMBOLS_TABLE[value], 15))
        else:
            # Signalizes as pending.
            self.instructions.append(PREFIX_A + value)

            # Resolves the address later.
            self.unresolvedInstructions.append(self.instructionCounter)

    def _addC(self, instruction):
        self.instructions.append(
            '111' +
            self._C_COMP_TABLE[instruction['comp']] +
            self._C_DEST_TABLE[instruction['dest']] +
            self._C_JUMP_TABLE[instruction['jump']]
        )

class ProgramException(Exception):
    pass
