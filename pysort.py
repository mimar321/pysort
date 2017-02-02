#!/usr/bin/python

import os
from PyQt5.QtCode import *

f_in  = open("temp.txt", "r")
f_out = open('out.txt', 'w')

lines = f_in.readlines()
#print lines
lines.sort(key=lambda a_line: a_line[0:20])
f_out.write(''.join(lines)) # Write a sequence of strings to a file

f_out.close()
f_in.close()
