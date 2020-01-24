import cv2
import matplotlib.pyplot as plt
import numpy as np

N = 50

data = np.random.rand(N, 2).astype('float32')

# Define criteria = ( type, max_iter = 10 , epsilon = 1.0 )
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# Set flags
flags = cv2.KMEANS_RANDOM_CENTERS
attempts = 10
number_of_clusters = 2

# Apply KMeans
compactness, labels, centers = cv2.kmeans(
    data, number_of_clusters, None, criteria, attempts, flags)

# Now separate the data, Note the ravel()
A = data[labels.ravel() == 0]
B = data[labels.ravel() == 1]

# Plot the data
plt.scatter(A[:, 0], A[:, 1])
plt.scatter(B[:, 0], B[:, 1])
plt.scatter(centers[:, 0], centers[:, 1], s=80, c='y', marker='s')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()
