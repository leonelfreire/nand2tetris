# Code parser.

import re
from common import PREFIX_A, PREFIX_LABEL, MAX_A_BITS, MAX_A_VALUE, toInt

_REGEX_CLEAN = re.compile(r'//.*|\s')
_REGEX_A     = re.compile(r'@([\w.@$]+)')
_REGEX_C     = re.compile(r'(?:([DAM]|MD|AM|AD|AMD)=)?(?:(-?[01]|[!-]?[DAM]|[DAM][+-]1|D[+-][AM]|[AM]-D|D[&|][AM]);?)(?:(JGT|JEQ|JGE|JLT|JNE|JLE|JMP)){0,1}')
_REGEX_LABEL = re.compile(r'\(([\w.@$]+)\)')

_MSG_INVALID_A       = 'Invalid A instruction.'
_MSG_INVALID_A_VALUE = 'Invalid A value. The value is restricted to %s bits (%s).' % (MAX_A_BITS, MAX_A_VALUE)
_MSG_INVALID_C       = 'Invalid C instruction.'
_MSG_INVALID_LABEL   = 'Invalid LABEL name.'

def clean(line):
    return _REGEX_CLEAN.sub('', line)

def parseInstruction(line):
    if line.startswith(PREFIX_A):
        return _parseA(line)
    else:
        return _parseC(line)

def parseLabel(line):
    match = _REGEX_LABEL.fullmatch(line)

    if match == None:
        raise ParserException(_MSG_INVALID_LABEL)

    return {
        'type': 'L',
        'value': match.group(1)
    }

def _parseA(line):
    match = _REGEX_A.fullmatch(line)

    if match == None:
        raise ParserException(_MSG_INVALID_A)

    value = toInt(match.group(1))
    if value != None and value > MAX_A_VALUE:
        raise ParserException(_MSG_INVALID_A_VALUE)

    return {
        'type': 'A',
        'value': match.group(1),
    }

def _parseC(line):
    match = _REGEX_C.fullmatch(line)

    if match == None:
        raise ParserException(_MSG_INVALID_C)

    return {
        'type': 'C',
        'dest': match.group(1),
        'comp': match.group(2),
        'jump': match.group(3),
    }

class ParserException(Exception):
    pass
