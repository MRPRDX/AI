inp1 = int(input())
inp2 = int(input())
r = 0
if inp1 == 1:
    inp1 = 2
for i in range(inp1, inp2+1):
    for j in range(2, i):
        if int(i/j) == i/j:
            break
        r = j
    if i == 2:
        print(2)
    if r == i-1:
        print(i)