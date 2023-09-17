inp = input()
index = inp.index(" ")
n = int(inp[:index])
m = int(inp[index:])

def gcd(a, b):
    while b:
        a, b = b, a % b
        # we can't seperate a and b assignment in different lines because new a and b is assigned after this line
        print(a, b)
        # this loop continues until b which is smaller number equals 0 then other number equals bmm 
    return a


bmm = gcd(n, m)
kmm = (n * m) // bmm

print(str(bmm) + " " + str(kmm))