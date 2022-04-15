import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
l=[]
for i in input().split():
    value = int(i)
    l.append(value)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
l.sort()
for x in range(len(l)):
    if x!=len(l)-1:
        print(l[x],end=" ")
    else:
        print(l[x])
