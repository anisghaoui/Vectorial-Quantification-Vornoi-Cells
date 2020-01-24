import math
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import numpy as np
from tqdm import tqdm
from mpl_toolkits.mplot3d import Axes3D


# gif data
anim = []
TITLE = 'Vectorial quantising - Vornoi cells'
gif_fig = plt.figure(figsize=(10, 10))
# gif_ax = plt.subplot(111, projection="3d")
gif_clusters, gif_centers = [], []


def main():
    n_points = 10000
    n_dim = 2
    distribution_1 = np.random.normal(
        loc=1, scale=2, size=(n_points // 2, n_dim))
    distribution_2 = np.random.normal(
        loc=-2, scale=1, size=(n_points // 2, n_dim))
    points = np.vstack((distribution_1, distribution_2))
    clusters, centers, distorion, iters = LBG(
        points, max_cells=16, as_gif=True)  # set to True to produce a gif
    plt.show()


def cluster_forming(points: np.ndarray, centers: np.ndarray):
    """ returns (efficiently) clusters as a list of 2D arrays"""
    distances = np.array(
        [np.sum((points - np.full(points.shape, center))**2, axis=1) for center in centers])

    indices = np.where(distances == np.amin(distances, axis=0))
    clusters_belong = np.zeros(distances.shape, dtype=bool)
    clusters_belong[indices] = True
    clusters = np.array([points[np.where(cluster)]
                         for cluster in clusters_belong])
    return clusters


def LBG(points: np.ndarray, initial_cells: int = 2, eps: float = 0.005, max_cells: int = 8, as_gif=False):
    """ """
    assert points.shape[1] == 2 or points.shape[
        1] == 3, "wrong array shape, must be (*,2) or (*,3)"
    # initializing
    distortion = [9999999]
    iters = 0
    # pick unique centers
    centers = np.array(random.sample(list(points), initial_cells))
    clusters = np.empty((len(centers), points.shape[0], points.shape[1]))

    for i in tqdm(range(0, int(math.log(max_cells, 2)))):
        if len(points) < initial_cells:
            return clusters, centers, distortion, iters

        distorion_deviation = distortion[0]
        saved_centers = centers
        # choose random centers
        centers = np.array(random.sample(list(points), initial_cells))
        initial_cells *= 2

        while distorion_deviation >= eps:  # start Kmeans
            clusters = cluster_forming(points, centers)
            centers = np.array([np.average(cluster, axis=0)
                                for cluster in clusters])

            distances = np.hstack(np.array([np.array(list(map(lambda point:
                                                              (point[
                                                                  0] - center[0])**2 + (point[1] - center[1])**2,
                                                              cluster))) for cluster, center in zip(clusters, centers)]))

            distortion.append(np.sum(distances) / len(points))
            distorion_deviation = (
                distortion[iters] - distortion[iters + 1]) / distortion[iters + 1]
            iters += 1

            if as_gif:
                gif_clusters.append(clusters)
                gif_centers.append(centers)

        if not as_gif:
            plt.figure()
            for cluster in clusters:
                plt.plot(cluster[:, 0], cluster[:, 1], '.')
            plt.plot(centers[:, 0], centers[:, 1], 'sk')
            plt.title(TITLE)

    if as_gif:  # creating the gif
        global gif_fig
        global anim
    #	if is_3d:
    #		plt.subplot(111, projection='3d')
        anim = animation.FuncAnimation(
            gif_fig, animate, frames=iters, interval=300, repeat=True)
        # anim.save(TITLE + '.gif', fps=4, writer='ffmpeg')

    return clusters, centers, distortion, iters


def animate(nframe: int):
    plt.cla()
    for cluster in gif_clusters[nframe]:
        plt.plot(cluster[:, 0], cluster[:, 1], '.')
    plt.plot(gif_centers[nframe][:, 0], gif_centers[nframe][:, 1], 'sk')
    plt.title(TITLE)

if __name__ == '__main__':
    main()
