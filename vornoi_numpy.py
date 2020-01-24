import numpy as np
import math
import random
import matplotlib.pyplot as plt

# for reproductibility
np.random.seed(15)

# dimensions
n_dim = 2
n_points = 500
n_centers = 4

# creating a few different distributions
data_1 = np.random.normal(loc=1, scale=0.5, size=(n_points // 2, n_dim))
data_2 = np.random.normal(loc=-1, scale=0.5, size=(n_points // 2, n_dim))

data = np.vstack([data_1, data_2])

centers = np.random.rand(n_centers, n_dim)

# compute quatratic distance from each point to each center, don't perform
# sqrt()
distances = np.array(
    [np.sum((data - np.full(data.shape, center))**2, axis=1) for center in centers])

# find the closest center towards every points
# this returns the indices of the smallest distances
indices = np.where(distances == np.amin(distances, axis=0))

clusters_belong = np.zeros(distances.shape, dtype=bool)
# the line index is the cluster index, the column index is the point index
clusters_belong[indices] = True
clusters = np.array([data[np.where(cluster)] for cluster in clusters_belong])

# compute centers


# plt.plot(data[:,0], data[:,1], '.')
COLORS = ['r', 'y', 'b', 'c', 'm', 'k'] * 4
for cluster, color in zip(clusters, COLORS):
    plt.plot(cluster[:, 0], cluster[:, 1], '*', color=color)
    plt.plot(cluster[:, 0], cluster[:, 1], '*', color=color)
plt.plot(centers[:, 0], centers[:, 1], 'xk')


plt.grid()
plt.show()
