# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

numtimesteps = 161
gcount = 2
fcount = 2
qcount = 10
path = 'C:/Users/gabey/OneDrive/Desktop/Fall 2023/SM Research/Phase Diagram VTK Exports and PP/Single Pore Round 4 - test pt3/Final Snapshots/'

for ii in range(0, gcount+1):
    for kk in range(0, fcount+1):
        for jj in range(0, qcount+1):
            
            gg = round(0.5 + 0.1*ii, ndigits = 2)
            ff = round(0.6 + 0.1*kk, ndigits = 2)
            qq = round(1 + 0.1*jj, ndigits = 2)
            if jj==0 or jj==10: qq = round(qq)
            # create a new 'Legacy VTK Reader'
            DataSet = LegacyVTKReader(registrationName='SinglePoreg'+ str(ii) +'f'+ str(kk)+'q'+ str(jj) +'.vtk*', FileNames=['C:\\Users\\gabey\\OneDrive\\Desktop\\Fall 2023\\SM Research\\Phase Diagram VTK Exports and PP\\Single Pore Round 4 - test pt3\\VTK Files\\SinglePoreg'+ str(gg) + 'f' + str(ff) + 'q'+ str(qq) +'Final.vtk'])

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

            # get layout
            layout1 = GetLayout()
            
            renderView1.OrientationAxesVisibility = 0

                        # set scalar coloring
            ColorBy(DataSetDisplay, ('POINTS', 'vectors', 'Y'))

            # rescale color and/or opacity maps used to include current data range
            DataSetDisplay.RescaleTransferFunctionToDataRange(True, False)

            # show color bar/color legend
            DataSetDisplay.SetScalarBarVisibility(renderView1, True)

            # get color transfer function/color map for 'vectors'
            vectorsLUT = GetColorTransferFunction('vectors')
            # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
            vectorsLUT.ApplyPreset('Viridis (matplotlib)', True)
            # get opacity transfer function/opacity map for 'vectors'
            vectorsPWF = GetOpacityTransferFunction('vectors')

            # get 2D transfer function for 'vectors'
            vectorsTF2D = GetTransferFunction2D('vectors')

            # hide color bar/color legend
            DataSetDisplay.SetScalarBarVisibility(renderView1, False)

            SetActiveSource(DataSet)

            #Enter preview mode
            layout1.PreviewMode = [976, 300]

            # reset view to fit data
            renderView1.ResetCamera(True)

            # layout/tab size in pixels
            layout1.SetSize(976, 300)

            # current camera placement for renderView1
            renderView1.InteractionMode = '2D'
            renderView1.CameraPosition = [0.0, 0.0, 24.43620529482883]
            renderView1.CameraParallelScale = 2.2018822226357604

            # save screenshot
            SaveScreenshot(path+"SinglePore"+ str(ii) +'f'+str(kk)+'q'+ str(jj) +'.png', renderView1, ImageResolution=[976, 300])

            # destroy DataSet
            Delete(DataSet)
            del DataSet

            Delete(renderView1)
            del renderView1