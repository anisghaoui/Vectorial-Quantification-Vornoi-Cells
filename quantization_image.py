import numpy as np
import cv2

img = cv2.imread('input.jpg')
img_data = img.reshape((-1, 3)).astype('float32')

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

for K in range(2, 16, 2):
    ret, labels, centers = cv2.kmeans(
        img_data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    result = centers.astype('uint8')[labels.flatten()].reshape((img.shape))
    cv2.imshow(f'result - {K} centers', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
