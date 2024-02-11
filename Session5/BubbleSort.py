inp = input().split()

for i in range(len(inp)):
    for j in range(len(inp)):
        if inp[i] > inp[j]:
            inp[i], inp[j] = inp[j], inp[i]

print(inp)