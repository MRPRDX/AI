inp1 = input()
inp2 = input()

if inp1[::-1] > inp2[::-1]:
    print(inp2 + " < " + inp1)
elif inp1[::-1] < inp2[::-1]:
    print(inp1 + " < " + inp2)
elif inp1[::-1] == inp2[::-1]:
    print(inp1 + " = " + inp2)
