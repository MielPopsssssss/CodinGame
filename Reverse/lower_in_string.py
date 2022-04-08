import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
tot=0
for i in s:
    if i.islower():
        tot=tot+1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(tot)
