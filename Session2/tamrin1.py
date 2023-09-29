n = input()
r = 0
if len(str(n)) == 1:
    r = n
while len(str(n)) > 1:
    r = 0
    for i in range(len(n)):
        r += int(n[i])
    n = str(r)
print(r)
