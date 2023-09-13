inp = input()
x = 0
for i in range(len(inp)):
    if inp[i] == inp[-i-1]:
        x += 1
    else:
        print("NO")
        break

if x!=0:
    print("YES")