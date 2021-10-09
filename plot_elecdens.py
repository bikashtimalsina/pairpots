import os,glob
import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn import preprocessing
elecdens=[]
for edens in glob.glob("./elecdens[0-9]"):
	elecdens.append(edens);
all_elecdens=[]
for i in range(len(elecdens)):
	edens_val=[]
	with open(elecdens[i],"r") as file:
		for lines in file:
			edens_val.append(lines.split())
	all_elecdens.append(edens_val)
	file.close()
for i in range(len(all_elecdens)):
	label=all_elecdens[i][0][1]
	xydata=np.float64(all_elecdens[i][1:-9])
	plt.plot(xydata[:,0],preprocessing.normalize(xydata[:,[1]],axis=0),label=label)
	plt.legend()
plt.show()