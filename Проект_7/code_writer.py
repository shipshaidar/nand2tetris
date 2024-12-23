
EQ = 0
GT = 0
LT = 0

def a_add():
    return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D+M\n@SP\nAM=M+1\nA=A-1\nM=D"


def a_sub():
    return "@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@SP\nAM=M+1\nA=A-1\nM=D"


def a_neg():
    return "@SP\nM=M-1\nA=M\nD=-M\n@SP\nAM=M+1\nA=A-1\nM=D"



def a_eq():
    global EQ
    c_eq = f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n\
@TRUE_EQ_{str(EQ)}\nD;JEQ\n@FALSE_EQ_{str(EQ)}\n0;JMP\n\
(TRUE_EQ_{str(EQ)})\n@SP\nA=M\nM=-1\n@END_EQUAL_{str(EQ)}\n0;JMP\n\
(FALSE_EQ_{str(EQ)})\n@SP\nA=M\nM=0\n@END_EQUAL_{str(EQ)}\n0;JMP\n\
(END_EQUAL_{str(EQ)})\n@SP\nM=M+1"
    EQ += 1
    return c_eq


def a_gt():
    global GT
    c_gt = f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n\
@TRUE_GT_{str(GT)}\nD;JGT\n@FALSE_GT_{str(GT)}\n0;JMP\n\
(TRUE_GT_{str(GT)})\n@SP\nA=M\nM=-1\n@END_GT_{str(GT)}\n0;JMP\n\
(FALSE_GT_{str(GT)})\n@SP\nA=M\nM=0\n@END_GT_{str(GT)}\n0;JMP\n\
(END_GT_{str(GT)})\n@SP\nM=M+1"
    GT += 1
    return c_gt


def a_lt():
    global LT
    c_lt = f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n\
@TRUE_LT_{str(LT)}\nD;JLT\n@FALSE_LT_{str(LT)}\n0;JMP\n\
(TRUE_LT_{str(LT)})\n@SP\nA=M\nM=-1\n@END_LT_{str(LT)}\n0;JMP\n\
(FALSE_LT_{str(LT)})\n@SP\nA=M\nM=0\n@END_LT_{str(LT)}\n0;JMP\n\
(END_LT_{str(LT)})\n@SP\nM=M+1"
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
    

def w_label(object, n):
    return f"({object}.{n})"


def w_goto():
    pass


def w_if_goto():
    pass