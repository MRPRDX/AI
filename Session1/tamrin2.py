inp = input()
index = inp.index(" ")
n = int(inp[:index])
m = int(inp[index:])
bmm = 0
b = 1
r = n
while True:
    if int(n/(r)) == n/(r) and int(m/(r)) == m/(r):
        bmm = r
        break
    r -= 1
i = n/bmm
kmm = (m/bmm) * n
print(str(bmm)+" "+str(int(kmm)))