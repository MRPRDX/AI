inp = input().split()

def merge_sort(n):
    if len(n) == 1:
        return inp
    if len(n) == 2:
        return max(inp), min(inp)
    list1 = inp[0:(len(inp)//2)]
    list2 = inp[(len(inp)//2):len(inp)]
    print(list1, list2)
    list3 = merge_sort(list1)
print(merge_sort(inp))
