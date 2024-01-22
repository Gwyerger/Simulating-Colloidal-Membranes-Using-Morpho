# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
singlePoreFixedg6q0_0vtk = FindSource('SinglePoreFixedg6q0_0.vtk*')

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=singlePoreFixedg6q0_0vtk)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# Properties modified on integrateVariables1Display
integrateVariables1Display.Assembly = ''

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# update the view to ensure updated data information
renderView1.Update()

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

SelectIDs(IDs=[-1, 0], FieldType=0, ContainingCells=0)

SelectIDs(IDs=[-1, 0], FieldType=0, ContainingCells=0)

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
#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1202, 786)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 24.43620529482883]
renderView1.CameraParallelScale = 6.324555320336759

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).