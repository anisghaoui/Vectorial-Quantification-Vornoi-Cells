#
import math	
import random
import matplotlib.pyplot as plt
import numpy as np
import ffmpeg
import pandas as pd

from matplotlib import animation

#clustering
def distance (V1 : list, V2 :list ):
	return math.sqrt((V1[0]-V2[0])**2+(V1[1]-V2[1])**2)

def closest_center (point: list , centers : list):
	min = distance (point,centers[0])
	index = 0
	for center in centers:
		if(min > distance (point,center)) :
			min = distance (point,center)
			index = centers.index(center)
	return index	

def cluster_forming (points : list , centers : list):
	clusters=[[] for i in range(0,len(centers))]

	for point in points:
		clusters[closest_center(point,centers)].append(point)
	return clusters


def average_of_a_cluster(points : list ):
	x,y=[],[]
	x,y = zip(*points)
	x,y =list(x),list(y)
	return [sum(x)/len(x),sum(y)/len(y)]

	

def average_of_clusters(clusters : list):
	average = []
	for cluster in clusters:
		average.append(average_of_a_cluster(cluster))
	return average

def get_distortion(clusters :list ,centers : list):
	sum = 0.0
	for i in range(0,len(centers)):
		for point in clusters[i]:
			sum += distance(point,centers[i])**2
	return sum

#avoid duplicate centers
def get_centers(points: list,M : int):
	k = 0 
	centers = []
	while k < M:
		point = points[random.randint(0,N-1)]
		if point not in centers:
			centers.append(point)
			k +=1
	return centers

#LBG algo
def LBG(points : list ,M :int, eps : float,max_cells :int):

	#initializing
	distortion = [9999999]
	k = 0
	centers = get_centers(points,M)

	for i in range(0,int(math.log(max_cells,2))):
		distorion_deviation = distortion[0]
		save = centers
		centers = get_centers(points,M)
		M *=2
		for center in save:
			centers[save.index(center)]=center
		while distorion_deviation>= eps:
			clusters = cluster_forming(points,centers)
			centers = average_of_clusters(clusters)
			distortion.append(get_distortion(clusters,centers)/len(points[0]))
			distorion_deviation =  (distortion[k] - distortion[k+1])/distortion[k+1]
			k +=1
			Cdata.append(centers)
			Kdata.append(clusters)
	return clusters,centers,distortion,k

#animation
Kdata,Cdata =[],[]
title ="Vectorial quantification - Voronoi cells formation"
def animate(nframe):
	plt.cla()
	plt.ylim(-3,3)
	plt.xlim(-3,3)
	for cluster in Kdata[nframe]:
		X,Y = zip(*cluster)
		plt.plot(list(X),list(Y),'.')
	X,Y = zip(*Cdata[nframe])
	plt.plot(list(X),list(Y),'+k')
	plt.title(title)


N = 10000
eps = 0.001
M = 2
max_cells = 16
def main():
	x_0 = [ random.gauss(0,1) for x in range(0,N)]
	x_1 = [ random.gauss(0,1) for x in range(0,N)]
	points = list(zip(x_0,x_1))
	
	clusters,centers,distortion,iterations= LBG(points,M,eps,max_cells)
	
	fig = plt.figure(figsize=(10,10))
	anim = animation.FuncAnimation(fig, animate, frames=iterations,interval=200,repeat =True)
	anim.save(title+'.gif', fps=4)
	plt.show()

	plt.cla()
	plt.plot(range(1,iterations+1),distortion[1:])
	plt.title('distortion as a function of number of LGB iterations')
	plt.savefig('distortion as a function of LGB iterations'+'.png')
	plt.show()

main()