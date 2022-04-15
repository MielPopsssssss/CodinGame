n = int(input())
l=[]
for i in input().split():
    value = int(i)
    l.append(value)

for i in range(len(l)):
    if l.count(l[i])==1:
        print(l[i])
