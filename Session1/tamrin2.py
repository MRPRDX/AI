inp = input()
index = 0
for t in inp:
    if inp[index] == " ":
        inp1 = int(inp[:index])
        inp2 = int(inp[index:])
    index += 1
bmm = []
b = 1
if inp1>inp2:
    big = int(inp1)
    small = int(inp2)
else:
    big = inp2
    small = inp1
for r in range(int(big/2)):
    if int(inp1/(r+1)) == inp1/(r+1) and int(inp2/(r+1)) == inp2/(r+1):
        bmm.append(r+1)

if int(big/small) == big/small:
    kmm = big
else:
    kmm = max(bmm) * big 
print(str(max(bmm))+" "+str(kmm))