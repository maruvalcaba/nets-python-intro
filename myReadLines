#! /usr/bin/env python3
#
# readlines.py.  Demo of buffered stdin semantics
#

from sys import stdin, stdout
from os import read, write

numLines = 0
ibuf = read(0, 100)
sbuf = ibuf.decode()
next = 0
limit = len(sbuf)

def myReadLines():
    x = getChar()
    line = ""
    while(x != '\n'):
        line += x
        x = getChar()
        if (x == ''):
            return ""
    line+='\n'
    return line

def getChar():
    global sbuf
    global next
    global limit
    global ibuf
    if (next==limit):
        next = 0
        ibuf = read(0,100)
        sbuf = ibuf.decode()
        limit = len(sbuf)
        if(limit == 0):
            return ''
    c = sbuf[next]
    next+=1
    return c

inLine = myReadLines()
print(f"Stdin uses file descriptor {stdin.fileno()}\n")
print(f"Stdout uses file descriptor {stdout.fileno()}\n")
while len(inLine):
    numLines += 1
    stdout.write(f"### Line {numLines}: <{str(inLine)}> ###\n")
    inLine = myReadLines()
stdout.write(f"EOF after {numLines} lines\n")
