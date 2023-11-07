import numpy as np
x = np.array([[1, 0, 2],[-1, -1, -1],[2, 4, -3]])
print(x)
reverse_x = np.linalg.inv(x)
print(reverse_x)
print(str(np.matmul(x, reverse_x)) + "\nsame as\n" + str(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])) + "\nalways stays at 0 and 1 even if we change numbers in first matris")