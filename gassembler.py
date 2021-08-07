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
            token = tok.tokenize(line)
            # label logic
            # comments logic
            # instructions logic
