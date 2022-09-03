import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m = int(input())
n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
r = (m+(n%7))
if r>7:
    r=r-7
print(r)
