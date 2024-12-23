

symbol_table = \
{
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576
}
variable_cursor = 16

def add_entry(symbol):
    global variable_cursor
    symbol_table[symbol] = variable_cursor
    variable_cursor += 1


def contains(symbol):
    return symbol in symbol_table


def get_address(symbol):
    return symbol_table[symbol]