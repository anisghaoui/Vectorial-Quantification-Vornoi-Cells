import math
import random 
import matplotlib.pyplot as plt

def average_of_a_cluster(points : list ):
	x,y = zip(*points)
	x,y =list(x),list(y)
	return [sum(x)/len(x),sum(y)/len(y)]

def average_of_clusters(clusters : list):
	averages=[]
	for cluster in clusters:
		averages.append(average_of_a_cluster(cluster))
	return averages

def distance (V1 : list, V2 :list ):
	return math.sqrt((V1[0]-V2[0])**2+(V1[1]-V2[1])**2)

def closest_center (point: list , centers : list):
	min = distance (point,centers[0])
	index = 0
	for center in centers:
		if(min >= distance (point,center)) :
			min = distance (point,center)
			index = centers.index(center)
	return index

def cluster_forming (points : list , centers : list):
	clusters=[[]for x in range(0,M)]
	for point in points:
		clusters[closest_center(point,centers)].append(point)
	return clusters

M=4
N=10000

def main():
	x_0 = [ random.gauss(0,1)for x in range(0,N)]
	x_1 = [ random.gauss(0,1)for x in range(0,N)]
	Points =list(zip(x_0,x_1))
	
	centers = [Points[random.randint(0,N-1)]  for i in range(0,M)]
	clusters  = cluster_forming(Points,centers)
	
	#print("before",centers)
	#print("after",average_of_clusters (clusters))

main()