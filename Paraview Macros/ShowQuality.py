# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
poreEqAreaConsV5C0q00vtk = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
poreEqAreaConsV5C0q00vtkDisplay = GetDisplayProperties(poreEqAreaConsV5C0q00vtk, view=renderView1)

# set scalar coloring
ColorBy(poreEqAreaConsV5C0q00vtkDisplay, ('POINTS', 'vectors', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
poreEqAreaConsV5C0q00vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
poreEqAreaConsV5C0q00vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'vectors'
vectorsTF2D = GetTransferFunction2D('vectors')

# get color transfer function/color map for 'vectors'
vectorsLUT = GetColorTransferFunction('vectors')
vectorsLUT.TransferFunction2D = vectorsTF2D
vectorsLUT.RGBPoints = [0.9999993213667537, 0.231373, 0.298039, 0.752941, 0.9999999961992322, 0.865003, 0.865003, 0.865003, 1.0000006710317106, 0.705882, 0.0156863, 0.14902]
vectorsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'vectors'
vectorsPWF = GetOpacityTransferFunction('vectors')
vectorsPWF.Points = [0.9999993213667537, 0.0, 0.5, 0.0, 1.0000006710317106, 1.0, 0.5, 0.0]
vectorsPWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(poreEqAreaConsV5C0q00vtkDisplay, ('POINTS', 'vectors', 'Y'))

# rescale color and/or opacity maps used to exactly fit the current data range
poreEqAreaConsV5C0q00vtkDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(vectorsLUT, poreEqAreaConsV5C0q00vtkDisplay)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
vectorsLUT.ApplyPreset('Viridis (matplotlib)', True)

# create a new 'Mesh Quality'
meshQuality1 = MeshQuality(registrationName='MeshQuality1', Input=poreEqAreaConsV5C0q00vtk)

# show data in view
meshQuality1Display = Show(meshQuality1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'Quality'
qualityTF2D = GetTransferFunction2D('Quality')

# get color transfer function/color map for 'Quality'
qualityLUT = GetColorTransferFunction('Quality')
qualityLUT.TransferFunction2D = qualityTF2D
qualityLUT.RGBPoints = [1.0000039695845067, 0.231373, 0.298039, 0.752941, 1.377596507523513, 0.865003, 0.865003, 0.865003, 1.7551890454625194, 0.705882, 0.0156863, 0.14902]
qualityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Quality'
qualityPWF = GetOpacityTransferFunction('Quality')
qualityPWF.Points = [1.0000039695845067, 0.0, 0.5, 0.0, 1.7551890454625194, 1.0, 0.5, 0.0]
qualityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
meshQuality1Display.Representation = 'Surface'
meshQuality1Display.ColorArrayName = ['CELLS', 'Quality']
meshQuality1Display.LookupTable = qualityLUT
meshQuality1Display.SelectTCoordArray = 'None'
meshQuality1Display.SelectNormalArray = 'None'
meshQuality1Display.SelectTangentArray = 'None'
meshQuality1Display.OSPRayScaleArray = 'vectors'
meshQuality1Display.OSPRayScaleFunction = 'PiecewiseFunction'
meshQuality1Display.SelectOrientationVectors = 'vectors'
meshQuality1Display.ScaleFactor = 1.2000000000000002
meshQuality1Display.SelectScaleArray = 'Quality'
meshQuality1Display.GlyphType = 'Arrow'
meshQuality1Display.GlyphTableIndexArray = 'Quality'
meshQuality1Display.GaussianRadius = 0.06
meshQuality1Display.SetScaleArray = ['POINTS', 'vectors']
meshQuality1Display.ScaleTransferFunction = 'PiecewiseFunction'
meshQuality1Display.OpacityArray = ['POINTS', 'vectors']
meshQuality1Display.OpacityTransferFunction = 'PiecewiseFunction'
meshQuality1Display.DataAxesGrid = 'GridAxesRepresentation'
meshQuality1Display.PolarAxes = 'PolarAxesRepresentation'
meshQuality1Display.ScalarOpacityFunction = qualityPWF
meshQuality1Display.ScalarOpacityUnitDistance = 0.450491986115592
meshQuality1Display.OpacityArrayName = ['CELLS', 'Quality']
meshQuality1Display.SelectInputVectors = ['POINTS', 'vectors']
meshQuality1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
meshQuality1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
meshQuality1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(poreEqAreaConsV5C0q00vtk, renderView1)

# show color bar/color legend
meshQuality1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on meshQuality1Display
meshQuality1Display.Position = [0.0, -5.0, 0.0]

# Properties modified on meshQuality1Display.DataAxesGrid
meshQuality1Display.DataAxesGrid.Position = [0.0, -5.0, 0.0]

# Properties modified on meshQuality1Display.PolarAxes
meshQuality1Display.PolarAxes.Translation = [0.0, -5.0, 0.0]

# Properties modified on meshQuality1
meshQuality1.TriangleQualityMeasure = 'Equiangle Skew'

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
qualityLUT.RescaleTransferFunction(0.0017515496197994195, 1.7551890454625194)

# Rescale transfer function
qualityPWF.RescaleTransferFunction(0.0017515496197994195, 1.7551890454625194)

# set active source
SetActiveSource(poreEqAreaConsV5C0q00vtk)

# show data in view
poreEqAreaConsV5C0q00vtkDisplay = Show(poreEqAreaConsV5C0q00vtk, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
poreEqAreaConsV5C0q00vtkDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(meshQuality1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
qualityLUT.ApplyPreset('Viridis (matplotlib)', True)

# Properties modified on qualityLUT
qualityLUT.NanColor = [0.0, 0.0, 0.0]

# Rescale transfer function
qualityLUT.RescaleTransferFunction(0.0017515496197994195, 0.5015347814295779)

# Rescale transfer function
qualityPWF.RescaleTransferFunction(0.0017515496197994195, 0.5015347814295779)

# get the material library
materialLibrary1 = GetMaterialLibrary()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1198, 768)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.31886299740031177, -2.291827793814739, 40.2]
renderView1.CameraFocalPoint = [0.31886299740031177, -2.291827793814739, 0.0]
renderView1.CameraParallelScale = 7.65271193760748

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).