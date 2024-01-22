# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get the material library
materialLibrary1 = GetMaterialLibrary()

# find source
totalEnergyDensity = FindSource('Total Energy Density')

# set active source
SetActiveSource(totalEnergyDensity)

# set active source
SetActiveSource(totalEnergyDensity)

# show data in view
totalEnergyDensityDisplay = Show(totalEnergyDensity, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'TotalEnergyDensity'
totalEnergyDensityTF2D = GetTransferFunction2D('TotalEnergyDensity')
totalEnergyDensityTF2D.ScalarRangeInitialized = 1
totalEnergyDensityTF2D.Range = [0.0, 2.0, 0.0, 1.0]

# get color transfer function/color map for 'TotalEnergyDensity'
totalEnergyDensityLUT = GetColorTransferFunction('TotalEnergyDensity')
totalEnergyDensityLUT.AutomaticRescaleRangeMode = 'Never'
totalEnergyDensityLUT.TransferFunction2D = totalEnergyDensityTF2D
totalEnergyDensityLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
totalEnergyDensityLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TotalEnergyDensity'
totalEnergyDensityPWF = GetOpacityTransferFunction('TotalEnergyDensity')
totalEnergyDensityPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
totalEnergyDensityPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
totalEnergyDensityDisplay.Representation = 'Surface'
totalEnergyDensityDisplay.ColorArrayName = ['CELLS', 'Total Energy Density']
totalEnergyDensityDisplay.LookupTable = totalEnergyDensityLUT
totalEnergyDensityDisplay.SelectTCoordArray = 'None'
totalEnergyDensityDisplay.SelectNormalArray = 'None'
totalEnergyDensityDisplay.SelectTangentArray = 'None'
totalEnergyDensityDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
totalEnergyDensityDisplay.SelectOrientationVectors = 'vectors'
totalEnergyDensityDisplay.ScaleFactor = 1.2000000000000002
totalEnergyDensityDisplay.SelectScaleArray = 'Total Energy Density'
totalEnergyDensityDisplay.GlyphType = 'Arrow'
totalEnergyDensityDisplay.GlyphTableIndexArray = 'Total Energy Density'
totalEnergyDensityDisplay.GaussianRadius = 0.06
totalEnergyDensityDisplay.SetScaleArray = [None, '']
totalEnergyDensityDisplay.ScaleTransferFunction = 'PiecewiseFunction'
totalEnergyDensityDisplay.OpacityArray = [None, '']
totalEnergyDensityDisplay.OpacityTransferFunction = 'PiecewiseFunction'
totalEnergyDensityDisplay.DataAxesGrid = 'GridAxesRepresentation'
totalEnergyDensityDisplay.PolarAxes = 'PolarAxesRepresentation'
totalEnergyDensityDisplay.ScalarOpacityFunction = totalEnergyDensityPWF
totalEnergyDensityDisplay.ScalarOpacityUnitDistance = 0.6088735100241448
totalEnergyDensityDisplay.OpacityArrayName = ['CELLS', 'Total Energy Density']
totalEnergyDensityDisplay.SelectInputVectors = [None, '']
totalEnergyDensityDisplay.WriteLog = ''

# show color bar/color legend
totalEnergyDensityDisplay.SetScalarBarVisibility(renderView1, True)

# Properties modified on totalEnergyDensityDisplay
totalEnergyDensityDisplay.Position = [0.0, -5.0, 0.0]

# Properties modified on totalEnergyDensityDisplay.DataAxesGrid
totalEnergyDensityDisplay.DataAxesGrid.Position = [0.0, -5.0, 0.0]

# Properties modified on totalEnergyDensityDisplay.PolarAxes
totalEnergyDensityDisplay.PolarAxes.Translation = [0.0, -5.0, 0.0]

# find source
pureSplay = FindSource('Pure Splay')

# set active source
SetActiveSource(pureSplay)

# show data in view
pureSplayDisplay = Show(pureSplay, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'PureSplay'
pureSplayTF2D = GetTransferFunction2D('PureSplay')
pureSplayTF2D.ScalarRangeInitialized = 1
pureSplayTF2D.Range = [0.0, 2.0, 0.0, 1.0]

# get color transfer function/color map for 'PureSplay'
pureSplayLUT = GetColorTransferFunction('PureSplay')
pureSplayLUT.AutomaticRescaleRangeMode = 'Never'
pureSplayLUT.TransferFunction2D = pureSplayTF2D
pureSplayLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
pureSplayLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'PureSplay'
pureSplayPWF = GetOpacityTransferFunction('PureSplay')
pureSplayPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
pureSplayPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pureSplayDisplay.Representation = 'Surface'
pureSplayDisplay.ColorArrayName = ['CELLS', 'Pure Splay']
pureSplayDisplay.LookupTable = pureSplayLUT
pureSplayDisplay.SelectTCoordArray = 'None'
pureSplayDisplay.SelectNormalArray = 'None'
pureSplayDisplay.SelectTangentArray = 'None'
pureSplayDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pureSplayDisplay.SelectOrientationVectors = 'vectors'
pureSplayDisplay.ScaleFactor = 1.2000000000000002
pureSplayDisplay.SelectScaleArray = 'Pure Splay'
pureSplayDisplay.GlyphType = 'Arrow'
pureSplayDisplay.GlyphTableIndexArray = 'Pure Splay'
pureSplayDisplay.GaussianRadius = 0.06
pureSplayDisplay.SetScaleArray = [None, '']
pureSplayDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pureSplayDisplay.OpacityArray = [None, '']
pureSplayDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pureSplayDisplay.DataAxesGrid = 'GridAxesRepresentation'
pureSplayDisplay.PolarAxes = 'PolarAxesRepresentation'
pureSplayDisplay.ScalarOpacityFunction = pureSplayPWF
pureSplayDisplay.ScalarOpacityUnitDistance = 0.6088735100241448
pureSplayDisplay.OpacityArrayName = ['CELLS', 'Pure Splay']
pureSplayDisplay.SelectInputVectors = [None, '']
pureSplayDisplay.WriteLog = ''

# show color bar/color legend
pureSplayDisplay.SetScalarBarVisibility(renderView1, True)

# find source
pureBend = FindSource('Pure Bend')

# set active source
SetActiveSource(pureBend)

# show data in view
pureBendDisplay = Show(pureBend, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'PureBend'
pureBendTF2D = GetTransferFunction2D('PureBend')
pureBendTF2D.ScalarRangeInitialized = 1
pureBendTF2D.Range = [0.0, 2.0, 0.0, 1.0]

# get color transfer function/color map for 'PureBend'
pureBendLUT = GetColorTransferFunction('PureBend')
pureBendLUT.TransferFunction2D = pureBendTF2D
pureBendLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
pureBendLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'PureBend'
pureBendPWF = GetOpacityTransferFunction('PureBend')
pureBendPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
pureBendPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pureBendDisplay.Representation = 'Surface'
pureBendDisplay.ColorArrayName = ['CELLS', 'Pure Bend']
pureBendDisplay.LookupTable = pureBendLUT
pureBendDisplay.SelectTCoordArray = 'None'
pureBendDisplay.SelectNormalArray = 'None'
pureBendDisplay.SelectTangentArray = 'None'
pureBendDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pureBendDisplay.SelectOrientationVectors = 'vectors'
pureBendDisplay.ScaleFactor = 1.2000000000000002
pureBendDisplay.SelectScaleArray = 'Pure Bend'
pureBendDisplay.GlyphType = 'Arrow'
pureBendDisplay.GlyphTableIndexArray = 'Pure Bend'
pureBendDisplay.GaussianRadius = 0.06
pureBendDisplay.SetScaleArray = [None, '']
pureBendDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pureBendDisplay.OpacityArray = [None, '']
pureBendDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pureBendDisplay.DataAxesGrid = 'GridAxesRepresentation'
pureBendDisplay.PolarAxes = 'PolarAxesRepresentation'
pureBendDisplay.ScalarOpacityFunction = pureBendPWF
pureBendDisplay.ScalarOpacityUnitDistance = 0.6088735100241448
pureBendDisplay.OpacityArrayName = ['CELLS', 'Pure Bend']
pureBendDisplay.SelectInputVectors = [None, '']
pureBendDisplay.WriteLog = ''

# show color bar/color legend
pureBendDisplay.SetScalarBarVisibility(renderView1, True)

# find source
pureTwist = FindSource('Pure Twist')

# set active source
SetActiveSource(pureTwist)

# show data in view
pureTwistDisplay = Show(pureTwist, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'PureTwist'
pureTwistTF2D = GetTransferFunction2D('PureTwist')
pureTwistTF2D.ScalarRangeInitialized = 1
pureTwistTF2D.Range = [0.0, 2.0, 0.0, 1.0]

# get color transfer function/color map for 'PureTwist'
pureTwistLUT = GetColorTransferFunction('PureTwist')
pureTwistLUT.TransferFunction2D = pureTwistTF2D
pureTwistLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0000000000000002, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
pureTwistLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'PureTwist'
pureTwistPWF = GetOpacityTransferFunction('PureTwist')
pureTwistPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
pureTwistPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
pureTwistDisplay.Representation = 'Surface'
pureTwistDisplay.ColorArrayName = ['CELLS', 'Pure Twist']
pureTwistDisplay.LookupTable = pureTwistLUT
pureTwistDisplay.SelectTCoordArray = 'None'
pureTwistDisplay.SelectNormalArray = 'None'
pureTwistDisplay.SelectTangentArray = 'None'
pureTwistDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pureTwistDisplay.SelectOrientationVectors = 'vectors'
pureTwistDisplay.ScaleFactor = 1.2000000000000002
pureTwistDisplay.SelectScaleArray = 'Pure Twist'
pureTwistDisplay.GlyphType = 'Arrow'
pureTwistDisplay.GlyphTableIndexArray = 'Pure Twist'
pureTwistDisplay.GaussianRadius = 0.06
pureTwistDisplay.SetScaleArray = [None, '']
pureTwistDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pureTwistDisplay.OpacityArray = [None, '']
pureTwistDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pureTwistDisplay.DataAxesGrid = 'GridAxesRepresentation'
pureTwistDisplay.PolarAxes = 'PolarAxesRepresentation'
pureTwistDisplay.ScalarOpacityFunction = pureTwistPWF
pureTwistDisplay.ScalarOpacityUnitDistance = 0.6088735100241448
pureTwistDisplay.OpacityArrayName = ['CELLS', 'Pure Twist']
pureTwistDisplay.SelectInputVectors = [None, '']
pureTwistDisplay.WriteLog = ''

# show color bar/color legend
pureTwistDisplay.SetScalarBarVisibility(renderView1, True)

# find source
tilt = FindSource('Tilt')

# set active source
SetActiveSource(tilt)

# show data in view
tiltDisplay = Show(tilt, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'Tilt'
tiltTF2D = GetTransferFunction2D('Tilt')
tiltTF2D.ScalarRangeInitialized = 1
tiltTF2D.Range = [0.0, 2.0, 0.0, 1.0]

# get color transfer function/color map for 'Tilt'
tiltLUT = GetColorTransferFunction('Tilt')
tiltLUT.TransferFunction2D = tiltTF2D
tiltLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 1.0000000000000002, 0.865003, 0.865003, 0.865003, 2.0, 0.705882, 0.0156863, 0.14902]
tiltLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Tilt'
tiltPWF = GetOpacityTransferFunction('Tilt')
tiltPWF.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]
tiltPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tiltDisplay.Representation = 'Surface'
tiltDisplay.ColorArrayName = ['CELLS', 'Tilt']
tiltDisplay.LookupTable = tiltLUT
tiltDisplay.SelectTCoordArray = 'None'
tiltDisplay.SelectNormalArray = 'None'
tiltDisplay.SelectTangentArray = 'None'
tiltDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
tiltDisplay.SelectOrientationVectors = 'vectors'
tiltDisplay.ScaleFactor = 1.2000000000000002
tiltDisplay.SelectScaleArray = 'Tilt'
tiltDisplay.GlyphType = 'Arrow'
tiltDisplay.GlyphTableIndexArray = 'Tilt'
tiltDisplay.GaussianRadius = 0.06
tiltDisplay.SetScaleArray = [None, '']
tiltDisplay.ScaleTransferFunction = 'PiecewiseFunction'
tiltDisplay.OpacityArray = [None, '']
tiltDisplay.OpacityTransferFunction = 'PiecewiseFunction'
tiltDisplay.DataAxesGrid = 'GridAxesRepresentation'
tiltDisplay.PolarAxes = 'PolarAxesRepresentation'
tiltDisplay.ScalarOpacityFunction = tiltPWF
tiltDisplay.ScalarOpacityUnitDistance = 0.6088735100241448
tiltDisplay.OpacityArrayName = ['CELLS', 'Tilt']
tiltDisplay.SelectInputVectors = [None, '']
tiltDisplay.WriteLog = ''

# show color bar/color legend
tiltDisplay.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(pureSplay)

# Properties modified on pureSplayDisplay
pureSplayDisplay.Position = [0.0, -10.0, 0.0]

# Properties modified on pureSplayDisplay.DataAxesGrid
pureSplayDisplay.DataAxesGrid.Position = [0.0, -10.0, 0.0]

# Properties modified on pureSplayDisplay.PolarAxes
pureSplayDisplay.PolarAxes.Translation = [0.0, -10.0, 0.0]

# set active source
SetActiveSource(pureBend)

# Properties modified on pureBendDisplay
pureBendDisplay.Position = [0.0, -15.0, 0.0]

# Properties modified on pureBendDisplay.DataAxesGrid
pureBendDisplay.DataAxesGrid.Position = [0.0, -15.0, 0.0]

# Properties modified on pureBendDisplay.PolarAxes
pureBendDisplay.PolarAxes.Translation = [0.0, -15.0, 0.0]

# set active source
SetActiveSource(pureTwist)

# Properties modified on pureTwistDisplay
pureTwistDisplay.Position = [0.0, 20.0, 0.0]

# Properties modified on pureTwistDisplay.DataAxesGrid
pureTwistDisplay.DataAxesGrid.Position = [0.0, 20.0, 0.0]

# Properties modified on pureTwistDisplay.PolarAxes
pureTwistDisplay.PolarAxes.Translation = [0.0, 20.0, 0.0]

# Properties modified on pureTwistDisplay
pureTwistDisplay.Position = [0.0, -20.0, 0.0]

# Properties modified on pureTwistDisplay.DataAxesGrid
pureTwistDisplay.DataAxesGrid.Position = [0.0, -20.0, 0.0]

# Properties modified on pureTwistDisplay.PolarAxes
pureTwistDisplay.PolarAxes.Translation = [0.0, -20.0, 0.0]

# set active source
SetActiveSource(tilt)

# Properties modified on tiltDisplay
tiltDisplay.Position = [0.0, -25.0, 0.0]

# Properties modified on tiltDisplay.DataAxesGrid
tiltDisplay.DataAxesGrid.Position = [0.0, -25.0, 0.0]

# Properties modified on tiltDisplay.PolarAxes
tiltDisplay.PolarAxes.Translation = [0.0, -25.0, 0.0]

# get 2D transfer function for 'vectors'
vectorsTF2D = GetTransferFunction2D('vectors')

# get color transfer function/color map for 'vectors'
vectorsLUT = GetColorTransferFunction('vectors')
vectorsLUT.TransferFunction2D = vectorsTF2D
vectorsLUT.RGBPoints = [-1.0, 0.231373, 0.298039, 0.752941, 8.127676309754861e-11, 0.865003, 0.865003, 0.865003, 1.0, 0.705882, 0.0156863, 0.14902]
vectorsLUT.ScalarRangeInitialized = 1.0
vectorsLUT.VectorComponent = 2
vectorsLUT.VectorMode = 'Component'

# get color legend/bar for vectorsLUT in view renderView1
vectorsLUTColorBar = GetScalarBar(vectorsLUT, renderView1)
vectorsLUTColorBar.Orientation = 'Horizontal'
vectorsLUTColorBar.WindowLocation = 'Any Location'
vectorsLUTColorBar.Position = [0.06884020618556694, 0.8064631043256998]
vectorsLUTColorBar.Title = 'vectors'
vectorsLUTColorBar.ComponentTitle = 'Z'
vectorsLUTColorBar.ScalarBarLength = 0.33000000000000007

# change scalar bar placement
vectorsLUTColorBar.Position = [0.14293814432989685, 0.836997455470738]

# get color legend/bar for pureBendLUT in view renderView1
pureBendLUTColorBar = GetScalarBar(pureBendLUT, renderView1)
pureBendLUTColorBar.WindowLocation = 'Upper Left Corner'
pureBendLUTColorBar.Title = 'Pure Bend'
pureBendLUTColorBar.ComponentTitle = ''

# change scalar bar placement
pureBendLUTColorBar.Orientation = 'Horizontal'
pureBendLUTColorBar.WindowLocation = 'Any Location'
pureBendLUTColorBar.Position = [0.18041237113402064, 0.3809414758269719]
pureBendLUTColorBar.ScalarBarLength = 0.33000000000000007

# get color legend/bar for pureSplayLUT in view renderView1
pureSplayLUTColorBar = GetScalarBar(pureSplayLUT, renderView1)
pureSplayLUTColorBar.WindowLocation = 'Upper Right Corner'
pureSplayLUTColorBar.Title = 'Pure Splay'
pureSplayLUTColorBar.ComponentTitle = ''

# change scalar bar placement
pureSplayLUTColorBar.Orientation = 'Horizontal'
pureSplayLUTColorBar.WindowLocation = 'Any Location'
pureSplayLUTColorBar.Position = [0.1867525773195876, 0.5443765903307889]
pureSplayLUTColorBar.ScalarBarLength = 0.3300000000000002

# get color legend/bar for pureTwistLUT in view renderView1
pureTwistLUTColorBar = GetScalarBar(pureTwistLUT, renderView1)
pureTwistLUTColorBar.WindowLocation = 'Lower Left Corner'
pureTwistLUTColorBar.Title = 'Pure Twist'
pureTwistLUTColorBar.ComponentTitle = ''

# change scalar bar placement
pureTwistLUTColorBar.Orientation = 'Horizontal'
pureTwistLUTColorBar.WindowLocation = 'Any Location'
pureTwistLUTColorBar.Position = [0.18353092783505126, 0.2072264631043257]
pureTwistLUTColorBar.ScalarBarLength = 0.33000000000000046

# get color legend/bar for totalEnergyDensityLUT in view renderView1
totalEnergyDensityLUTColorBar = GetScalarBar(totalEnergyDensityLUT, renderView1)
totalEnergyDensityLUTColorBar.Title = 'Total Energy Density'
totalEnergyDensityLUTColorBar.ComponentTitle = ''

# change scalar bar placement
totalEnergyDensityLUTColorBar.Orientation = 'Horizontal'
totalEnergyDensityLUTColorBar.WindowLocation = 'Any Location'
totalEnergyDensityLUTColorBar.Position = [0.1861082474226804, 0.6792366412213741]
totalEnergyDensityLUTColorBar.ScalarBarLength = 0.3300000000000002

# change scalar bar placement
vectorsLUTColorBar.Position = [0.18610824742268037, 0.8471755725190842]
vectorsLUTColorBar.ScalarBarLength = 0.32999999999999996

# get color legend/bar for tiltLUT in view renderView1
tiltLUTColorBar = GetScalarBar(tiltLUT, renderView1)
tiltLUTColorBar.Title = 'Tilt'
tiltLUTColorBar.ComponentTitle = ''

# change scalar bar placement
tiltLUTColorBar.Orientation = 'Horizontal'
tiltLUTColorBar.WindowLocation = 'Any Location'
tiltLUTColorBar.Position = [0.1841752577319588, 0.04310432569974548]
tiltLUTColorBar.ScalarBarLength = 0.3300000000000001

# find source
poreEq000vtk = FindSource('PoreEq00#0.vtk*')

# set active source
SetActiveSource(poreEq000vtk)

# get opacity transfer function/opacity map for 'vectors'
vectorsPWF = GetOpacityTransferFunction('vectors')
vectorsPWF.Points = [-1.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
vectorsPWF.ScalarRangeInitialized = 1

# get display properties
poreEq000vtkDisplay = GetDisplayProperties(poreEq000vtk, view=renderView1)

# set active source
SetActiveSource(totalEnergyDensity)

# set active source
SetActiveSource(pureSplay)

# set active source
SetActiveSource(pureBend)

# set active source
SetActiveSource(pureTwist)

# set active source
SetActiveSource(tilt)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1552, 786)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [-11.895443494627239, -11.78310795174972, 24.43620529482883]
renderView1.CameraFocalPoint = [-11.895443494627239, -11.78310795174972, 0.0]
renderView1.CameraParallelScale = 16.404267675608818

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).