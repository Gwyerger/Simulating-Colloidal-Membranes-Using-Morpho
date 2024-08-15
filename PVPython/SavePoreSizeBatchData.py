# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

SizeData = [["gamma","p","q","Pore Size"]]
AofRect = 48
numtimesteps = 161
gcount = 2
fcount = 2
qcount = 10
path = 'C:/Users/gabey/OneDrive/Desktop/Fall 2023/SM Research/Phase Diagram VTK Exports and PP/Single Pore Round 4 - test pt3/'

for ii in range(0, gcount+1):
    for kk in range(0, fcount+1):
        for jj in range(0, qcount+1):
            
            gg = round(0.5 + 0.1*ii, ndigits = 2)
            ff = round(0.6 + 0.1*kk, ndigits = 2)
            qq = round(1 + 0.1*jj, ndigits = 2)
            if jj==0 or jj==10: qq = round(qq)
            # create a new 'Legacy VTK Reader'
            DataSet = LegacyVTKReader(registrationName='SinglePoreg'+ str(ii) +'f'+ str(kk)+'q'+ str(jj) +'.vtk*', FileNames=['C:\\Users\\gabey\\OneDrive\\Desktop\\Fall 2023\\SM Research\\Phase Diagram VTK Exports and PP\\Single Pore Round 4 - test pt3\\VTK Files\\SinglePoreg'+ str(gg) + 'f' + str(ff) + 'q'+ str(qq)+'Final.vtk'])

            # create a new 'Integrate Variables'
            integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=DataSet)

            # Create a new 'SpreadSheet View'
            spreadSheetView1 = CreateView('SpreadSheetView')
            spreadSheetView1.ColumnToSort = ''
            spreadSheetView1.BlockSize = 1024

            # show data in view
            integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

        
            # Properties modified on integrateVariables1Display
            integrateVariables1Display.Assembly = ''


            # update the view to ensure updated data information
            spreadSheetView1.Update()

            # Properties modified on spreadSheetView1
            spreadSheetView1.FieldAssociation = 'Cell Data'

            # set active source
            SetActiveSource(integrateVariables1)

            # create a new 'Pass Arrays'
            passArrays1 = PassArrays(Input=integrateVariables1)
            passArrays1.CellDataArrays = ['Area']
            ss_data = paraview.servermanager.Fetch(passArrays1)    
            Area1 = ss_data.GetCellData().GetArray('Area').GetValue(0)

            # set active source
            SetActiveSource(integrateVariables1)

            # get animation scene
            animationScene1 = GetAnimationScene()

            animationScene1.GoToLast()

            # create a new 'Pass Arrays'
            passArrays1 = PassArrays(Input=integrateVariables1)
            passArrays1.CellDataArrays = ['Area']
            ss_data = paraview.servermanager.Fetch(passArrays1)  
            Area2 = ss_data.GetCellData().GetArray('Area').GetValue(0)


            print("g"+str(ii)+" f"+str(jj)+" q"+str(kk))

            SizeData.append([str(gg), str(ff), str(qq), str(AofRect - Area2)])

            animationScene1.GoToFirst()

            # destroy DataSet
            Delete(spreadSheetView1)
            del spreadSheetView1

            # destroy integrateVariables1
            Delete(integrateVariables1)
            del integrateVariables1

            Delete(passArrays1)
            del passArrays1

            Delete(DataSet)
            del DataSet

print(SizeData)

f = open(path+"PoreSizeData.txt", "w")
for i in range(0, len(SizeData)):
    f.write(', '.join(SizeData[i])+'\n')
