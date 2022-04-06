import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
a=re.findall("0\d{9}",s)
for i in a:
    if len(set(i)) > 1:
        print(i)
        break
