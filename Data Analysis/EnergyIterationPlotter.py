import numpy as np
import matplotlib.pyplot as plt

## Be able to grab data from txt files and plot it. 

path = "C:/Users/gabey/OneDrive/Desktop/Fall 2023/SM Research/Phase Diagram VTK Exports and PP/Single Pore Round 4/"

for i in range(1, 2):
    for j in range(0, 11):
        name1 = "EnergiesItg"+str(i)+"q"+str(j)+"sopt.txt"
        name2 = "EnergiesItg"+str(i)+"q"+str(j)+"fopt.txt"
        # name1 = "EnergiesItsopt.txt"
        # name2 = "EnergiesItfopt.txt"
        file1 = open(path+name1, "r")
        strdata1 = file1.readlines()
        for ii in range(0, len(strdata1)):
            strdata1[ii] = float(strdata1[ii])
        datarray1 = np.array(strdata1)
        #Now Grabbing second data file:
        file2 = open(path+name2, "r")
        strdata2 = file2.readlines()
        for ii in range(0, len(strdata2)):
            strdata2[ii] = float(strdata2[ii])
        datarray2 = np.array(strdata2)
        fig,ax = plt.subplots(2)
        ax[0].plot(np.arange(0, len(datarray1), 1), datarray1[:], label = "sopt")
        ax[1].plot(np.arange(0, len(datarray2), 1), datarray2[:], label = "fopt")
        ax[0].set_title("Energy Optimization over Iterations")
        ax[0].set_ylabel("Shape Optimizer Energy")
        ax[0].set_xlabel("Iterations")
        ax[0].set_ylim((datarray1.min(),datarray1.max()))
        ax[1].set_ylabel("Field Optimizer Energy")
        ax[1].set_xlabel("Iterations")
        ax[1].set_ylim((datarray2.min(),datarray2.max()))
        ax[0].grid(visible=True, which = 'major')
        ax[0].legend()
        ax[1].grid(visible=True, which = 'major')
        ax[1].legend()
        fig.set_size_inches(6, 5)
        plt.show()
        fig.savefig(path +"EnergyIterationsg"+str(i)+"q"+str(j)+".png")


