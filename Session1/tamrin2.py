inp = input()
index = inp.index(" ")
n = int(inp[:index])
m = int(inp[index:])
# for t in inp:
#     if inp[index] == " ":
#         n = int(inp[:index])
#         m = int(inp[index:])
#     index += 1
bmm = []
b = 1
for r in range(int(n)):
    if int(n/(r+1)) == n/(r+1) and int(m/(r+1)) == m/(r+1):
        bmm.append(r+1)

if (n/max(bmm)) * (m/max(bmm)) < m or (n/max(bmm)) * (m/max(bmm)) == m:
    kmm = (n/max(bmm)) * (m/max(bmm)) * max(bmm)
else:
    kmm = (n/max(bmm)) * (m/max(bmm))
print(str(max(bmm))+" "+str(int(kmm)))