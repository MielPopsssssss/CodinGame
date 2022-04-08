import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n1 = input()
equation = input().replace("x",'*')
n2 = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
equation=n1+equation+n2
print(round(eval(equation)))
