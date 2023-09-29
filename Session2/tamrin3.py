inp = int(input())

for i in range(1, (2*inp)+2, 2):
    space = " "*((2*inp+1-i)//2)
    print(space+"*"*i+space)
for j in range((2*inp)-1, 0, -2):
    space = " "*((2*inp+1-j)//2)
    print(space+"*"*j+space)