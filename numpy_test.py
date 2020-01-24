import numpy as np
import math
import random 
import matplotlib.pyplot as plt

#for reproductibility
np.random.seed(15)

#dimensions
n_dim= 2
n_points = 4
n_centers = 2

data = np.random.rand(n_points,n_dim)
centers = np.random.rand(n_centers,n_dim)

#compute quatratic distance from each point to each center, don't perform sqrt()
distances = np.array([np.sum((data - np.full(data.shape,center))**2, axis=1) for center in centers])

#find the closest center towards every points
indices = np.where(distances == np.amin(distances,axis=0)) # this returns the indices of the smallest distances

clusters_belong = np.zeros(distances.shape, dtype=bool)
clusters_belong[indices] = True # the line index is the cluster index, the column index is the point index

clusters = np.array([data[np.where(cluster)] for cluster in clusters_belong])
print()

plt.plot(data[:,0], data[:,1], '.b')
plt.plot(centers[:,0], centers[:,1], 'xk')
plt.plot(clusters[0][:,0], clusters[0][:,1], '*')
plt.plot(clusters[1][:,0], clusters[1][:,1], '*')

plt.grid()
plt.show()