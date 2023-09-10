inp = input()
ans1 = 0
ans2 = 0

if "L" in inp:
        if len(inp) == 1:
            print(50)
        else:
            if inp[0] == "L":
                ans1 += 50
            else:
                ans2 += 50
if "X" in inp:
        if len(inp) == 1:
            print(10)
        else:
            if inp[0] == "X":
                ans1 += 10
            else:
                ans2 += 10
if "V" in inp:
        if len(inp) == 1:
            print(5)
        else:
            if inp[0] == "V":
                ans1 += 5
            else:
                ans2 += 5
if "I" in inp:
        if len(inp) == 1:
            print(50)
        else:
            if inp[0] == "I":
                ans1 += 1
            elif inp[1] == "I":
                ans2 += 1

if ans2>ans1:
    print(ans2-ans1)
elif ans1>ans2:
    print(ans1+ans2)