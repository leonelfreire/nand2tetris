# Common stuff.

PREFIX_A     = '@'
PREFIX_LABEL = '('

MAX_A_BITS = 15
MAX_A_VALUE = (2 ** MAX_A_BITS) - 1

def toInt(value):
    try:
        return int(value)
    except ValueError:
        return None

def toBin(value, size):
    return bin(value)[2:].rjust(size, '0')
