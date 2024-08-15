# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

SizeData = [["gamma","p","q","Pore Size"]]
AofRect = 48
gs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
fs = [0.5]
qs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
C = 2
pathp = r'C:\Users\gabey\OneDrive\Desktop\Fall 2023\SM Research\Phase Diagram VTK Exports and PP\Single Pore Round 5 no X\VTK Files'
pathexp = r'C:\Users\gabey\OneDrive\Desktop\Fall 2023\SM Research\Phase Diagram VTK Exports and PP\Single Pore Round 5 no X\Snapshots'
for g in gs:
    for f in fs:
        for q in qs:
            pathc = pathp+f"\\q={q} g={g}"
            ldocs = os.listdir(pathc)
            maxiter = 0
            for st in ldocs:
                if "_" in st:
                    st = st.split("_")[1]
                    iter = int(st.replace(".vtk", ""))
                    if iter > maxiter:
                        maxiter = iter

            if g==0.0 or g==1.0 or g==2.0: gg = round(g)
            else: gg=g
            if q==0.0 or q==1.0 or q==2.0: qq = round(q)
            else: qq=q
            if f==0.0 or f==1.0 or f==2.0: ff = round(f)
            else: ff=f
            # create a new 'Legacy VTK Reader'
            DataSet = LegacyVTKReader(registrationName='SinglePore.vtk*', FileNames=[pathc+f'\\SinglePoreg{gg}f{ff}q{qq}C{C}_{maxiter}.vtk'])

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
            SaveScreenshot(pathexp+f"\\SinglePoreg{gg}f{ff}q{qq}C{C}.png", renderView1, ImageResolution=[976, 300])

            # destroy DataSet
            Delete(DataSet)
            del DataSet

            Delete(renderView1)
            del renderView1