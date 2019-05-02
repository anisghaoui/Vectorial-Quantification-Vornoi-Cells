import matplotlib.pyplot as plt
import numpy as np
import math
from pprint import pprint


def boundaries (center, centers):
	boundaries =10
	step =0.1
	y = []
	x = []
	for c in centers:
		x1 = (center[0]+c[0])/2
		y1 = (center[1]+c[1])/2
		direction = (center[1]-c[1])/(center[0]-c[0]) if center[0]-c[0]!=0 else 9999999
		direction = -1 / direction if direction !=0 else 9999999
		offset = (y1- direction * x1)

		point = (x1,y1)
		value = x1 -step
		other_centers =centers.copy()
		other_centers.remove(c)
		while distance(point,center) < distance_other_centers(point,other_centers)\
				and math.fabs(value) <boundaries :
			x.append(value)
			y.append(direction * value + offset)
			point=(value,direction * value + offset)
			value -=step

		value = x1
		point=(value,direction * value + offset)

		while distance(point,center) < distance_other_centers(point,other_centers)\
				and math.fabs(value) <boundaries :
			x.append(value)
			y.append(direction * value + offset)
			point=(value,direction * value + offset)
			value +=step

	return zip(x,y)


def distance (V1 : list, V2 :list ):
	return math.sqrt((V1[0]-V2[0])**2+(V1[1]-V2[1])**2)


def distance_other_centers(point, centers):
	min = distance(point,centers[0])
	for center in centers:
		d = distance(point,center)
		if min >= d:
			min = d
	return min


def draw (shape,point_option : bool = False):
	A,B = zip(*shape)
	plt.plot(A,B,'+' if point_option else '') 
	plt.grid(1,'major','both')

if __name__ == '__main__':

	centers = [(1,2),(4,2),(5,6),(2,7)]
	center = (3.5,3)
	draw(centers,True)
	draw([center],True)
	draw(boundaries(center,centers),True)
	plt.show()