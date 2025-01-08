
ARITHMETIC = "C_ARITHMETIC"
PUSH = "C_PUSH"
POP = "C_POP"
LABEL = "C_LABEL"
GOTO = "C_GOTO"
IF = "C_IF"
FUNCTION = "C_FUNCTION"
RETURN = "C_RETURN"
CALL = "C_CALL"


def clean(instruction):
    new_instruction = str()
    for i in instruction:
        if i == "\n":
            continue
        new_instruction += i
    if "/" in new_instruction:
        return new_instruction[:new_instruction.find("/")].strip()
    return new_instruction.strip()



def command_type(instruction: str):
    if instruction.startswith("push"):
        return PUSH
    elif instruction.startswith("pop"):
        return POP
    elif instruction.startswith("label"):
        return LABEL
    elif instruction.startswith("goto"):
        return GOTO
    elif instruction.startswith("if"):
        return IF
    elif instruction.startswith("function"):
        return FUNCTION
    elif instruction.startswith("return"):
        return RETURN
    elif instruction.startswith("call"):
        return CALL
    for i in ("add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"):
        if instruction.startswith(i):
            return ARITHMETIC


def arg_1(instruction):
    if command_type(instruction) == ARITHMETIC:
        return instruction.strip()
    return instruction.split()[1]


def arg_2(instruction):
    print(instruction)
    if len(instruction.split()) < 3:
        return instruction.split()[1]
    return instruction.split()[-1]



