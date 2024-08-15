# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

pathp = r'C:\Users\gabey\OneDrive\Desktop\Fall 2023\SM Research\Pure Cholesteric\VTK'
pathexp = r'C:\Users\gabey\OneDrive\Desktop\Fall 2023\SM Research\Pure Cholesteric\VTK'

num = 2001

for n in range(2000, num):
    pathc = pathp+f"\\Sim {n}"
    # ldocs = os.listdir(pathc)
    # maxiter = 0
    # for st in ldocs:
    #     if "_" in st:
    #         st = st.split("_")[1]
    #         iter = int(st.replace(".vtk", ""))
    #         if iter > maxiter:
    #             maxiter = iter

    # create a new 'Legacy VTK Reader'
    DataSet = LegacyVTKReader(registrationName='dataset*', FileNames=[pathc+f'\\PureCholesteric{n}q.vtk'])

        # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')
    spreadSheetView1.ColumnToSort = ''
    spreadSheetView1.BlockSize = 1024
    # show data in view
    DataDisplay = Show(DataSet, spreadSheetView1, 'SpreadSheetRepresentation')

    # get layout
    layout1 = GetLayout()

    # assign view to a particular cell in the layout
    AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

    # export view
    ExportView(f'C:\\Users\\gabey\\OneDrive\\Desktop\\Fall 2023\\SM Research\\Pure Cholesteric\\CSV\\Sim {n}.csv', view=spreadSheetView1)
    # destroy DataSet
    Delete(DataSet)
    del DataSet
    RemoveLayout(layout1)

