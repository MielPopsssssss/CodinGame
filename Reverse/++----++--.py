import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
r=0
for i in s:
    if i=="+":r=r+1
    else:r=r-1
print(r)
