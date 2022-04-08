import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

x=0
for i in range(0, c):
    x+=d+i

if a-b-x<0:
    print(0)
else:
    print(a-b-x)
