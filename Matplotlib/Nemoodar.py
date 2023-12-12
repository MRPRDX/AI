import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.01)
y = x ** 2 + 8
plt.figure(figsize=(10, 7))
plt.plot(x, y)
x = np.random.rand(1000)*4-2
plt.hist(x, alpha = 0.5, bins = 100)
# bins makes shows number of columns
x = np.random.randn(1000)*2
plt.hist(x,alpha = 0.5, bins = 100)

plt.show()