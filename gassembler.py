import tokenizer as tok
import fileinput
import sys
import re

def parser(fn):



def binfile(fn):
    with open("out.bin", "wb") as bin_file:
        bin_file.close()

def writebin(fn, b):
    with open("out.bin", "wb") as bin_file:
        bin_file.write(bytearray(b))

binfile("out.bin")

parser(sys.argv[1])

def assemble():
    with open(sys.argv[1]) as fn:
        for line in fn:
            tk = Tokenizer(line)
            # label logic
            if tk.curTok() == ".":
                #logic
            
            # instructions logic
            if tk.curTok() == "LD" or "ld":
                #load logic
                tk.advance()
            if tk.curTok() == "ADD" or "add":
                tk.advance()

            #similar advances
