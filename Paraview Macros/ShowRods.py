# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
pureCholesteric4n_0vtk = FindSource('PureCholesteric4n_0.vtk*')

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=pureCholesteric4n_0vtk,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'vectors']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.7999939918518066
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.GlyphType = 'Cylinder'
glyph1.ScaleFactor = 0.40799693584442137
glyph1.GlyphMode = 'All Points'

# Properties modified on glyph1.GlyphTransform
glyph1.GlyphTransform.Rotate = [0.0, 0.0, 90.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'vectors'
vectorsLUT = GetColorTransferFunction('vectors')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'vectors']
glyph1Display.LookupTable = vectorsLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'Normals'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'Normals'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'vectors'
glyph1Display.ScaleFactor = 0.8289156436920166
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.04144578218460083
glyph1Display.SetScaleArray = ['POINTS', 'Normals']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'Normals']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.SelectInputVectors = ['POINTS', 'vectors']
glyph1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-0.9999993443489075, 0.0, 0.5, 0.0, 0.9999993443489075, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-0.9999993443489075, 0.0, 0.5, 0.0, 0.9999993443489075, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'vectors'
vectorsPWF = GetOpacityTransferFunction('vectors')

# get 2D transfer function for 'vectors'
vectorsTF2D = GetTransferFunction2D('vectors')

# Properties modified on glyph1
glyph1.ScaleFactor = 0.29599777698516844

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1157, 744)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [1.3508454591345445, 1.6777617298853664, 26.799798727035522]
renderView1.CameraFocalPoint = [1.3508454591345445, 1.6777617298853664, 0.0]
renderView1.CameraParallelScale = 6.844742236217586

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).