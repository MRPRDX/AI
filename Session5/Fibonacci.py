inp = int(input())

lis = [1, 2]
indexes = []
i = 0
while lis[i] < inp:
    a = lis[i]
    b = lis[i+1]
    lis.append(a+b)
    i += 1

for j in range(len(lis)-1, -1, -1):
    if lis[j] <= inp:
        inp -= lis[j]
        indexes.append(j+1)

for t in indexes:
    print(t, end=" ")
