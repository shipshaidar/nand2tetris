
ARITHMETIC = "C_ARITHMETIC"
PUSH = "C_PUSH"
POP = "C_POP"
LABEL = "C_LABEL"
GOTO = "C_GOTO"
IF = "C_IF"
FUNCTION = "C_FUNCTION"
RETURN = "C_RETURN"
CALL = "C_CALL"


def clean(string):
    new_string = str()
    for i in string:
        if i == "\n":
            continue
        new_string += i
    if "/" in new_string:
        return new_string[:new_string.find("/")].strip()
    return new_string.strip()



def command_type(string):
    if "push" in string:
        return PUSH
    elif "pop" in string:
        return POP
    elif "label" in string:
        return LABEL
    elif "goto" in string:
        return GOTO
    elif "if" in string:
        return IF
    elif "function" in string:
        return FUNCTION
    elif "return" in string:
        return RETURN
    elif "call" in string:
        return CALL
    for i in ("add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"):
        if i in string:
            return ARITHMETIC


def arg_1(string):
    if command_type(string) is ARITHMETIC:
        return string.strip()
    return string.split()[1]


def arg_2(string):
    return string.split()[2]



