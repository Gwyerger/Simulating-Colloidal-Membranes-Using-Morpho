# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
source = GetActiveSource()
# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# get display properties
sourceDisplay = GetDisplayProperties(source, view=renderView1)
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# set scalar coloring
ColorBy(sourceDisplay, ('POINTS', 'vectors', 'Y'))

# rescale color and/or opacity maps used to include current data range
sourceDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
sourceDisplay.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'vectors'
vectorsTF2D = GetTransferFunction2D('vectors')

# get color transfer function/color map for 'vectors'
vectorsLUT = GetColorTransferFunction('vectors')
vectorsLUT.TransferFunction2D = vectorsTF2D
vectorsLUT.RGBPoints = [-0.13201500475406647, 0.02, 0.3813, 0.9981, -0.10506226654563627, 0.02000006, 0.424267768, 0.96906969, -0.07810952833720616, 0.02, 0.467233763, 0.940033043, -0.05115679012877604, 0.02, 0.5102, 0.911, -0.02420405192034586, 0.02000006, 0.546401494, 0.872669438, 0.0027486862880843344, 0.02, 0.582600362, 0.83433295, 0.0297014244965145, 0.02, 0.6188, 0.796, 0.056654162704944555, 0.02000006, 0.652535156, 0.749802434, 0.08360690091337475, 0.02, 0.686267004, 0.703599538, 0.11055963912180494, 0.02, 0.72, 0.6574, 0.13751237733023514, 0.02000006, 0.757035456, 0.603735359, 0.16446511553866522, 0.02, 0.794067037, 0.55006613, 0.19141785374709536, 0.02, 0.8311, 0.4964, 0.2183705919555256, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 0.2453233301639557, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, 0.2722760683723858, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 0.29922880658081596, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, 0.32618154478924616, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, 0.3531342829976763, 0.6439, 0.9773, 0.0469, 0.3800870212061065, 0.762401813, 0.984669591, 0.034600153, 0.40703975941453674, 0.880901185, 0.992033407, 0.022299877, 0.43399249762296677, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 0.4609452358313969, 0.999402998, 0.955036376, 0.079066628, 0.48789797403982715, 0.9994, 0.910666223, 0.148134024, 0.5148507122482572, 0.9994, 0.8663, 0.2172, 0.5418034504566874, 0.999269665, 0.818035981, 0.217200652, 0.5687561886651177, 0.999133332, 0.769766184, 0.2172, 0.5957089268735477, 0.999, 0.7215, 0.2172, 0.6226616650819778, 0.99913633, 0.673435546, 0.217200652, 0.649614403290408, 0.999266668, 0.625366186, 0.2172, 0.6765671414988381, 0.9994, 0.5773, 0.2172, 0.7035198797072684, 0.999402998, 0.521068455, 0.217200652, 0.7304726179156984, 0.9994, 0.464832771, 0.2172, 0.7574253561241286, 0.9994, 0.4086, 0.2172, 0.7843780943325588, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 0.8113308325409889, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 0.8382835707494191, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 0.8652363089578491, 0.949903037, 0.116867171, 0.252900603, 0.8921890471662794, 0.903199533, 0.078432949, 0.291800389, 0.9191417853747095, 0.8565, 0.04, 0.3307, 0.94609452358314, 0.798902627, 0.04333345, 0.358434298, 0.9730472617915698, 0.741299424, 0.0466667, 0.386166944, 1.0, 0.6837, 0.05, 0.4139]
vectorsLUT.ColorSpace = 'RGB'
vectorsLUT.NanColor = [1.0, 0.0, 0.0]
vectorsLUT.ScalarRangeInitialized = 1.0
vectorsLUT.VectorComponent = 1
vectorsLUT.VectorMode = 'Component'

# get opacity transfer function/opacity map for 'vectors'
vectorsPWF = GetOpacityTransferFunction('vectors')
vectorsPWF.Points = [-0.13201500475406647, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
vectorsPWF.ScalarRangeInitialized = 1
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# change representation type
sourceDisplay.SetRepresentationType('3D Glyphs')
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# Properties modified on sourceDisplay
sourceDisplay.Orient = 1
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# Properties modified on sourceDisplay
sourceDisplay.Scaling = 1
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# Properties modified on sourceDisplay
sourceDisplay.ScaleFactor = 0.38400000000000006
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=sourceDisplay.GlyphType)
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# Properties modified on sourceDisplay
sourceDisplay.GlyphType = 'Line'
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=sourceDisplay.GlyphType)
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# get the material library
materialLibrary1 = GetMaterialLibrary()
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

# Properties modified on sourceDisplay.DataAxesGrid
sourceDisplay.DataAxesGrid.GridAxesVisibility = 1
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759
# Adjust camera

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.0, 40.2]
renderView1.CameraParallelScale = 6.324555320336759

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1216, 786)

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