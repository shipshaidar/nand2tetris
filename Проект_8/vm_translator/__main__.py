import parser
import code_writer

import argparse
import os

_parser = argparse.ArgumentParser()
_parser.add_argument("-t", nargs="+", dest="files")
files = vars(_parser.parse_args())["files"]


def translate_push_asm(filename, instruction):
    match parser.arg_1(instruction):
        case "constant":
            return code_writer.push_constant(parser.arg_2(instruction))
        case "local":
            return code_writer.push_local(parser.arg_2(instruction))
        case "static":
            return code_writer.push_static(filename, parser.arg_2(instruction))
        case "argument":
            return code_writer.push_argument(parser.arg_2(instruction))
        case "this":
            return code_writer.push_this(parser.arg_2(instruction))
        case "that":
            return code_writer.push_that(parser.arg_2(instruction))
        case "temp":
            return code_writer.push_temp(parser.arg_2(instruction))
        case "pointer":
            return code_writer.push_pointer(parser.arg_2(instruction))
        case _:
            raise ValueError("Неизвестная команда push.")


def translate_pop_asm(filename, instruction):
    match parser.arg_1(instruction):
        case "local":
            return code_writer.pop_local(parser.arg_2(instruction))
        case "static":
            return code_writer.pop_static(filename, parser.arg_2(instruction))
        case "argument":
            return code_writer.pop_argument(parser.arg_2(instruction))
        case "this":
            return code_writer.pop_this(parser.arg_2(instruction))
        case "that":
            return code_writer.pop_that(parser.arg_2(instruction))
        case "temp":
            return code_writer.pop_temp(parser.arg_2(instruction))
        case "pointer":
            return code_writer.pop_pointer(parser.arg_2(instruction))
        case _:
            raise ValueError("Неизвестная команда pop.")


def translate_arithmetic_asm(scope, instruction):
    match instruction:
        case "add":
            return code_writer.a_add()
        case "sub":
            return code_writer.a_sub()
        case "neg":
            return code_writer.a_neg()
        case "eq":
            return code_writer.a_eq(scope)
        case "gt":
            return code_writer.a_gt(scope)
        case "lt":
            return code_writer.a_lt(scope)
        case "and":
            return code_writer.a_and()
        case "or":
            return code_writer.a_or()
        case "not":
            return code_writer.a_not()
        case _:
            raise ValueError("Неизвестная команда arithmetic.")


def translate_label(scope: str, instruction: str):
    return code_writer.asm_label(scope, parser.arg_1(instruction))


def translate_goto(scope: str, instruction: str):
    return code_writer.asm_goto(scope, parser.arg_1(instruction))


def translate_if_goto(scope: str, instruction: str):
    return code_writer.asm_if_goto(scope, parser.arg_1(instruction))


def translate_call(scope: str, instruction: str):
    return code_writer.asm_call(
        scope,
        parser.arg_1(instruction),
        parser.arg_2(instruction)
        )


def translate_function(scope, instruction):
    return code_writer.asm_function(
        scope,
        parser.arg_2(instruction)
        )


def translate_return():
    return code_writer.asm_return()


def translate_asm(filename, scope, instruction):
    match parser.command_type(instruction):
        case parser.PUSH:
            return translate_push_asm(filename, instruction)
        case parser.POP:
            return translate_pop_asm(filename, instruction)
        case parser.ARITHMETIC:
            return translate_arithmetic_asm(scope, instruction)
        case parser.LABEL:
            return translate_label(scope, instruction)
        case parser.GOTO:
            return translate_goto(scope, instruction)
        case parser.IF:
            return translate_if_goto(scope, instruction)
        case parser.CALL:
            return translate_call(scope, instruction)
        case parser.FUNCTION:
            return translate_function(scope, instruction)
        case parser.RETURN:
            return translate_return()
        case _:
            raise ValueError("Неизвестная комманда translate_asm.")


def end():
    return "(END)\n@END\n0;JMP"


def start_programm():
    return "\n".join([
        "@256",
        "D=A",
        "@SP",
        "M=D",
        f"{translate_call("Sys", "call Sys.init 0")}"
    ])


fns = list([None])
def vm_translate_asm(filename):
    fin = open(filename, "rt")
    fout = open(filename[:-2] + "asm", "wt")
    for i in fin:
        instruction = parser.clean(i)
        if instruction == str():
            continue
        if instruction.startswith("/"):
            continue
        if parser.command_type(instruction) == parser.FUNCTION:
            fns.append(f"{filename[:-3]}.{parser.arg_1(instruction)}")
        if parser.command_type(instruction) == parser.CALL:
            scope = instruction.split()[1].split(".")[0]
        else:
            scope = fns[-1]
        fout.write(f"//{instruction}\n")
        fout.write(translate_asm(filename, scope, instruction) + "\n\n")
    fin.close()
    fout.close()
    return fout.name

translated = list()
def translate_vm_files():
    for file in files:
        translated.append(vm_translate_asm(file))
    unite_files()


def unite_files():
    with open("NestedCall.asm", "at+") as fout: # Вместо NestedCall.asm подставьте нужное вам название для выводного файла.
        fout.write(start_programm() + "\n\n")
        for i in translated:
            fout.write(f"//file: {i}\n")
            with open(i, "rt") as fin:
                for line in fin:
                    fout.write(line)
        fout.write(end() + "\n")
    for asm_file in translated:
        os.remove(asm_file)

translate_vm_files()
