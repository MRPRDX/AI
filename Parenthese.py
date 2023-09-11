inp = input()

a = 0
b = 0
c = 0

for i in inp:
    if "}" in inp and "{" not in inp:
        print("No")
        break
    if "]" in inp and "[" not in inp:
        print("No")
        break
    if ")" in inp and "(" not in inp:
        print("No")
        break
    if "{" in inp:
        a += 1
    if "}" in inp:
        a -= 1
    if "[" in inp:
        b += 1
    if "]" in inp:
        b -= 1
    if "(" in inp:
        c += 1
    if ")" in inp:
        c -= 1

if a==b==c==0:
    print("Yes")
else:
    print("No")