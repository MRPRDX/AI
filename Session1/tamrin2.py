inp1 = int(input())
inp2 = int(input())

bmm = 0
kmm = 0
numbmm = 1
numkmm = 1
k = 0
if inp1 > inp2:
    b = inp1
else:
    b = inp2
while True:
    if numbmm > b/2:
        break
    else:
        if int(inp1/numbmm) == inp1/numbmm and int(inp2/numbmm) == inp2/numbmm:
            bmm += numbmm
    numbmm += 1
while True:
    var = inp2*inp1
    if int(var/numkmm) == var/numkmm:
        kmm += numkmm
    numkmm += 1
