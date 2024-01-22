# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
poreEq000vtk = FindSource('PoreEq00#0.vtk*')

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(registrationName='ComputeDerivatives1', Input=poreEq000vtk)
computeDerivatives1.Scalars = [None, '']
computeDerivatives1.Vectors = ['POINTS', 'vectors']

# Properties modified on computeDerivatives1
computeDerivatives1.Scalars = ['POINTS', '']
computeDerivatives1.OutputVectorType = 'Nothing'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
computeDerivatives1Display = Show(computeDerivatives1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
computeDerivatives1Display.Representation = 'Surface'
computeDerivatives1Display.ColorArrayName = [None, '']
computeDerivatives1Display.SelectTCoordArray = 'None'
computeDerivatives1Display.SelectNormalArray = 'None'
computeDerivatives1Display.SelectTangentArray = 'None'
computeDerivatives1Display.OSPRayScaleArray = 'vectors'
computeDerivatives1Display.OSPRayScaleFunction = 'PiecewiseFunction'
computeDerivatives1Display.SelectOrientationVectors = 'vectors'
computeDerivatives1Display.ScaleFactor = 1.2000000000000002
computeDerivatives1Display.SelectScaleArray = 'None'
computeDerivatives1Display.GlyphType = 'Arrow'
computeDerivatives1Display.GlyphTableIndexArray = 'None'
computeDerivatives1Display.GaussianRadius = 0.06
computeDerivatives1Display.SetScaleArray = ['POINTS', 'vectors']
computeDerivatives1Display.ScaleTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display.OpacityArray = ['POINTS', 'vectors']
computeDerivatives1Display.OpacityTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display.DataAxesGrid = 'GridAxesRepresentation'
computeDerivatives1Display.PolarAxes = 'PolarAxesRepresentation'
computeDerivatives1Display.ScalarOpacityUnitDistance = 0.4475858941160456
computeDerivatives1Display.OpacityArrayName = ['POINTS', 'vectors']
computeDerivatives1Display.SelectInputVectors = ['POINTS', 'vectors']
computeDerivatives1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
computeDerivatives1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
computeDerivatives1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(poreEq000vtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Extract Cells By Type'
extractCellsByType1 = ExtractCellsByType(registrationName='ExtractCellsByType1', Input=computeDerivatives1)
extractCellsByType1.CellTypes = []

# Properties modified on extractCellsByType1
extractCellsByType1.CellTypes = ['Triangle']

# show data in view
extractCellsByType1Display = Show(extractCellsByType1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractCellsByType1Display.Representation = 'Surface'
extractCellsByType1Display.ColorArrayName = [None, '']
extractCellsByType1Display.SelectTCoordArray = 'None'
extractCellsByType1Display.SelectNormalArray = 'None'
extractCellsByType1Display.SelectTangentArray = 'None'
extractCellsByType1Display.OSPRayScaleArray = 'vectors'
extractCellsByType1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractCellsByType1Display.SelectOrientationVectors = 'vectors'
extractCellsByType1Display.ScaleFactor = 1.2000000000000002
extractCellsByType1Display.SelectScaleArray = 'None'
extractCellsByType1Display.GlyphType = 'Arrow'
extractCellsByType1Display.GlyphTableIndexArray = 'None'
extractCellsByType1Display.GaussianRadius = 0.06
extractCellsByType1Display.SetScaleArray = ['POINTS', 'vectors']
extractCellsByType1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractCellsByType1Display.OpacityArray = ['POINTS', 'vectors']
extractCellsByType1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractCellsByType1Display.DataAxesGrid = 'GridAxesRepresentation'
extractCellsByType1Display.PolarAxes = 'PolarAxesRepresentation'
extractCellsByType1Display.ScalarOpacityUnitDistance = 0.6088735100241448
extractCellsByType1Display.OpacityArrayName = ['POINTS', 'vectors']
extractCellsByType1Display.SelectInputVectors = ['POINTS', 'vectors']
extractCellsByType1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractCellsByType1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractCellsByType1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(computeDerivatives1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=extractCellsByType1)
pointDatatoCellData1.PointDataArraytoprocess = ['vectors']

# show data in view
pointDatatoCellData1Display = Show(pointDatatoCellData1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
pointDatatoCellData1Display.Representation = 'Surface'
pointDatatoCellData1Display.ColorArrayName = [None, '']
pointDatatoCellData1Display.SelectTCoordArray = 'None'
pointDatatoCellData1Display.SelectNormalArray = 'None'
pointDatatoCellData1Display.SelectTangentArray = 'None'
pointDatatoCellData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.SelectOrientationVectors = 'vectors'
pointDatatoCellData1Display.ScaleFactor = 1.2000000000000002
pointDatatoCellData1Display.SelectScaleArray = 'None'
pointDatatoCellData1Display.GlyphType = 'Arrow'
pointDatatoCellData1Display.GlyphTableIndexArray = 'None'
pointDatatoCellData1Display.GaussianRadius = 0.06
pointDatatoCellData1Display.SetScaleArray = [None, '']
pointDatatoCellData1Display.ScaleTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.OpacityArray = [None, '']
pointDatatoCellData1Display.OpacityTransferFunction = 'PiecewiseFunction'
pointDatatoCellData1Display.DataAxesGrid = 'GridAxesRepresentation'
pointDatatoCellData1Display.PolarAxes = 'PolarAxesRepresentation'
pointDatatoCellData1Display.ScalarOpacityUnitDistance = 0.6088735100241448
pointDatatoCellData1Display.OpacityArrayName = ['CELLS', 'VectorGradient']
pointDatatoCellData1Display.SelectInputVectors = [None, '']
pointDatatoCellData1Display.WriteLog = ''

# hide data in view
Hide(extractCellsByType1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1.AttributeType = 'Cell Data'
calculator1.Function = ''

#Grab user input for chiral wavevector

qval = input('Input Chiral Wavevector')

# Properties modified on calculator1
calculator1.ResultArrayName = 'Total Energy Density'
calculator1.Function = '1/2*("VectorGradient_0" + "VectorGradient_4" + "VectorGradient_8")^2 + 1/2*((vectors_Y*("VectorGradient_3" - "VectorGradient_1") - vectors_Z*("VectorGradient_2" - "VectorGradient_6"))^2 + (vectors_Z*("VectorGradient_7" - "VectorGradient_5")-vectors_X*("VectorGradient_3" - "VectorGradient_1"))^2 + (vectors_X*("VectorGradient_2" - "VectorGradient_6") - vectors_Y*("VectorGradient_7" - "VectorGradient_5"))^2) + (vectors_Z*(("VectorGradient_7" - "VectorGradient_5")-("VectorGradient_2" - "VectorGradient_6")))^2) + 1/2*(vectors_X*("VectorGradient_7" - "VectorGradient_5") + vectors_Y*("VectorGradient_2" - "VectorGradient_6") + vectors_Z*("VectorGradient_3" - "VectorGradient_1") - '+str(qval)+')^2 + 1/2*(1 - vectors_Z^2)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'TotalEnergyDensity'
totalEnergyDensityLUT = GetColorTransferFunction('TotalEnergyDensity')

# get opacity transfer function/opacity map for 'TotalEnergyDensity'
totalEnergyDensityPWF = GetOpacityTransferFunction('TotalEnergyDensity')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['CELLS', 'Total Energy Density']
calculator1Display.LookupTable = totalEnergyDensityLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'vectors'
calculator1Display.ScaleFactor = 1.2000000000000002
calculator1Display.SelectScaleArray = 'Total Energy Density'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'Total Energy Density'
calculator1Display.GaussianRadius = 0.06
calculator1Display.SetScaleArray = [None, '']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = [None, '']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = totalEnergyDensityPWF
calculator1Display.ScalarOpacityUnitDistance = 0.6088735100241448
calculator1Display.OpacityArrayName = ['CELLS', 'Total Energy Density']
calculator1Display.SelectInputVectors = [None, '']
calculator1Display.WriteLog = ''

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'TotalEnergyDensity'
totalEnergyDensityTF2D = GetTransferFunction2D('TotalEnergyDensity')

# rename source object
RenameSource('Total Energy Density', calculator1)

# set active source
SetActiveSource(pointDatatoCellData1)

# create a new 'Calculator'
calculator1_1 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1_1.AttributeType = 'Cell Data'
calculator1_1.Function = ''

# Properties modified on calculator1_1
calculator1_1.ResultArrayName = 'Pure Splay'
calculator1_1.Function = '1/2*("VectorGradient_0" + "VectorGradient_4" + "VectorGradient_8")^2'

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'PureSplay'
pureSplayLUT = GetColorTransferFunction('PureSplay')

# get opacity transfer function/opacity map for 'PureSplay'
pureSplayPWF = GetOpacityTransferFunction('PureSplay')

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'
calculator1_1Display.ColorArrayName = ['CELLS', 'Pure Splay']
calculator1_1Display.LookupTable = pureSplayLUT
calculator1_1Display.SelectTCoordArray = 'None'
calculator1_1Display.SelectNormalArray = 'None'
calculator1_1Display.SelectTangentArray = 'None'
calculator1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_1Display.SelectOrientationVectors = 'vectors'
calculator1_1Display.ScaleFactor = 1.2000000000000002
calculator1_1Display.SelectScaleArray = 'Pure Splay'
calculator1_1Display.GlyphType = 'Arrow'
calculator1_1Display.GlyphTableIndexArray = 'Pure Splay'
calculator1_1Display.GaussianRadius = 0.06
calculator1_1Display.SetScaleArray = [None, '']
calculator1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_1Display.OpacityArray = [None, '']
calculator1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_1Display.ScalarOpacityFunction = pureSplayPWF
calculator1_1Display.ScalarOpacityUnitDistance = 0.6088735100241448
calculator1_1Display.OpacityArrayName = ['CELLS', 'Pure Splay']
calculator1_1Display.SelectInputVectors = [None, '']
calculator1_1Display.WriteLog = ''

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'PureSplay'
pureSplayTF2D = GetTransferFunction2D('PureSplay')

# rename source object
RenameSource('Pure Splay', calculator1_1)

# set active source
SetActiveSource(pointDatatoCellData1)

# create a new 'Calculator'
calculator1_2 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1_2.AttributeType = 'Cell Data'
calculator1_2.Function = ''

# Properties modified on calculator1_2
calculator1_2.ResultArrayName = 'Pure Bend'
calculator1_2.Function = '1/2*((vectors_Y*("VectorGradient_3" - "VectorGradient_1") - vectors_Z*("VectorGradient_2" - "VectorGradient_6"))^2 + (vectors_Z*("VectorGradient_7" - "VectorGradient_5")-vectors_X*("VectorGradient_3" - "VectorGradient_1"))^2'

# show data in view
calculator1_2Display = Show(calculator1_2, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'PureBend'
pureBendLUT = GetColorTransferFunction('PureBend')

# get opacity transfer function/opacity map for 'PureBend'
pureBendPWF = GetOpacityTransferFunction('PureBend')

# trace defaults for the display properties.
calculator1_2Display.Representation = 'Surface'
calculator1_2Display.ColorArrayName = ['CELLS', 'Pure Bend']
calculator1_2Display.LookupTable = pureBendLUT
calculator1_2Display.SelectTCoordArray = 'None'
calculator1_2Display.SelectNormalArray = 'None'
calculator1_2Display.SelectTangentArray = 'None'
calculator1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_2Display.SelectOrientationVectors = 'vectors'
calculator1_2Display.ScaleFactor = 1.2000000000000002
calculator1_2Display.SelectScaleArray = 'Pure Bend'
calculator1_2Display.GlyphType = 'Arrow'
calculator1_2Display.GlyphTableIndexArray = 'Pure Bend'
calculator1_2Display.GaussianRadius = 0.06
calculator1_2Display.SetScaleArray = [None, '']
calculator1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_2Display.OpacityArray = [None, '']
calculator1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_2Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_2Display.ScalarOpacityFunction = pureBendPWF
calculator1_2Display.ScalarOpacityUnitDistance = 0.6088735100241448
calculator1_2Display.OpacityArrayName = ['CELLS', 'Pure Bend']
calculator1_2Display.SelectInputVectors = [None, '']
calculator1_2Display.WriteLog = ''

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# show color bar/color legend
calculator1_2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'PureBend'
pureBendTF2D = GetTransferFunction2D('PureBend')

# rename source object
RenameSource('Pure Bend', calculator1_2)

# set active source
SetActiveSource(pointDatatoCellData1)

# create a new 'Calculator'
calculator1_3 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1_3.AttributeType = 'Cell Data'
calculator1_3.Function = ''

# Properties modified on calculator1_3
calculator1_3.ResultArrayName = 'Pure Twist'
calculator1_3.Function = '1/2*(vectors_X*("VectorGradient_7" - "VectorGradient_5") + vectors_Y*("VectorGradient_2" - "VectorGradient_6") + vectors_Z*("VectorGradient_3" - "VectorGradient_1") - '+str(qval)+')^2'

# show data in view
calculator1_3Display = Show(calculator1_3, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'PureTwist'
pureTwistLUT = GetColorTransferFunction('PureTwist')

# get opacity transfer function/opacity map for 'PureTwist'
pureTwistPWF = GetOpacityTransferFunction('PureTwist')

# trace defaults for the display properties.
calculator1_3Display.Representation = 'Surface'
calculator1_3Display.ColorArrayName = ['CELLS', 'Pure Twist']
calculator1_3Display.LookupTable = pureTwistLUT
calculator1_3Display.SelectTCoordArray = 'None'
calculator1_3Display.SelectNormalArray = 'None'
calculator1_3Display.SelectTangentArray = 'None'
calculator1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_3Display.SelectOrientationVectors = 'vectors'
calculator1_3Display.ScaleFactor = 1.2000000000000002
calculator1_3Display.SelectScaleArray = 'Pure Twist'
calculator1_3Display.GlyphType = 'Arrow'
calculator1_3Display.GlyphTableIndexArray = 'Pure Twist'
calculator1_3Display.GaussianRadius = 0.06
calculator1_3Display.SetScaleArray = [None, '']
calculator1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_3Display.OpacityArray = [None, '']
calculator1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_3Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_3Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_3Display.ScalarOpacityFunction = pureTwistPWF
calculator1_3Display.ScalarOpacityUnitDistance = 0.6088735100241448
calculator1_3Display.OpacityArrayName = ['CELLS', 'Pure Twist']
calculator1_3Display.SelectInputVectors = [None, '']
calculator1_3Display.WriteLog = ''

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# show color bar/color legend
calculator1_3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'PureTwist'
pureTwistTF2D = GetTransferFunction2D('PureTwist')

# rename source object
RenameSource('Pure Twist', calculator1_3)

# set active source
SetActiveSource(pointDatatoCellData1)

# create a new 'Calculator'
calculator1_4 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1_4.AttributeType = 'Cell Data'
calculator1_4.Function = ''

# Properties modified on calculator1_4
calculator1_4.ResultArrayName = 'Tilt'
calculator1_4.Function = '1/2*(1 - vectors_Z^2)'

# show data in view
calculator1_4Display = Show(calculator1_4, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Tilt'
tiltLUT = GetColorTransferFunction('Tilt')

# get opacity transfer function/opacity map for 'Tilt'
tiltPWF = GetOpacityTransferFunction('Tilt')

# trace defaults for the display properties.
calculator1_4Display.Representation = 'Surface'
calculator1_4Display.ColorArrayName = ['CELLS', 'Tilt']
calculator1_4Display.LookupTable = tiltLUT
calculator1_4Display.SelectTCoordArray = 'None'
calculator1_4Display.SelectNormalArray = 'None'
calculator1_4Display.SelectTangentArray = 'None'
calculator1_4Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_4Display.SelectOrientationVectors = 'vectors'
calculator1_4Display.ScaleFactor = 1.2000000000000002
calculator1_4Display.SelectScaleArray = 'Tilt'
calculator1_4Display.GlyphType = 'Arrow'
calculator1_4Display.GlyphTableIndexArray = 'Tilt'
calculator1_4Display.GaussianRadius = 0.06
calculator1_4Display.SetScaleArray = [None, '']
calculator1_4Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_4Display.OpacityArray = [None, '']
calculator1_4Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_4Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_4Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_4Display.ScalarOpacityFunction = tiltPWF
calculator1_4Display.ScalarOpacityUnitDistance = 0.6088735100241448
calculator1_4Display.OpacityArrayName = ['CELLS', 'Tilt']
calculator1_4Display.SelectInputVectors = [None, '']
calculator1_4Display.WriteLog = ''

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# show color bar/color legend
calculator1_4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'Tilt'
tiltTF2D = GetTransferFunction2D('Tilt')

# rename source object
RenameSource('Tilt', calculator1_4)

# set active source
SetActiveSource(calculator1)

# set active source
SetActiveSource(pointDatatoCellData1)

# create a new 'Calculator'
calculator1_5 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1_5.AttributeType = 'Cell Data'
calculator1_5.Function = ''

# Properties modified on calculator1_5
calculator1_5.ResultArrayName = 'Nematic'
calculator1_5.Function = '1/2*("VectorGradient_0" + "VectorGradient_4" + "VectorGradient_8")^2 + 1/2*((vectors_Y*("VectorGradient_3" - "VectorGradient_1") - vectors_Z*("VectorGradient_2" - "VectorGradient_6"))^2 + (vectors_Z*("VectorGradient_7" - "VectorGradient_5")-vectors_X*("VectorGradient_3" - "VectorGradient_1"))^2+ (vectors_Z*(("VectorGradient_7" - "VectorGradient_5")-("VectorGradient_2" - "VectorGradient_6")))^2) + 1/2*(vectors_X*("VectorGradient_7" - "VectorGradient_5") + vectors_Y*("VectorGradient_2" - "VectorGradient_6") + vectors_Z*("VectorGradient_3" - "VectorGradient_1") - '+ str(qval)+')^2'

# show data in view
calculator1_5Display = Show(calculator1_5, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Nematic'
nematicLUT = GetColorTransferFunction('Nematic')

# get opacity transfer function/opacity map for 'Nematic'
nematicPWF = GetOpacityTransferFunction('Nematic')

# trace defaults for the display properties.
calculator1_5Display.Representation = 'Surface'
calculator1_5Display.ColorArrayName = ['CELLS', 'Nematic']
calculator1_5Display.LookupTable = nematicLUT
calculator1_5Display.SelectTCoordArray = 'None'
calculator1_5Display.SelectNormalArray = 'None'
calculator1_5Display.SelectTangentArray = 'None'
calculator1_5Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1_5Display.SelectOrientationVectors = 'vectors'
calculator1_5Display.ScaleFactor = 1.2000000000000002
calculator1_5Display.SelectScaleArray = 'Nematic'
calculator1_5Display.GlyphType = 'Arrow'
calculator1_5Display.GlyphTableIndexArray = 'Nematic'
calculator1_5Display.GaussianRadius = 0.06
calculator1_5Display.SetScaleArray = [None, '']
calculator1_5Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1_5Display.OpacityArray = [None, '']
calculator1_5Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1_5Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1_5Display.PolarAxes = 'PolarAxesRepresentation'
calculator1_5Display.ScalarOpacityFunction = nematicPWF
calculator1_5Display.ScalarOpacityUnitDistance = 0.6088735100241448
calculator1_5Display.OpacityArrayName = ['CELLS', 'Nematic']
calculator1_5Display.SelectInputVectors = [None, '']
calculator1_5Display.WriteLog = ''

# hide data in view
Hide(pointDatatoCellData1, renderView1)

# show color bar/color legend
calculator1_5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'Nematic'
nematicTF2D = GetTransferFunction2D('Nematic')

# rename source object
RenameSource('Nematic', calculator1_5)

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
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).