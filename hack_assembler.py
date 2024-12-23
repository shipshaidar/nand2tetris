import parser
import code
import symbol_table

import argparse

parse = argparse.ArgumentParser()
parse.add_argument("filename")
argument = parse.parse_args()
filename = argument.filename

def translate_a(string):
    string = parser.symbol(string)
    if string.isdecimal():
        num = int(string)
        return f"{num:016b}"
    if string.isalnum() and not symbol_table.contains(string):
        symbol_table.add_entry(string)
    if string.isalnum() and symbol_table.contains(string):
        return f"{symbol_table.symbol_table[string]:016b}"
    

def translate_c(string):
    return "111" + code.comp(string) + code.dest(string) + code.jump(string)


def translate(string):
    string = parser.advance(string)
    if parser.instruction_type(string) == parser.A:
        return translate_a(string)
    else:
        return translate_c(string)


def first_pass():
    line_number = 0
    fin = open(filename, "rt")
    for string in fin:
        string = parser.advance(string)
        if string == str():
            continue
        if parser.instruction_type(string) == parser.L and not symbol_table.contains(string):
            symbol_table.symbol_table[parser.symbol(string)] = line_number
        else:
            line_number += 1
    fin.close()


def second_pass():
    fin = open(filename, "rt")
    fout = open(filename[:-4] + ".hack", "wt")
    for string in fin:
        if parser.advance(string) == str():
            continue
        if "(" in parser.advance(string):
            continue
        fout.write(translate(string) + "\n")
    fin.close()
    fout.close()


def assembler():
    first_pass()
    second_pass()

assembler()