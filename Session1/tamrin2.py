inp = input()
index = inp.index(" ")
n = int(inp[:index])
m = int(inp[index:])
bmm = []
b = 1

r = 0
while True:
    if int(n/(r+1)) == n/(r+1) and int(m/(r+1)) == m/(r+1):
        bmm.append(r+1)
    if r == int(n/2):
        break
    r += 1
i = n/max(bmm)
while True:
    if int((m*i)/n) == (m*i)/n:
        kmm = m*i
        break
    i -= 1
print(str(max(bmm))+" "+str(int(kmm)))