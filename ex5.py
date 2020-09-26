import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
plt.figure(figsize=(20,10))
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
p_f = np.poly1d(p)
p_f(0.5)
p_f([1, 2, 3])
plt.grid()
plt.show()