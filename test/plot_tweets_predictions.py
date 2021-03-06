import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

#configs
x_scale = (0,5.5)
y_scale = (0,5.5)
plot_path = "plots/"

#load ground truth labels
O = []
C = []
E = []
A = []
N = []

for line in open("questionnaires.csv", "r"):
    parts= line.split(";")
    O.append(float(parts[-10].replace(",",".")))
    C.append(float(parts[-9].replace(",",".")))
    E.append(float(parts[-8].replace(",",".")))
    A.append(float(parts[-7].replace(",",".")))
    N.append(float(parts[-6].replace(",",".")))


#load MP small predictions
O1 = []
C1 = []
E1 = []
A1 = []
N1 = []

for line in open("personality_predictions1.csv"):
    parts = line.split(",")
    O1.append(float(parts[1].replace(",",".")))
    C1.append(float(parts[2].replace(",",".")))
    E1.append(float(parts[3].replace(",",".")))
    A1.append(float(parts[4].replace(",",".")))
    N1.append(float(parts[5].replace(",",".")))

#load MP big predictions test 2
O2 = []
C2 = []
E2 = []
A2 = []
N2 = []

for line in open("personality_predictions1_big.csv"):
    parts = line.split(",")
    O2.append(float(parts[1].replace(",",".")))
    C2.append(float(parts[2].replace(",",".")))
    E2.append(float(parts[3].replace(",",".")))
    A2.append(float(parts[4].replace(",",".")))
    N2.append(float(parts[5].replace(",",".")))

#load MP big predictions test 3
O3 = []
C3 = []
E3 = []
A3 = []
N3 = []

for line in open("personality_predictions1_big_userWise.csv"):
    parts = line.split(",")
    O3.append(float(parts[1].replace(",",".")))
    C3.append(float(parts[2].replace(",",".")))
    E3.append(float(parts[3].replace(",",".")))
    A3.append(float(parts[4].replace(",",".")))
    N3.append(float(parts[5].replace(",",".")))

mse_O_1 = mean_squared_error(O,O1)
mse_C_1 = mean_squared_error(C,C1)
mse_E_1 = mean_squared_error(E,E1)
mse_A_1 = mean_squared_error(A,A1)
mse_N_1 = mean_squared_error(N,N1)

mse_O_2 = mean_squared_error(O,O2)
mse_C_2 = mean_squared_error(C,C2)
mse_E_2 = mean_squared_error(E,E2)
mse_A_2 = mean_squared_error(A,A2)
mse_N_2 = mean_squared_error(N,N2)

mse_O_3 = mean_squared_error(O,O3)
mse_C_3 = mean_squared_error(C,C3)
mse_E_3 = mean_squared_error(E,E3)
mse_A_3 = mean_squared_error(A,A3)
mse_N_3 = mean_squared_error(N,N3)

fp = open("twitusers_predictions_benchmark_smallBig.csv", "w")
fp.write("mse,O,1,"+str(mse_O_1)+"\n")
fp.write("mse,C,1,"+str(mse_C_1)+"\n")
fp.write("mse,E,1,"+str(mse_E_1)+"\n")
fp.write("mse,A,1,"+str(mse_A_1)+"\n")
fp.write("mse,N,1,"+str(mse_N_1)+"\n")
fp.write("mse,O,2,"+str(mse_O_2)+"\n")
fp.write("mse,C,2,"+str(mse_C_2)+"\n")
fp.write("mse,E,2,"+str(mse_E_2)+"\n")
fp.write("mse,A,2,"+str(mse_A_2)+"\n")
fp.write("mse,N,2,"+str(mse_N_2)+"\n")
fp.write("mse,O,2,"+str(mse_O_3)+"\n")
fp.write("mse,C,2,"+str(mse_C_3)+"\n")
fp.write("mse,E,2,"+str(mse_E_3)+"\n")
fp.write("mse,A,2,"+str(mse_A_3)+"\n")
fp.write("mse,N,2,"+str(mse_N_3)+"\n")
fp.close()

for elem in zip([O,C,E,A,N],[O1,C1,E1,A1,N1],[O2,C2,E2,A2,N2],[O3,C3,E3,A3,N3],["O","C","E","A","N"]):
	plt.clf()
	plt.xlim(x_scale)
	plt.ylim(y_scale)
	plt.plot(elem[0], elem[1], '.', color='b')
	plt.plot(elem[0], elem[2], '.', color='r')
	plt.plot(elem[0], elem[3], '.', color='g')
	plt.ylabel('predicted values')
	plt.xlabel('actual values')
	plt.legend(["MP small", "MP big test2", "MP big test3"])
	plt.savefig(plot_path+elem[4]+".png")
	plt.show()
