import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
for i in s:
    if i.islower():
        print(i.upper(),end='')
    elif i.isupper():
        print(i.lower(),end="")
    else:
        print(i,end="")
        
