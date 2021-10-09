import os,glob
import numpy as np
import itertools
import matplotlib.pyplot as plt
pairpot=[]
for pair in glob.glob("./pairpot[0-9][0-9]"):
	pairpot.append(pair);
All_Pair_Potentials=[]
for i in range(len(pairpot)):
	pair_data=[]
	with open(pairpot[i],"r") as file:
		for lines in file:
			pair_data.append(lines.split())
	file.close()
	pair_data_polished=[]
	pair_data_polished.append([pair_data[0][1],pair_data[0][2]])
	for i in range(1,len(pair_data)-9):
		pair_data_polished.append(pair_data[i])
	All_Pair_Potentials.append(pair_data_polished)
max=1
for i in range(len(All_Pair_Potentials)):
	if len(All_Pair_Potentials[i]) > max:
		max=len(All_Pair_Potentials[i])
#print(max)
#print(len(All_Pair_Potentials[0]))
#plt.figure()
mins=[]
for i in range(len(All_Pair_Potentials)):
	x=[All_Pair_Potentials[i][k] for k in range(1,len(All_Pair_Potentials[i]))]
	y=np.float64(x)
	mins.append(np.min(y[:,1]))
	labels="{}-{}".format(All_Pair_Potentials[i][0][0],All_Pair_Potentials[i][0][1])
	plt.plot(y[:,0],y[:,1],label=labels)
	plt.legend()
#plt.ylim((,1))
min_val_on_graph=np.min(mins)
if min_val_on_graph<0:
	plt.ylim((min_val_on_graph-1,1.5))
elif min_val_on_graph>0:
	plt.ylim((min_val_on_graph+1,1.5))
plt.show()
All_Pair_Potentials_Copy=All_Pair_Potentials
#for i in range(len(All_Pair_Potentials)):
#	print(len(All_Pair_Potentials[i]))
#	for j in range(len(All_Pair_Potentials[i])):
#		print(All_Pair_Potentials[i][j])
#	print("**************************************************************************************************")
for i in range(len(All_Pair_Potentials_Copy)):
	if len(All_Pair_Potentials_Copy[i])<max:
		for j in range(max-len(All_Pair_Potentials_Copy[i])):
			All_Pair_Potentials_Copy[i].append(list(str('                    ')*2))
Trans_Data=[]
for j in range(len(All_Pair_Potentials_Copy[0])):
	Data_Row=[]
	for i in range(len(All_Pair_Potentials_Copy)):
		Data_Row.append(All_Pair_Potentials_Copy[i][j][0])
		Data_Row.append(All_Pair_Potentials_Copy[i][j][1])
	separator=' '
	new_string=separator.join(Data_Row)
	Trans_Data.append(new_string)
with open("Potential.txt","w") as file:
	for i in range(len(Trans_Data)):
		file.writelines(Trans_Data[i])
		file.writelines("\n")
file.close()