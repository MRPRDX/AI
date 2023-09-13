inp = int(input())

x = 1
t = 0
division = []
while True:
    i = inp/x
    if x > inp / 2:
        break
    if int(i)*x == inp:
        division.append(x)
    x += 1
for j in range(len(division)):
    t += division[j]
if t == inp or inp == 1:
    print("YES")
else:
    print("NO")


