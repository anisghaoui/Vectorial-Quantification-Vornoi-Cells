#!/usr/bin/python3

import random
import matplotlib.pyplot as plt
import numpy as np


samples = 5000
display = 0


figure_number = 1

def plot_fig (x : list ,y: list ):
	#plotting
	global figure_number
	plt.figure(figure_number )
	plt.plot(x,y,'+')
	figure_number += 1



def main():
	Xm = 4
	R = 2
	M = 2**R
	vector =[]
	for x in range(0,samples):
		#vector.append(random.gauss(0,1/3*Xm*Xm)/Xm)
		vector.append(random.uniform(-Xm,Xm))
	N =np.linspace(0,samples,samples)
	if display:	
		plot_fig (N,vector)	
	delta  = 2*Xm/M
	intervals = [-Xm + i*delta for i in range(0,M+1) ]
	vector.sort()
	qx =[]
	for x in vector :
		if x < -Xm :
			qx.append(0)	
		elif x > Xm :
			qx.append(M-1)
		else :
			for i in range(1,len(intervals)) :
				if x >= (intervals[i]- delta) and x <= intervals[i] :
					qx.append(i-1)	
	if display:	
		N =np.linspace(-Xm,Xm,samples)
		plot_fig(N,qx)	
	Qx =[]
	for value in qx :
		Qx.append(value*1/2*Xm +(-3/4*Xm))
	if display:	
		plot_fig(N,sorted(Qx))
	distance =[]
	for i in range(0,len(Qx)):
		distance.append(vector[i]-Qx[i])
	if display:	
		plot_fig(N,distance)

	varianceX =  1/3*Xm**Xm
	distortion =[]
	for i in range(0,10):
		distortion.append(varianceX*(2**(-2*i)))
	if display :
		plot_fig(range(0,10),distortion);

	

	if display :
		plt.show()
main()