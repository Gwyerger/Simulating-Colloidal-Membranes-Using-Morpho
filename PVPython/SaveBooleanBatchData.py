# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

BoolData = [["gamma","q","is pore"]]

numtimesteps = 50
gcount = 20
qcount = 20


for ii in range(1, gcount+1):
    for jj in range(0, qcount+1):
        
        gg = 5*ii
        qq = 50 + 5*jj
        # create a new 'Legacy VTK Reader'
        DataSet = LegacyVTKReader(registrationName='SinglePoreFixedg'+ str(gg) +'q'+ str(qq) +'.vtk*', FileNames=['C:\\Users\\gabey\\OneDrive\\Desktop\\Fall 2023\\SM Research\\Phase Diagram VTK Exports and PP\\Single Pore Round 2\\VTK\\SinglePoreFixedg'+ str(gg) +'q'+ str(qq) +'_'+str(i)+'.vtk' for i in range(0, numtimesteps+1)])

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


        print("Initial Area: ")
        print(Area1)
        print("Final Area: ")
        print(Area2)
        print("Final over Initial: ")
        print(Area2/Area1)

        if (Area2/Area1 < 1):
            BoolData.append([str(gg), str(qq), "True"])
        elif (1.0075 > Area2/Area1 > 1):
            BoolData.append([str(gg), str(qq), "None"])
        elif (Area2/Area1 > 1.0075):
            BoolData.append([str(gg), str(qq), "False"])

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

print(BoolData)

f = open("C:\\Users\\gabey\\OneDrive\\Desktop\\Fall 2023\\SM Research\\Phase Diagram VTK Exports and PP\\Single Pore Round 2\\IsPoreData.txt", "w")
for i in range(0, len(BoolData)):
    f.write(', '.join(BoolData[i])+'\n')
