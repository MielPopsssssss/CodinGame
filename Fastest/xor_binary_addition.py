n_1, n_2 = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in range(len(n_1)):
    if n_1[i]=="1" and n_2[i]=="1":
        print("0",end='')
    else:
        print(int(n_1[i])+int(n_2[i]),end='')
