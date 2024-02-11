inp = input().split()
int_list = []
for j in inp:
    int_list.append(int(j))
sorted_list = []
for i in range(len(int_list)):
    sorted_list.append(max(int_list))
    int_list.remove(max(int_list))

print(sorted_list)
