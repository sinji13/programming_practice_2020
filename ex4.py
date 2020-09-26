import numpy as np
import matplotlib.pyplot as plt
y = input()

with plt.xkcd():
    plt.figure(figsize=(20,10))
    plt.plot([eval(y) for x in range(100)], lw =3, label ='func')
    plt.legend(prop = {'size': 16})
    plt.grid(True)
    plt.show()