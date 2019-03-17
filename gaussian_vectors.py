	#

import random
import matplotlib.pyplot as plt
import numpy as np


figure_number =1

def plot_fig (x : list , y: list ):
	#plotting
	global figure_number
	plt.figure(figure_number)
	plt.plot(x,y,'+')
	figure_number += 1


def main():
	vectors = [ np.array([ random.gauss(0,1), random.gauss(0,1)]) for x in range(0,N)]
	for vector in vectors:
		print(vector)

		
	plt.show()
main()