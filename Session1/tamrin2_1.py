inp = input()
index = inp.index(" ")
inp1 = int(inp[:index])
inp2 = int(inp[index:])
mm = inp1 * inp2

while inp2:
    remain = inp1 % inp2
    inp1 = inp2
    inp2 = remain
    bmm = inp1

print(str(bmm)+" "+str(int(mm/bmm)))