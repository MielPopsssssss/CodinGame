import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
k=[]
for i in input().split():
    tower = k.append(int(i))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
max=0
s=0
for i in range(n):
    if k[i]>max:
        s=s+1
        max=k[i]

print(s)
