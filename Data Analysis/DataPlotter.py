import numpy as np
import matplotlib.pyplot as plt

## Be able to grab data from txt files and plot it. 

# First Grabbing Bob's Data:
r=5
path = "C:\\Users\\gabey\\OneDrive\\Desktop\\Fall 2023\\SM Research\\Colloidal Droplets - Benchmarking\\Disk Data\\"
name1 = "solution"+str(r)+".txt"
delimiter = "\t"
pop = "\n"
file = open(path+name1, "r")
strdata = file.readlines()
# print("Before: ")
# print(strdata)
for i in range(0, len(strdata)):
    strdata[i] = strdata[i].replace(pop, "")
    strdata[i] = strdata[i].split(delimiter)
    for j in range(0, len(strdata[i])):
        strdata[i][j] = float(strdata[i][j])
# print("After: ")
# print(strdata)
datarray = np.array(strdata)
# print("To array: ")
# print(datarray)

#Now Grabbing Morpho Data:

name2 = "rs="+str(r)+" PVdata.txt"
delimiter = ","
pop = "\n"
file = open(path+name2, "r")
strdatam = file.readlines()
print(strdatam[0])
strdatam = strdatam[1:]


for i in range(0, len(strdatam)):
    strdatam[i] = strdatam[i].replace(pop, "")
    strdatam[i] = strdatam[i].split(delimiter)
    for j in range(0, len(strdatam[i])):
        strdatam[i][j] = float(strdatam[i][j])

datarraym = np.array(strdatam)

fig,ax = plt.subplots()

ax.plot(datarray[:, 0], datarray[:, 1], label = "Bob's Data")
ax.plot(r-r*datarraym[:, 5], datarraym[:, 0], label = "Morpho's Data")

ax.set_title("Morpho Data compared with Bob's Data: $R^*$ = "+ str(r))
ax.set_ylabel("$\\theta$")
ax.set_xlabel("$r^*$")
ax.grid(visible=True, which = 'major')
ax.legend()
plt.show()
fig.savefig(path +"Rstar"+ str(r) +".png")


