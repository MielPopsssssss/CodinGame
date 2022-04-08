x=[int(input())]
while x[-1]!=1:x.append((lambda n:n%2==0 and n/2 or 3*n+1)(x[-1]))
print(len(x)-1)
