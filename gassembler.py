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
            tk = tok.Tokenizer(line)
            # comments 
            if tk.curTok() == "#":
                continue
            
            # label logici
            if tk.curTok() == ".":
                continue    

            # instructions logic
            if tk.curValue() == "LD" or "ld":
                r = int(tk.peekValue(1).upper()[1])
                tk.advance(2)
                if r>=0 and r<=7:
                    a1 = tk.curValue()
                    if a1 = "$": # address
                        addr = int(a1[1:], 0)
                        b = [0x02, r, addr >> 8, addr & 0xFF]
                        writebin("out.bin", b)
                    elif a1[0] == "R": # Register
                        r2 = int(a1[1:0], 0)
                        b = [0x01, r, 0, r2]
                        writebin("out.bin", b)
                    else: # Value
                        v = int(a1,0)
                        b = [0x00, r, v >> 8, v & 0xFF]
                        writebin("out.bin", b)
                else:
                    print("Invalid identities")
                    sys.exit()

            if tk.curValue() == "ST" or "st":
                
                r = int(tk.peekValue(1).upper()[1])
                tk.advance(2)
                if r>=0 and r<=7:
                    a1 = tk.curValue()
                    if a1 = "$": # address
                        addr = int(a1[1:], 0)
                        b = [0x10, r, addr >> 8, addr & 0xFF]
                        writebin("out.bin", b)
                    elif a1[0] == "R": # Register
                        r2 = int(a1[1:0], 0)
                        b = [0x13, r, 0, r2]
                        writebin("out.bin", b)
                    else: # Value
                        v = int(a1,0)
                        b = [0x14, r, v >> 8, v & 0xFF]
                        writebin("out.bin", b)
                else:
                    print("Invalid identities")
                    sys.exit()

            if tk.curValue() == "CMP" or "cmp":
                
                r = int(tk.peekValue(1).upper()[1])
                tk.advance(2)
                if r>=0 and r<=7:
                    a1 = tk.curValue()
                    if a1[0] == "R": # Register
                        r2 = int(a1[1:0], 0)
                        b = [0x20, r, 0, r2]
                        writebin("out.bin", b)
                    else: # Value
                        v = int(a1,0)
                        b = [0x21, r, v >> 8, v & 0xFF]
                        writebin("out.bin", b)
                else:
                    print("Invalid identities")
                    sys.exit()

            if tk.curTok() == "ADD" or "add":
                
                r = int(tk.peekValue(1).upper()[1])
                tk.advance(2)
                if r>=0 and r<=7:
                    a1 = tk.curValue()
                    if a1[0] == "R": # Register
                        r2 = int(a1[1:0], 0)
                        b = [0x42, r, 0, r2]
                        writebin("out.bin", b)
                    else: # Value
                        v = int(a1,0)
                        b = [0x40, r, v >> 8, v & 0xFF]
                        writebin("out.bin", b)
                else:
                    print("Invalid identities")
                    sys.exit()
