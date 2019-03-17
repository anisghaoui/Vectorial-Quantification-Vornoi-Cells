
import math
import random 
import matplotlib.pyplot as plt


figure_number=1
def plot_fig (x : list , y: list ,option = '+'):
	#plotting
	global figure_number
	plt.figure(figure_number)
	plt.plot(x,y,option)

def plot_clusters(clusters : list,centers : list):
	for cluster in clusters:
		try :
			A,B	= zip(*cluster)
		except :
			pass
		A,B =list(A),list(B)
		plot_fig(A,B,"x")
	for center in centers:
		A,B	= zip(*centers)
		A,B =list(A),list(B)
		plot_fig(A,B,"+")

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
	clusters=[[]for x in range(0,len(centers))]
	for point in points:
		index =closest_center(point,centers) # cluster is empty when it shouldn't
		clusters[index].append(point)
		print(point,centers[index])
	return clusters

def average_of_cluster(points : list ):
	x,y = zip(*points)
	x,y =list(x),list(y)
	return [sum(x)/len(x),sum(y)/len(y)]

M=2
N=10

def main():
	x_0 = [ random.gauss(0,1)for x in range(0,N)]
	x_1 = [ random.gauss(0,1)for x in range(0,N)]
	Points =list(zip(x_0,x_1))
	k = 0 
	centers = []
	while k < M:
		point = Points[random.randint(0,N-1)]
		if point not in centers:
			centers.append(point)
			k +=1
	clusters  = cluster_forming(Points,centers)

	for cluster in clusters:
		print(len(cluster))
	plot_clusters(clusters,centers)
	
	plt.show()
main()