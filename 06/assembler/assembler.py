# Main module.

import sys
import os
import re

import common
from parser import clean, parseLabel, parseInstruction, ParserException
from program import Program, ProgramException

def prepare():
    if sys.version_info[0] < 3:
        print('This program requires python 3.')
        sys.exit(1)

    if len(sys.argv) != 2:
        print('Usage: python assembler.py file.asm')
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print('File not found: %s' % sys.argv[1])
        sys.exit(1)

def build():
    inputFileName = sys.argv[1]
    inputFile = open(inputFileName, 'r', encoding='UTF-8')
    program = Program()

    for lineNumber, line in enumerate(inputFile, 1):
        line = clean(line)

        if line:
            try:
                if (line.startswith(common.PREFIX_LABEL)):
                    program.addLabel(parseLabel(line))
                else:
                    program.addInstruction(parseInstruction(line))
            except (ParserException, ProgramException) as e:
                print('Error on line: %s' % lineNumber)
                print('Content: %s' % line)
                print('Message: %s' % e)
                sys.exit(1)

    if re.search(r'\.asm$', inputFileName):
        outputFileName = re.sub(r'\.asm$', '.hack', inputFileName)
    else:
        outputFileName = inputFileName + '.hack'

    outputFile = open(outputFileName, 'w')
    outputFile.write(program.getBinary())
    outputFile.write('\n')

if __name__ == '__main__':
    prepare()
    build()
