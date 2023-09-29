inp = int(input())

for i in range(1, inp+1):
    if i % 2 == 1:
        space = int(((inp*2) - (i*2))/4)
        mid_space = int((inp-i)/2)
        print((" "*space+"*"*i+" "*mid_space)*2)
for j in range(inp-1, 0, -1):
    if j % 2 == 1:
        space = int(((inp*2) - (j*2))/4)
        mid_space = int((inp-j)/2)
        print((" "*space+"*"*j+" "*mid_space)*2)