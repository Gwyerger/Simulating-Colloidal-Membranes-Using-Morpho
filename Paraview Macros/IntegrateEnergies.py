# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import numpy as np

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
totalEnergyDensity = FindSource('Total Energy Density')

# find source
computeDerivatives1 = FindSource('ComputeDerivatives1')

# find source
poreEq000vtk = FindSource('PoreEq00#0.vtk*')

# find source
tilt = FindSource('Tilt')

# find source
pointDatatoCellData1 = FindSource('PointDatatoCellData1')

# find source
nematic = FindSource('Nematic')

# find source
pureBend = FindSource('Pure Bend')

# find source
extractCellsByType1 = FindSource('ExtractCellsByType1')

# find source
pureSplay = FindSource('Pure Splay')

# find source
pureTwist = FindSource('Pure Twist')


# set active source
SetActiveSource(totalEnergyDensity)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=totalEnergyDensity)

# get active view
spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables1Display
integrateVariables1Display.Assembly = ''

# set active source
SetActiveSource(pureSplay)

# create a new 'Integrate Variables'
integrateVariables2 = IntegrateVariables(registrationName='IntegrateVariables2', Input=pureSplay)

# show data in view
integrateVariables2Display = Show(integrateVariables2, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables2Display
integrateVariables2Display.Assembly = ''

# set active source
SetActiveSource(pureBend)

# create a new 'Integrate Variables'
integrateVariables3 = IntegrateVariables(registrationName='IntegrateVariables3', Input=pureBend)

# show data in view
integrateVariables3Display = Show(integrateVariables3, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables3Display
integrateVariables3Display.Assembly = ''

# set active source
SetActiveSource(pureTwist)

# create a new 'Integrate Variables'
integrateVariables4 = IntegrateVariables(registrationName='IntegrateVariables4', Input=pureTwist)

# show data in view
integrateVariables4Display = Show(integrateVariables4, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables3Display
integrateVariables4Display.Assembly = ''

# set active source
SetActiveSource(tilt)

# create a new 'Integrate Variables'
integrateVariables5 = IntegrateVariables(registrationName='IntegrateVariables5', Input=tilt)

# show data in view
integrateVariables5Display = Show(integrateVariables5, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables5Display
integrateVariables5Display.Assembly = ''

# set active source
SetActiveSource(nematic)

# create a new 'Integrate Variables'
integrateVariables6 = IntegrateVariables(registrationName='IntegrateVariables6', Input=nematic)

# show data in view
integrateVariables6Display = Show(integrateVariables6, spreadSheetView1, 'SpreadSheetRepresentation')

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on integrateVariables6Display
integrateVariables6Display.Assembly = ''

# create a new 'Pass Arrays'
passArrays1 = PassArrays(Input=integrateVariables2)
passArrays1.CellDataArrays = ['Pure Splay']


# update the view to ensure updated data information
spreadSheetView1.Update()

Energies = []

ss_data = paraview.servermanager.Fetch(passArrays1)    
Energies.append(ss_data.GetCellData().GetArray('Pure Splay').GetValue(0))


# create a new 'Pass Arrays'
passArrays1 = PassArrays(Input=integrateVariables4)
passArrays1.CellDataArrays = ['Pure Twist']


# update the view to ensure updated data information
spreadSheetView1.Update()


ss_data = paraview.servermanager.Fetch(passArrays1)    
Energies.append(ss_data.GetCellData().GetArray('Pure Twist').GetValue(0))

# create a new 'Pass Arrays'
passArrays1 = PassArrays(Input=integrateVariables3)
passArrays1.CellDataArrays = ['Pure Bend']


# update the view to ensure updated data information
spreadSheetView1.Update()


ss_data = paraview.servermanager.Fetch(passArrays1)    
Energies.append(ss_data.GetCellData().GetArray('Pure Bend').GetValue(0))

# create a new 'Pass Arrays'
passArrays1 = PassArrays(Input=integrateVariables5)
passArrays1.CellDataArrays = ['Tilt']


# update the view to ensure updated data information
spreadSheetView1.Update()


ss_data = paraview.servermanager.Fetch(passArrays1)    
Energies.append(ss_data.GetCellData().GetArray('Tilt').GetValue(0))


# create a new 'Pass Arrays'
passArrays1 = PassArrays(Input=integrateVariables1)
passArrays1.CellDataArrays = ['Total Energy Density']


# update the view to ensure updated data information
spreadSheetView1.Update()


ss_data = paraview.servermanager.Fetch(passArrays1)    
Energies.append(ss_data.GetCellData().GetArray('Total Energy Density').GetValue(0))


print(Energies[0])
print(Energies[1])
print(Energies[2])
print(Energies[3])
print(Energies[4])