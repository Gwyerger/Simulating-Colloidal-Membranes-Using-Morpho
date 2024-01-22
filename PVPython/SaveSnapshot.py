# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

numtimesteps = 50
gcount = 20
qcount = 20


for ii in range(1, gcount+1):
    for jj in range(0, qcount+1):
        
        gg = 5*ii
        qq = 50 + 5*jj
        # create a new 'Legacy VTK Reader'
        DataSet = LegacyVTKReader(registrationName='SinglePoreFixedg'+ str(gg) +'q'+ str(qq) +'.vtk*', FileNames=['C:\\Users\\gabey\\OneDrive\\Desktop\\Fall 2023\\SM Research\\Phase Diagram VTK Exports and PP\\Single Pore Round 2\\VTK\\SinglePoreFixedg'+ str(gg) +'q'+ str(qq) +'_'+str(numtimesteps)+'.vtk'])

        # get active view
        renderView1 = GetActiveViewOrCreate('RenderView')

        # show data in view
        DataSetDisplay = Show(DataSet, renderView1, 'UnstructuredGridRepresentation')

        # trace defaults for the display properties.
        DataSetDisplay.Representation = 'Surface'
        DataSetDisplay.ColorArrayName = [None, '']
        DataSetDisplay.SelectTCoordArray = 'None'
        DataSetDisplay.SelectNormalArray = 'None'
        DataSetDisplay.SelectTangentArray = 'None'
        DataSetDisplay.OSPRayScaleArray = 'vectors'
        DataSetDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
        DataSetDisplay.SelectOrientationVectors = 'vectors'
        DataSetDisplay.ScaleFactor = 1.2000000000000002
        DataSetDisplay.SelectScaleArray = 'None'
        DataSetDisplay.GlyphType = 'Arrow'
        DataSetDisplay.GlyphTableIndexArray = 'None'
        DataSetDisplay.GaussianRadius = 0.06
        DataSetDisplay.SetScaleArray = ['POINTS', 'vectors']
        DataSetDisplay.ScaleTransferFunction = 'PiecewiseFunction'
        DataSetDisplay.OpacityArray = ['POINTS', 'vectors']
        DataSetDisplay.OpacityTransferFunction = 'PiecewiseFunction'
        DataSetDisplay.DataAxesGrid = 'GridAxesRepresentation'
        DataSetDisplay.PolarAxes = 'PolarAxesRepresentation'
        DataSetDisplay.ScalarOpacityUnitDistance = 0.731620427723986
        DataSetDisplay.OpacityArrayName = ['POINTS', 'vectors']
        DataSetDisplay.SelectInputVectors = ['POINTS', 'vectors']
        DataSetDisplay.WriteLog = ''

        # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
        DataSetDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

        # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
        DataSetDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

        # reset view to fit data
        renderView1.ResetCamera(False)

        #changing interaction mode based on data extents
        renderView1.CameraPosition = [0.0, 0.0, 40.2]
        renderView1.CameraFocalPoint = [0.0, 0.0, 0.0]

        # get the material library
        materialLibrary1 = GetMaterialLibrary()

        # update the view to ensure updated data information
        renderView1.Update()

        # set scalar coloring
        ColorBy(DataSetDisplay, ('POINTS', 'vectors', 'Z'))

        # rescale color and/or opacity maps used to include current data range
        DataSetDisplay.RescaleTransferFunctionToDataRange(True, False)

        # show color bar/color legend
        DataSetDisplay.SetScalarBarVisibility(renderView1, True)

        # get color transfer function/color map for 'vectors'
        vectorsLUT = GetColorTransferFunction('vectors')

        # get opacity transfer function/opacity map for 'vectors'
        vectorsPWF = GetOpacityTransferFunction('vectors')

        # get 2D transfer function for 'vectors'
        vectorsTF2D = GetTransferFunction2D('vectors')

        # get color legend/bar for vectorsLUT in view renderView1
        vectorsLUTColorBar = GetScalarBar(vectorsLUT, renderView1)

        # change scalar bar placement
        vectorsLUTColorBar.WindowLocation = 'Any Location'
        vectorsLUTColorBar.Position = [0.8355263157894737, 0.3346055979643766]
        vectorsLUTColorBar.ScalarBarLength = 0.32999999999999974

        # get layout
        layout1 = GetLayout()

        # layout/tab size in pixels
        layout1.SetSize(1216, 786)

        # current camera placement for renderView1
        renderView1.InteractionMode = '2D'
        renderView1.CameraPosition = [0.08046508041140917, -0.04827904824684549, 40.2]
        renderView1.CameraFocalPoint = [0.08046508041140917, -0.04827904824684549, 0.0]
        renderView1.CameraParallelScale = 6.324555320336759

        # save screenshot
        SaveScreenshot('C:/Users/gabey/OneDrive/Desktop/Fall 2023/SM Research/Phase Diagram VTK Exports and PP/Single Pore Round 2/Final Screenshot/SinglePoreFixedg'+ str(gg) +'q'+ str(qq) +'.png', renderView1, ImageResolution=[1216, 786])

        # destroy DataSet
        Delete(DataSet)
        del DataSet