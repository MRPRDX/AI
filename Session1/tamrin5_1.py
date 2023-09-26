inp1 = int(input())
inp2 = int(input())

if (inp1 - inp2) % 2 == 1:
    print("wrong order!")
else:
    for i in range((inp1-inp2)//2):
        print("* "*(inp1-1)+"*")
    for p in range(inp2):
        print("* "*(((inp1-inp2)//2)-1)+"*"+" "*inp1+"* "*(((inp1-inp2)//2)-1)+"*")
    for j in range((inp1-inp2)//2):
        print("* "*(inp1-1)+"*")