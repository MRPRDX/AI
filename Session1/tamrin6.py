from math import factorial

n = int(input())

for i in range(n):
    for j in range(i+1):
        print(int(factorial(i) / (factorial(j) * factorial(i - j))), end=" ")
    print(end="\n")