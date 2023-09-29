inp = input()

for i in range(len(inp)):
    print(inp[i], end=": ")
    for j in range(int(inp[i])):
        print(inp[i], end="")
    print(end="\n")