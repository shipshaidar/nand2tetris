
EQ = 0
GT = 0
LT = 0
RETURN_COUNTER = 0

def a_add():
    return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D+M\n@SP\nAM=M+1\nA=A-1\nM=D"


def a_sub():
    return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@SP\nAM=M+1\nA=A-1\nM=D"


def a_neg():
    return "@SP\nM=M-1\nA=M\nD=-M\n@SP\nAM=M+1\nA=A-1\nM=D"



def a_eq(scope):
    global EQ
    c_eq = f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n\
@TRUE_EQ_{scope}.{str(EQ)}\nD;JEQ\n@FALSE_EQ_{scope}.{str(EQ)}\n0;JMP\n\
(TRUE_EQ_{scope}.{str(EQ)})\n@SP\nA=M\nM=-1\n@END_EQUAL_{scope}.{str(EQ)}\n0;JMP\n\
(FALSE_EQ_{scope}.{str(EQ)})\n@SP\nA=M\nM=0\n@END_EQUAL_{scope}.{str(EQ)}\n0;JMP\n\
(END_EQUAL_{scope}.{str(EQ)})\n@SP\nM=M+1"
    EQ += 1
    return c_eq


def a_gt(scope):
    global GT
    c_gt = f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n\
@TRUE_GT_{scope}.{str(GT)}\nD;JGT\n@FALSE_GT_{scope}.{str(GT)}\n0;JMP\n\
(TRUE_GT_{scope}.{str(GT)})\n@SP\nA=M\nM=-1\n@END_GT_{scope}.{str(GT)}\n0;JMP\n\
(FALSE_GT_{scope}.{str(GT)})\n@SP\nA=M\nM=0\n@END_GT_{scope}.{str(GT)}\n0;JMP\n\
(END_GT_{scope}.{str(GT)})\n@SP\nM=M+1"
    GT += 1
    return c_gt


def a_lt(scope):
    global LT
    c_lt = f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n\
@TRUE_LT_{scope}.{str(LT)}\nD;JLT\n@FALSE_LT_{scope}.{str(LT)}\n0;JMP\n\
(TRUE_LT_{scope}.{str(LT)})\n@SP\nA=M\nM=-1\n@END_LT_{scope}.{str(LT)}\n0;JMP\n\
(FALSE_LT_{scope}.{str(LT)})\n@SP\nA=M\nM=0\n@END_LT_{scope}.{str(LT)}\n0;JMP\n\
(END_LT_{scope}.{str(LT)})\n@SP\nM=M+1"
    LT += 1
    return c_lt


def a_and():
    return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D&M\n@SP\nAM=M+1\nA=A-1\nM=D"


def a_or():
    return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D|M\n@SP\nAM=M+1\nA=A-1\nM=D"


def a_not():
    return "@SP\nM=M-1\nA=M\nD=!M\n@SP\nAM=M+1\nA=A-1\nM=D"


def push_constant(i):
    return f"@{i}\nD=A\n@SP\nAM=M+1\nA=A-1\nM=D"


def push_static(filename, i):
    return f"@{filename}.{i}\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"


def pop_static(filename, i):
    return f"@SP\nM=M-1\nA=M\nD=M\n@{filename}.{i}\nM=D"


def push_local(i):
    return f"@LCL\nD=M\n@{i}\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"


def pop_local(i):
    return f"@SP\nM=M-1\nA=M\nD=M\n@LCL\nD=D+M\n@{i}\nD=D+A\n@SP\nA=M\nA=M\nA=D-A\nM=D-A"


def push_argument(i):
    return f"@ARG\nD=M\n@{i}\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"


def pop_argument(i):
    return f"@SP\nM=M-1\nA=M\nD=M\n@ARG\nD=D+M\n@{i}\nD=D+A\n@SP\nA=M\nA=M\nA=D-A\nM=D-A"


def push_this(i):
    return f"@THIS\nD=M\n@{i}\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"


