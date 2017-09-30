## This file shows how to plot contour graphs in matplotlib

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# Generate meshgrid of x-y coordinates on the contour graph
delta = 0.025
x = np.arange(-2, 2, delta)
y = np.arange(-2, 2, delta)
X, Y = np.meshgrid(x, y)

# Get probablity in a bivariate normal distribution
xy = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)

plt.contour(X, Y, xy)
plt.show()
