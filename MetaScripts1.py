



#histogram line
def draw_histline(input_lst,input_bins=20):
	import numpy as np
	import matplotlib.pyplot as plt
	y,binEdges=np.histogram(input_lst,bins=input_bins)
	bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
	plt.plot(bincenters,y,'-')