def pop_this(i):
    return f"@SP\nM=M-1\nA=M\nD=M\n@THIS\nD=D+M\n@{i}\nD=D+A\n@SP\nA=M\nA=M\nA=D-A\nM=D-A"


def push_that(i):
    return f"@THAT\nD=M\n@{i}\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"


def pop_that(i):
    return f"@SP\nM=M-1\nA=M\nD=M\n@THAT\nD=D+M\n@{i}\nD=D+A\n@SP\nA=M\nA=M\nA=D-A\nM=D-A"


def push_temp(i):
    return f"@5\nD=A\n@{i}\nA=D+A\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"


def pop_temp(i):
    return f"@SP\nM=M-1\nA=M\nD=M\n@5\nD=D+A\n@{i}\nD=D+A\n@SP\nA=M\nA=M\nA=D-A\nM=D-A"


def push_pointer(i):
    if i == str(0):
        return "@THIS\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"
    elif i == str(1):
        return "@THAT\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D"


def pop_pointer(i):
    if i == str(0):
        return "@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D"
    elif i == str(1):
        return "@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D"
    

def asm_label(scope: str, label: str):
    return f"({scope}.{label})"


def asm_goto(scope: str, label: str):
    return "\n".join([
        f"@{scope}.{label}",
        "0;JMP"
    ])


def asm_if_goto(scope: str, label: str):
    return "\n".join([
        "@SP",
        "AM=M-1",
        "D=M",
        f"@{scope}.{label}",
        "D;JNE"
    ])


def generate_return_address(caller: str) -> str:
    global RETURN_COUNTER
    addr = "\n".join([
        f"{caller}$ret_{RETURN_COUNTER}"
    ])
    RETURN_COUNTER += 1
    return addr


def asm_call(caller: str, callee: str, n_args: str) -> str:
    ret_addr = generate_return_address(caller)
    return "\n".join([
        f"@{ret_addr}",
        "D=A",
        "@SP",
        "AM=M+1",
        "A=A-1",
        "M=D",

        "@LCL",
        "D=M",
        "@SP",
        "AM=M+1",
        "A=A-1",
        "M=D",

        "@ARG",
        "D=M",
        "@SP",
        "AM=M+1",
        "A=A-1",
        "M=D",

        "@THIS",
        "D=M",
        "@SP",
        "AM=M+1",
        "A=A-1",
        "M=D",

        "@THAT",
        "D=M",
        "@SP",
        "AM=M+1",
        "A=A-1",
        "M=D",

        "@SP",
        "D=M",
        "@5",
        "D=D-A",
        f"@{n_args}",
        "D=D-A",
        "@ARG",
        "M=D",

        "@SP",
        "D=M",
        "@LCL",
        "M=D",

        f"@{caller}.{callee}",
        "0;JMP",

        f"({ret_addr})"])


def asm_function(fn: str, n_arg: str):
    locals = [f"({fn})"]
    for i in range(int(n_arg)):
        locals.extend([
            "@SP",
            "AM=M+1",
            "A=A-1",
            "M=0"
        ])
    return "\n".join(locals)


def asm_return():
    return "\n".join([
        "@LCL",
        "D=M",
        "@5",
        "D=D-A",
        "A=D",
        "D=M",
        "@R14",
        "M=D",

        "@SP",
        "AM=M-1",
        "D=M",
        "@ARG",
        "A=M",
        "M=D",

        "@ARG",
        "D=M",
        "@1",
        "D=D+A",
        "@SP",
        "M=D",

        "@LCL",
        "D=M",
        "D=D-1",
        "A=D",
        "D=M",
        "@THAT",
        "M=D",

        "@LCL",
        "D=M",
        "@2",
        "D=D-A",
        "A=D",
        "D=M",
        "@THIS",
        "M=D",

        "@LCL",
        "D=M",
        "@3",
        "D=D-A",
        "A=D",
        "D=M",
        "@ARG",
        "M=D",

        "@LCL",
        "D=M",
        "@4",
        "D=D-A",
        "A=D",
        "D=M",
        "@LCL",
        "M=D",

        "@R14",
        "A=M",
        "0;JMP"
    ])