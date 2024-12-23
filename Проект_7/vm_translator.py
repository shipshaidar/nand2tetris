import parser
import code_writer

import argparse

parse = argparse.ArgumentParser()
parse.add_argument("filename")
argument = parse.parse_args()
filename = argument.filename


def translate_push_asm(string):
    match parser.arg_1(string):
        case "constant":
            return code_writer.push_constant(parser.arg_2(string))
        case "local":
            return code_writer.push_local(parser.arg_2(string))
        case "static":
            return code_writer.push_static(filename[:-3], parser.arg_2(string))
        case "argument":
            return code_writer.push_argument(parser.arg_2(string))
        case "this":
            return code_writer.push_this(parser.arg_2(string))
        case "that":
            return code_writer.push_that(parser.arg_2(string))
        case "temp":
            return code_writer.push_temp(parser.arg_2(string))
        case "pointer":
            return code_writer.push_pointer(parser.arg_2(string))
        case _:
            print("Неизвестная команда push.")


def translate_pop_asm(string):
    match parser.arg_1(string):
        case "local":
            return code_writer.pop_local(parser.arg_2(string))
        case "static":
            return code_writer.pop_static(filename[:-3], parser.arg_2(string))
        case "argument":
            return code_writer.pop_argument(parser.arg_2(string))
        case "this":
            return code_writer.pop_this(parser.arg_2(string))
        case "that":
            return code_writer.pop_that(parser.arg_2(string))
        case "temp":
            return code_writer.pop_temp(parser.arg_2(string))
        case "pointer":
            return code_writer.pop_pointer(parser.arg_2(string))
        case _:
            print("Неизвестная команда pop.")


def translate_arithmetic_asm(string):
    match string:
        case "add":
            return code_writer.a_add()
        case "sub":
            return code_writer.a_sub()
        case "neg":
            return code_writer.a_neg()
        case "eq":
            return code_writer.a_eq()
        case "gt":
            return code_writer.a_gt()
        case "lt":
            return code_writer.a_lt()
        case "and":
            return code_writer.a_and()
        case "or":
            return code_writer.a_or()
        case "not":
            return code_writer.a_not()
        case _:
            print("Неизвестная команда arithmetic.")


def translate_asm(string):
    match parser.command_type(string):
        case parser.PUSH:
            return translate_push_asm(string)
        case parser.POP:
            return translate_pop_asm(string)
        case parser.ARITHMETIC:
            return translate_arithmetic_asm(string)
        case _:
            print("Неизвестная комманда translate_asm.")


def end():
    return "(END)\n@END\n0;JMP"


def vm_translate_asm():
    fin = open(filename, "rt")
    fout = open(filename[:-2] + "asm", "wt")

    for string in fin:
        if parser.clean(string) == str():
            continue
        if string.rstrip().startswith("/"):
            continue
        string = parser.clean(string)
        fout.write(f"//{string}\n")
        fout.write(translate_asm(string) + "\n\n")


    fout.write(end() + "\n")
    fin.close()
    fout.close()

vm_translate_asm()