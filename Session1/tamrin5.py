a = int(input())
b = int(input())
t = b
if a%2 == 0:
    satr = 0
else:
    satr = 0
if a > b:
    for i in range(a):
        if (a-b)%2 == 1:
            print("Wrong difference!")
            break
        if satr == ((a-b)/2):
            while t > 0:
                satr += 1
                print((int((a-b)/2))*"* "+b*"  "+(int(((a-b)/2)-1))*"* "+"*")
                t -= 1
        else:
            if satr%2 == 1:
                if satr < a:
                    satr += 1
                    if satr == a:
                        print((a-1)*"* "+"*")
                    else:
                        print((a-1)*"* "+"*", end="\n")
            else:
                if satr < a:
                    satr += 1
                    if satr == a:
                        print((a-1)*"* "+"*")
                    else:
                        print((a-1)*"* "+"*", end="\n")
elif a == b or b > a or b >= 20:
    print("Wrong order!")
