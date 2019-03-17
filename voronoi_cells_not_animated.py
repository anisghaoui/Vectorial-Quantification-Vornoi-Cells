#
import math	
import random
import matplotlib.pyplot as plt
import numpy as np
import time 

figure_number =1

def plot_fig (x : list , y: list ,option = '+'):
	#plotting
	global figure_number
	plt.figure(figure_number)
	plt.plot(x,y,option)
	

	

def plot_clusters(clusters : list,centers : list):
	plt.clf()
	for center in centers:
		A,B	= zip(*centers)
		A,B =list(A),list(B)
		plot_fig(A,B,"+k")
	for cluster in clusters:
		A,B	= zip(*cluster)
		A,B =list(A),list(B)
		plot_fig(A,B,".")
	global figure_number
	figure_number +=1
	

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

def get_centers(points: list):
	k = 0 
	centers = []
	while k < M:
		point = points[random.randint(0,N-1)]
		if point not in centers:
			centers.append(point)
			k +=1
	return centers

def LBG(points : list , M : int , eps : float):
	#initializing
	centers = get_centers(points)
	distortion = [9999999]
	distorion_deviation = distortion[0]
	k = 0
	while distorion_deviation>= eps:
		clusters = cluster_forming(points,centers)
		
		centers = average_of_clusters(clusters)
		distortion.append(get_distortion(clusters,centers)/len(points[0]))
		distorion_deviation =  (distortion[k] - distortion[k+1])/distortion[k+1]
		k +=1	
		plot_clusters(clusters,centers)	
	return clusters,centers,distortion

N = 1000
eps = 0.005
M = 8
def main():
	x_0 = [ random.gauss(0,1)for x in range(0,N)]
	x_1 = [ random.gauss(0,1)for x in range(0,N)]
	points = list(zip(x_0,x_1))

	clusters,centers,distorion = LBG(points,M,eps)
	
	plot_clusters(clusters,centers)
	plt.show()
main()