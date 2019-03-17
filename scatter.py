	#

import random
import matplotlib.pyplot as plt
import numpy as np

figure_number = 1
N =  100 


def plot_fig (x : list ,y: list ):
	#plotting
	global figure_number
	plt.figure(figure_number)
	plt.plot(x,y,'+')
	figure_number += 1



def main():
	x =[ random.randint(0,N-1) for i in range(0,N-1)]
	y =[ random.randint(0,N-1) for i in range(0,N-1)]
	print(x,y)
	t = np.linspace(0,N-1,N)
	plot_fig(x,y)
	plt.show()
main()