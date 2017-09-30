## This file shows how to plot multiple graphs in one step, i.e. subplot
import matplotlib.pyplot as plt

for i in range(1, 19):
    x = list(range(20))
    y = [i * (data ** 2) for data in x]
    plt.subplot(6, 3, i)
    plt.plot(x, y)

plt.show()
    
