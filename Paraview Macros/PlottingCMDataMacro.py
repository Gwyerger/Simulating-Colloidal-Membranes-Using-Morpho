# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
collMemb0vtk = FindSource('CollMemb#0.vtk*')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=collMemb0vtk)
calculator1.AttributeType = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'Result'
calculator1.Function = ''
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0
calculator1.ResultArrayType = 'Double'

# Properties modified on calculator1
calculator1.ResultArrayName = 'theta'
calculator1.Function = 'atan(sqrt(vectors_Y^2 + vectors_X^2)/vectors_Z)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'theta'
thetaTF2D = GetTransferFunction2D('theta')
thetaTF2D.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
thetaTF2D.Boxes = []
thetaTF2D.ScalarRangeInitialized = 0
thetaTF2D.Range = [0.0, 1.0, 0.0, 1.0]
thetaTF2D.OutputDimensions = [10, 10]

# get color transfer function/color map for 'theta'
thetaLUT = GetColorTransferFunction('theta')
thetaLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
thetaLUT.InterpretValuesAsCategories = 0
thetaLUT.AnnotationsInitialized = 0
thetaLUT.ShowCategoricalColorsinDataRangeOnly = 0
thetaLUT.RescaleOnVisibilityChange = 0
thetaLUT.EnableOpacityMapping = 0
thetaLUT.TransferFunction2D = thetaTF2D
thetaLUT.Use2DTransferFunction = 0
thetaLUT.RGBPoints = [0.0005354736052027345, 0.231373, 0.298039, 0.752941, 0.3671026821061493, 0.865003, 0.865003, 0.865003, 0.733669890607096, 0.705882, 0.0156863, 0.14902]
thetaLUT.UseLogScale = 0
thetaLUT.UseOpacityControlPointsFreehandDrawing = 0
thetaLUT.ShowDataHistogram = 0
thetaLUT.AutomaticDataHistogramComputation = 0
thetaLUT.DataHistogramNumberOfBins = 10
thetaLUT.ColorSpace = 'Diverging'
thetaLUT.UseBelowRangeColor = 0
thetaLUT.BelowRangeColor = [0.0, 0.0, 0.0]
thetaLUT.UseAboveRangeColor = 0
thetaLUT.AboveRangeColor = [0.5, 0.5, 0.5]
thetaLUT.NanColor = [1.0, 1.0, 0.0]
thetaLUT.NanOpacity = 1.0
thetaLUT.Discretize = 1
thetaLUT.NumberOfTableValues = 256
thetaLUT.ScalarRangeInitialized = 1.0
thetaLUT.HSVWrap = 0
thetaLUT.VectorComponent = 0
thetaLUT.VectorMode = 'Magnitude'
thetaLUT.AllowDuplicateScalars = 1
thetaLUT.Annotations = []
thetaLUT.ActiveAnnotatedValues = []
thetaLUT.IndexedColors = []
thetaLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'theta'
thetaPWF = GetOpacityTransferFunction('theta')
thetaPWF.Points = [0.0005354736052027345, 0.0, 0.5, 0.0, 0.733669890607096, 1.0, 0.5, 0.0]
thetaPWF.AllowDuplicateScalars = 1
thetaPWF.UseLogScale = 0
thetaPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Selection = None
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'theta']
calculator1Display.LookupTable = thetaLUT
calculator1Display.MapScalars = 1
calculator1Display.MultiComponentsMapping = 0
calculator1Display.InterpolateScalarsBeforeMapping = 1
calculator1Display.Opacity = 1.0
calculator1Display.PointSize = 2.0
calculator1Display.LineWidth = 1.0
calculator1Display.RenderLinesAsTubes = 0
calculator1Display.RenderPointsAsSpheres = 0
calculator1Display.Interpolation = 'Gouraud'
calculator1Display.Specular = 0.0
calculator1Display.SpecularColor = [1.0, 1.0, 1.0]
calculator1Display.SpecularPower = 100.0
calculator1Display.Luminosity = 0.0
calculator1Display.Ambient = 0.0
calculator1Display.Diffuse = 1.0
calculator1Display.Roughness = 0.3
calculator1Display.Metallic = 0.0
calculator1Display.EdgeTint = [1.0, 1.0, 1.0]
calculator1Display.Anisotropy = 0.0
calculator1Display.AnisotropyRotation = 0.0
calculator1Display.BaseIOR = 1.5
calculator1Display.CoatStrength = 0.0
calculator1Display.CoatIOR = 2.0
calculator1Display.CoatRoughness = 0.0
calculator1Display.CoatColor = [1.0, 1.0, 1.0]
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.Texture = None
calculator1Display.RepeatTextures = 1
calculator1Display.InterpolateTextures = 0
calculator1Display.SeamlessU = 0
calculator1Display.SeamlessV = 0
calculator1Display.UseMipmapTextures = 0
calculator1Display.ShowTexturesOnBackface = 1
calculator1Display.BaseColorTexture = None
calculator1Display.NormalTexture = None
calculator1Display.NormalScale = 1.0
calculator1Display.CoatNormalTexture = None
calculator1Display.CoatNormalScale = 1.0
calculator1Display.MaterialTexture = None
calculator1Display.OcclusionStrength = 1.0
calculator1Display.AnisotropyTexture = None
calculator1Display.EmissiveTexture = None
calculator1Display.EmissiveFactor = [1.0, 1.0, 1.0]
calculator1Display.FlipTextures = 0
calculator1Display.BackfaceRepresentation = 'Follow Frontface'
calculator1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
calculator1Display.BackfaceOpacity = 1.0
calculator1Display.Position = [0.0, 0.0, 0.0]
calculator1Display.Scale = [1.0, 1.0, 1.0]
calculator1Display.Orientation = [0.0, 0.0, 0.0]
calculator1Display.Origin = [0.0, 0.0, 0.0]
calculator1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
calculator1Display.Pickable = 1
calculator1Display.Triangulate = 0
calculator1Display.UseShaderReplacements = 0
calculator1Display.ShaderReplacements = ''
calculator1Display.NonlinearSubdivisionLevel = 1
calculator1Display.UseDataPartitions = 0
calculator1Display.OSPRayUseScaleArray = 'All Approximate'
calculator1Display.OSPRayScaleArray = 'theta'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.OSPRayMaterial = 'None'
calculator1Display.BlockSelectors = ['/']
calculator1Display.BlockColors = []
calculator1Display.BlockOpacities = []
calculator1Display.Orient = 0
calculator1Display.OrientationMode = 'Direction'
calculator1Display.SelectOrientationVectors = 'vectors'
calculator1Display.Scaling = 0
calculator1Display.ScaleMode = 'No Data Scaling Off'
calculator1Display.ScaleFactor = 0.19999940395355226
calculator1Display.SelectScaleArray = 'theta'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.UseGlyphTable = 0
calculator1Display.GlyphTableIndexArray = 'theta'
calculator1Display.UseCompositeGlyphTable = 0
calculator1Display.UseGlyphCullingAndLOD = 0
calculator1Display.LODValues = []
calculator1Display.ColorByLODIndex = 0
calculator1Display.GaussianRadius = 0.009999970197677613
calculator1Display.ShaderPreset = 'Sphere'
calculator1Display.CustomTriangleScale = 3
calculator1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
calculator1Display.Emissive = 0
calculator1Display.ScaleByArray = 0
calculator1Display.SetScaleArray = ['POINTS', 'theta']
calculator1Display.ScaleArrayComponent = ''
calculator1Display.UseScaleFunction = 1
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityByArray = 0
calculator1Display.OpacityArray = ['POINTS', 'theta']
calculator1Display.OpacityArrayComponent = ''
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelBold = 0
calculator1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
calculator1Display.SelectionCellLabelFontFamily = 'Arial'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionCellLabelFontSize = 18
calculator1Display.SelectionCellLabelItalic = 0
calculator1Display.SelectionCellLabelJustification = 'Left'
calculator1Display.SelectionCellLabelOpacity = 1.0
calculator1Display.SelectionCellLabelShadow = 0
calculator1Display.SelectionPointLabelBold = 0
calculator1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
calculator1Display.SelectionPointLabelFontFamily = 'Arial'
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.SelectionPointLabelFontSize = 18
calculator1Display.SelectionPointLabelItalic = 0
calculator1Display.SelectionPointLabelJustification = 'Left'
calculator1Display.SelectionPointLabelOpacity = 1.0
calculator1Display.SelectionPointLabelShadow = 0
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = thetaPWF
calculator1Display.ScalarOpacityUnitDistance = 0.2523470244634752
calculator1Display.UseSeparateOpacityArray = 0
calculator1Display.OpacityArrayName = ['POINTS', 'theta']
calculator1Display.OpacityComponent = ''
calculator1Display.SelectMapper = 'Projected tetra'
calculator1Display.SamplingDimensions = [128, 128, 128]
calculator1Display.UseFloatingPointFrameBuffer = 1
calculator1Display.SelectInputVectors = ['POINTS', 'vectors']
calculator1Display.NumberOfSteps = 40
calculator1Display.StepSize = 0.25
calculator1Display.NormalizeVectors = 1
calculator1Display.EnhancedLIC = 1
calculator1Display.ColorMode = 'Blend'
calculator1Display.LICIntensity = 0.8
calculator1Display.MapModeBias = 0.0
calculator1Display.EnhanceContrast = 'Off'
calculator1Display.LowLICContrastEnhancementFactor = 0.0
calculator1Display.HighLICContrastEnhancementFactor = 0.0
calculator1Display.LowColorContrastEnhancementFactor = 0.0
calculator1Display.HighColorContrastEnhancementFactor = 0.0
calculator1Display.AntiAlias = 0
calculator1Display.MaskOnSurface = 1
calculator1Display.MaskThreshold = 0.0
calculator1Display.MaskIntensity = 0.0
calculator1Display.MaskColor = [0.5, 0.5, 0.5]
calculator1Display.GenerateNoiseTexture = 0
calculator1Display.NoiseType = 'Gaussian'
calculator1Display.NoiseTextureSize = 128
calculator1Display.NoiseGrainSize = 2
calculator1Display.MinNoiseValue = 0.0
calculator1Display.MaxNoiseValue = 0.8
calculator1Display.NumberOfNoiseLevels = 1024
calculator1Display.ImpulseNoiseProbability = 1.0
calculator1Display.ImpulseNoiseBackgroundValue = 0.0
calculator1Display.NoiseGeneratorSeed = 1
calculator1Display.CompositeStrategy = 'AUTO'
calculator1Display.UseLICForLOD = 0
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
calculator1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
calculator1Display.GlyphType.TipResolution = 6
calculator1Display.GlyphType.TipRadius = 0.1
calculator1Display.GlyphType.TipLength = 0.35
calculator1Display.GlyphType.ShaftResolution = 6
calculator1Display.GlyphType.ShaftRadius = 0.03
calculator1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0005354736052027345, 0.0, 0.5, 0.0, 0.733669890607096, 1.0, 0.5, 0.0]
calculator1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0005354736052027345, 0.0, 0.5, 0.0, 0.733669890607096, 1.0, 0.5, 0.0]
calculator1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitle = 'X Axis'
calculator1Display.DataAxesGrid.YTitle = 'Y Axis'
calculator1Display.DataAxesGrid.ZTitle = 'Z Axis'
calculator1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.XTitleBold = 0
calculator1Display.DataAxesGrid.XTitleItalic = 0
calculator1Display.DataAxesGrid.XTitleFontSize = 12
calculator1Display.DataAxesGrid.XTitleShadow = 0
calculator1Display.DataAxesGrid.XTitleOpacity = 1.0
calculator1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleBold = 0
calculator1Display.DataAxesGrid.YTitleItalic = 0
calculator1Display.DataAxesGrid.YTitleFontSize = 12
calculator1Display.DataAxesGrid.YTitleShadow = 0
calculator1Display.DataAxesGrid.YTitleOpacity = 1.0
calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleBold = 0
calculator1Display.DataAxesGrid.ZTitleItalic = 0
calculator1Display.DataAxesGrid.ZTitleFontSize = 12
calculator1Display.DataAxesGrid.ZTitleShadow = 0
calculator1Display.DataAxesGrid.ZTitleOpacity = 1.0
calculator1Display.DataAxesGrid.FacesToRender = 63
calculator1Display.DataAxesGrid.CullBackface = 0
calculator1Display.DataAxesGrid.CullFrontface = 1
calculator1Display.DataAxesGrid.ShowGrid = 0
calculator1Display.DataAxesGrid.ShowEdges = 1
calculator1Display.DataAxesGrid.ShowTicks = 1
calculator1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
calculator1Display.DataAxesGrid.AxesToLabel = 63
calculator1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.XLabelBold = 0
calculator1Display.DataAxesGrid.XLabelItalic = 0
calculator1Display.DataAxesGrid.XLabelFontSize = 12
calculator1Display.DataAxesGrid.XLabelShadow = 0
calculator1Display.DataAxesGrid.XLabelOpacity = 1.0
calculator1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelBold = 0
calculator1Display.DataAxesGrid.YLabelItalic = 0
calculator1Display.DataAxesGrid.YLabelFontSize = 12
calculator1Display.DataAxesGrid.YLabelShadow = 0
calculator1Display.DataAxesGrid.YLabelOpacity = 1.0
calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelBold = 0
calculator1Display.DataAxesGrid.ZLabelItalic = 0
calculator1Display.DataAxesGrid.ZLabelFontSize = 12
calculator1Display.DataAxesGrid.ZLabelShadow = 0
calculator1Display.DataAxesGrid.ZLabelOpacity = 1.0
calculator1Display.DataAxesGrid.XAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.XAxisPrecision = 2
calculator1Display.DataAxesGrid.XAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.XAxisLabels = []
calculator1Display.DataAxesGrid.YAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.YAxisPrecision = 2
calculator1Display.DataAxesGrid.YAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.YAxisLabels = []
calculator1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.ZAxisPrecision = 2
calculator1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.ZAxisLabels = []
calculator1Display.DataAxesGrid.UseCustomBounds = 0
calculator1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.Visibility = 0
calculator1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
calculator1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
calculator1Display.PolarAxes.EnableCustomRange = 0
calculator1Display.PolarAxes.CustomRange = [0.0, 1.0]
calculator1Display.PolarAxes.PolarAxisVisibility = 1
calculator1Display.PolarAxes.RadialAxesVisibility = 1
calculator1Display.PolarAxes.DrawRadialGridlines = 1
calculator1Display.PolarAxes.PolarArcsVisibility = 1
calculator1Display.PolarAxes.DrawPolarArcsGridlines = 1
calculator1Display.PolarAxes.NumberOfRadialAxes = 0
calculator1Display.PolarAxes.AutoSubdividePolarAxis = 1
calculator1Display.PolarAxes.NumberOfPolarAxis = 0
calculator1Display.PolarAxes.MinimumRadius = 0.0
calculator1Display.PolarAxes.MinimumAngle = 0.0
calculator1Display.PolarAxes.MaximumAngle = 90.0
calculator1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
calculator1Display.PolarAxes.Ratio = 1.0
calculator1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisTitleVisibility = 1
calculator1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
calculator1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
calculator1Display.PolarAxes.PolarLabelVisibility = 1
calculator1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
calculator1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
calculator1Display.PolarAxes.RadialLabelVisibility = 1
calculator1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
calculator1Display.PolarAxes.RadialLabelLocation = 'Bottom'
calculator1Display.PolarAxes.RadialUnitsVisibility = 1
calculator1Display.PolarAxes.ScreenSize = 10.0
calculator1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisTitleBold = 0
calculator1Display.PolarAxes.PolarAxisTitleItalic = 0
calculator1Display.PolarAxes.PolarAxisTitleShadow = 0
calculator1Display.PolarAxes.PolarAxisTitleFontSize = 12
calculator1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelBold = 0
calculator1Display.PolarAxes.PolarAxisLabelItalic = 0
calculator1Display.PolarAxes.PolarAxisLabelShadow = 0
calculator1Display.PolarAxes.PolarAxisLabelFontSize = 12
calculator1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
calculator1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextBold = 0
calculator1Display.PolarAxes.LastRadialAxisTextItalic = 0
calculator1Display.PolarAxes.LastRadialAxisTextShadow = 0
calculator1Display.PolarAxes.LastRadialAxisTextFontSize = 12
calculator1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
calculator1Display.PolarAxes.EnableDistanceLOD = 1
calculator1Display.PolarAxes.DistanceLODThreshold = 0.7
calculator1Display.PolarAxes.EnableViewAngleLOD = 1
calculator1Display.PolarAxes.ViewAngleLODThreshold = 0.7
calculator1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
calculator1Display.PolarAxes.PolarTicksVisibility = 1
calculator1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
calculator1Display.PolarAxes.TickLocation = 'Both'
calculator1Display.PolarAxes.AxisTickVisibility = 1
calculator1Display.PolarAxes.AxisMinorTickVisibility = 0
calculator1Display.PolarAxes.ArcTickVisibility = 1
calculator1Display.PolarAxes.ArcMinorTickVisibility = 0
calculator1Display.PolarAxes.DeltaAngleMajor = 10.0
calculator1Display.PolarAxes.DeltaAngleMinor = 5.0
calculator1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.ArcMajorTickSize = 0.0
calculator1Display.PolarAxes.ArcTickRatioSize = 0.3
calculator1Display.PolarAxes.ArcMajorTickThickness = 1.0
calculator1Display.PolarAxes.ArcTickRatioThickness = 0.5
calculator1Display.PolarAxes.Use2DMode = 0
calculator1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(collMemb0vtk, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName='PlotOverLine1', Input=calculator1)
plotOverLine1.SamplingPattern = 'Sample Uniformly'
plotOverLine1.Resolution = 1000
plotOverLine1.PassPartialArrays = 1
plotOverLine1.PassCellArrays = 0
plotOverLine1.PassPointArrays = 0
plotOverLine1.PassFieldArrays = 1
plotOverLine1.ComputeTolerance = 1
plotOverLine1.Tolerance = 2.220446049250313e-16
plotOverLine1.Point1 = [-0.9999970197677612, -0.9998940229415894, 0.0]
plotOverLine1.Point2 = [0.9999970197677612, 0.9999960064888, 0.0]

rad = float(input("radius of the droplet"))-0.001


# Properties modified on plotOverLine1
plotOverLine1.ComputeTolerance = 0
plotOverLine1.Point1 = [0.0, 0.0, 0.0]
plotOverLine1.Point2 = [rad, 0.0, 0.0]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plotOverLine1Display.Selection = None
plotOverLine1Display.Representation = 'Surface'
plotOverLine1Display.ColorArrayName = ['POINTS', 'theta']
plotOverLine1Display.LookupTable = thetaLUT
plotOverLine1Display.MapScalars = 1
plotOverLine1Display.MultiComponentsMapping = 0
plotOverLine1Display.InterpolateScalarsBeforeMapping = 1
plotOverLine1Display.Opacity = 1.0
plotOverLine1Display.PointSize = 2.0
plotOverLine1Display.LineWidth = 1.0
plotOverLine1Display.RenderLinesAsTubes = 0
plotOverLine1Display.RenderPointsAsSpheres = 0
plotOverLine1Display.Interpolation = 'Gouraud'
plotOverLine1Display.Specular = 0.0
plotOverLine1Display.SpecularColor = [1.0, 1.0, 1.0]
plotOverLine1Display.SpecularPower = 100.0
plotOverLine1Display.Luminosity = 0.0
plotOverLine1Display.Ambient = 0.0
plotOverLine1Display.Diffuse = 1.0
plotOverLine1Display.Roughness = 0.3
plotOverLine1Display.Metallic = 0.0
plotOverLine1Display.EdgeTint = [1.0, 1.0, 1.0]
plotOverLine1Display.Anisotropy = 0.0
plotOverLine1Display.AnisotropyRotation = 0.0
plotOverLine1Display.BaseIOR = 1.5
plotOverLine1Display.CoatStrength = 0.0
plotOverLine1Display.CoatIOR = 2.0
plotOverLine1Display.CoatRoughness = 0.0
plotOverLine1Display.CoatColor = [1.0, 1.0, 1.0]
plotOverLine1Display.SelectTCoordArray = 'None'
plotOverLine1Display.SelectNormalArray = 'None'
plotOverLine1Display.SelectTangentArray = 'None'
plotOverLine1Display.Texture = None
plotOverLine1Display.RepeatTextures = 1
plotOverLine1Display.InterpolateTextures = 0
plotOverLine1Display.SeamlessU = 0
plotOverLine1Display.SeamlessV = 0
plotOverLine1Display.UseMipmapTextures = 0
plotOverLine1Display.ShowTexturesOnBackface = 1
plotOverLine1Display.BaseColorTexture = None
plotOverLine1Display.NormalTexture = None
plotOverLine1Display.NormalScale = 1.0
plotOverLine1Display.CoatNormalTexture = None
plotOverLine1Display.CoatNormalScale = 1.0
plotOverLine1Display.MaterialTexture = None
plotOverLine1Display.OcclusionStrength = 1.0
plotOverLine1Display.AnisotropyTexture = None
plotOverLine1Display.EmissiveTexture = None
plotOverLine1Display.EmissiveFactor = [1.0, 1.0, 1.0]
plotOverLine1Display.FlipTextures = 0
plotOverLine1Display.BackfaceRepresentation = 'Follow Frontface'
plotOverLine1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
plotOverLine1Display.BackfaceOpacity = 1.0
plotOverLine1Display.Position = [0.0, 0.0, 0.0]
plotOverLine1Display.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display.Origin = [0.0, 0.0, 0.0]
plotOverLine1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
plotOverLine1Display.Pickable = 1
plotOverLine1Display.Triangulate = 0
plotOverLine1Display.UseShaderReplacements = 0
plotOverLine1Display.ShaderReplacements = ''
plotOverLine1Display.NonlinearSubdivisionLevel = 1
plotOverLine1Display.UseDataPartitions = 0
plotOverLine1Display.OSPRayUseScaleArray = 'All Approximate'
plotOverLine1Display.OSPRayScaleArray = 'theta'
plotOverLine1Display.OSPRayScaleFunction = 'PiecewiseFunction'
plotOverLine1Display.OSPRayMaterial = 'None'
plotOverLine1Display.BlockSelectors = ['/']
plotOverLine1Display.BlockColors = []
plotOverLine1Display.BlockOpacities = []
plotOverLine1Display.Orient = 0
plotOverLine1Display.OrientationMode = 'Direction'
plotOverLine1Display.SelectOrientationVectors = 'vectors'
plotOverLine1Display.Scaling = 0
plotOverLine1Display.ScaleMode = 'No Data Scaling Off'
plotOverLine1Display.ScaleFactor = 0.09990000128746034
plotOverLine1Display.SelectScaleArray = 'theta'
plotOverLine1Display.GlyphType = 'Arrow'
plotOverLine1Display.UseGlyphTable = 0
plotOverLine1Display.GlyphTableIndexArray = 'theta'
plotOverLine1Display.UseCompositeGlyphTable = 0
plotOverLine1Display.UseGlyphCullingAndLOD = 0
plotOverLine1Display.LODValues = []
plotOverLine1Display.ColorByLODIndex = 0
plotOverLine1Display.GaussianRadius = 0.004995000064373017
plotOverLine1Display.ShaderPreset = 'Sphere'
plotOverLine1Display.CustomTriangleScale = 3
plotOverLine1Display.CustomShader = """ // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
"""
plotOverLine1Display.Emissive = 0
plotOverLine1Display.ScaleByArray = 0
plotOverLine1Display.SetScaleArray = ['POINTS', 'theta']
plotOverLine1Display.ScaleArrayComponent = ''
plotOverLine1Display.UseScaleFunction = 1
plotOverLine1Display.ScaleTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.OpacityByArray = 0
plotOverLine1Display.OpacityArray = ['POINTS', 'theta']
plotOverLine1Display.OpacityArrayComponent = ''
plotOverLine1Display.OpacityTransferFunction = 'PiecewiseFunction'
plotOverLine1Display.DataAxesGrid = 'GridAxesRepresentation'
plotOverLine1Display.SelectionCellLabelBold = 0
plotOverLine1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
plotOverLine1Display.SelectionCellLabelFontFamily = 'Arial'
plotOverLine1Display.SelectionCellLabelFontFile = ''
plotOverLine1Display.SelectionCellLabelFontSize = 18
plotOverLine1Display.SelectionCellLabelItalic = 0
plotOverLine1Display.SelectionCellLabelJustification = 'Left'
plotOverLine1Display.SelectionCellLabelOpacity = 1.0
plotOverLine1Display.SelectionCellLabelShadow = 0
plotOverLine1Display.SelectionPointLabelBold = 0
plotOverLine1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
plotOverLine1Display.SelectionPointLabelFontFamily = 'Arial'
plotOverLine1Display.SelectionPointLabelFontFile = ''
plotOverLine1Display.SelectionPointLabelFontSize = 18
plotOverLine1Display.SelectionPointLabelItalic = 0
plotOverLine1Display.SelectionPointLabelJustification = 'Left'
plotOverLine1Display.SelectionPointLabelOpacity = 1.0
plotOverLine1Display.SelectionPointLabelShadow = 0
plotOverLine1Display.PolarAxes = 'PolarAxesRepresentation'
plotOverLine1Display.SelectInputVectors = ['POINTS', 'vectors']
plotOverLine1Display.NumberOfSteps = 40
plotOverLine1Display.StepSize = 0.25
plotOverLine1Display.NormalizeVectors = 1
plotOverLine1Display.EnhancedLIC = 1
plotOverLine1Display.ColorMode = 'Blend'
plotOverLine1Display.LICIntensity = 0.8
plotOverLine1Display.MapModeBias = 0.0
plotOverLine1Display.EnhanceContrast = 'Off'
plotOverLine1Display.LowLICContrastEnhancementFactor = 0.0
plotOverLine1Display.HighLICContrastEnhancementFactor = 0.0
plotOverLine1Display.LowColorContrastEnhancementFactor = 0.0
plotOverLine1Display.HighColorContrastEnhancementFactor = 0.0
plotOverLine1Display.AntiAlias = 0
plotOverLine1Display.MaskOnSurface = 1
plotOverLine1Display.MaskThreshold = 0.0
plotOverLine1Display.MaskIntensity = 0.0
plotOverLine1Display.MaskColor = [0.5, 0.5, 0.5]
plotOverLine1Display.GenerateNoiseTexture = 0
plotOverLine1Display.NoiseType = 'Gaussian'
plotOverLine1Display.NoiseTextureSize = 128
plotOverLine1Display.NoiseGrainSize = 2
plotOverLine1Display.MinNoiseValue = 0.0
plotOverLine1Display.MaxNoiseValue = 0.8
plotOverLine1Display.NumberOfNoiseLevels = 1024
plotOverLine1Display.ImpulseNoiseProbability = 1.0
plotOverLine1Display.ImpulseNoiseBackgroundValue = 0.0
plotOverLine1Display.NoiseGeneratorSeed = 1
plotOverLine1Display.CompositeStrategy = 'AUTO'
plotOverLine1Display.UseLICForLOD = 0
plotOverLine1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
plotOverLine1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
plotOverLine1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
plotOverLine1Display.GlyphType.TipResolution = 6
plotOverLine1Display.GlyphType.TipRadius = 0.1
plotOverLine1Display.GlyphType.TipLength = 0.35
plotOverLine1Display.GlyphType.ShaftResolution = 6
plotOverLine1Display.GlyphType.ShaftRadius = 0.03
plotOverLine1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
plotOverLine1Display.ScaleTransferFunction.Points = [0.001039576361772849, 0.0, 0.5, 0.0, 0.7285562687607313, 1.0, 0.5, 0.0]
plotOverLine1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
plotOverLine1Display.OpacityTransferFunction.Points = [0.001039576361772849, 0.0, 0.5, 0.0, 0.7285562687607313, 1.0, 0.5, 0.0]
plotOverLine1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
plotOverLine1Display.DataAxesGrid.XTitle = 'X Axis'
plotOverLine1Display.DataAxesGrid.YTitle = 'Y Axis'
plotOverLine1Display.DataAxesGrid.ZTitle = 'Z Axis'
plotOverLine1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.XTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.XTitleBold = 0
plotOverLine1Display.DataAxesGrid.XTitleItalic = 0
plotOverLine1Display.DataAxesGrid.XTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.XTitleShadow = 0
plotOverLine1Display.DataAxesGrid.XTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.YTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.YTitleBold = 0
plotOverLine1Display.DataAxesGrid.YTitleItalic = 0
plotOverLine1Display.DataAxesGrid.YTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.YTitleShadow = 0
plotOverLine1Display.DataAxesGrid.YTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.ZTitleFontFile = ''
plotOverLine1Display.DataAxesGrid.ZTitleBold = 0
plotOverLine1Display.DataAxesGrid.ZTitleItalic = 0
plotOverLine1Display.DataAxesGrid.ZTitleFontSize = 12
plotOverLine1Display.DataAxesGrid.ZTitleShadow = 0
plotOverLine1Display.DataAxesGrid.ZTitleOpacity = 1.0
plotOverLine1Display.DataAxesGrid.FacesToRender = 63
plotOverLine1Display.DataAxesGrid.CullBackface = 0
plotOverLine1Display.DataAxesGrid.CullFrontface = 1
plotOverLine1Display.DataAxesGrid.ShowGrid = 0
plotOverLine1Display.DataAxesGrid.ShowEdges = 1
plotOverLine1Display.DataAxesGrid.ShowTicks = 1
plotOverLine1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
plotOverLine1Display.DataAxesGrid.AxesToLabel = 63
plotOverLine1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.XLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.XLabelBold = 0
plotOverLine1Display.DataAxesGrid.XLabelItalic = 0
plotOverLine1Display.DataAxesGrid.XLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.XLabelShadow = 0
plotOverLine1Display.DataAxesGrid.XLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.YLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.YLabelBold = 0
plotOverLine1Display.DataAxesGrid.YLabelItalic = 0
plotOverLine1Display.DataAxesGrid.YLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.YLabelShadow = 0
plotOverLine1Display.DataAxesGrid.YLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
plotOverLine1Display.DataAxesGrid.ZLabelFontFile = ''
plotOverLine1Display.DataAxesGrid.ZLabelBold = 0
plotOverLine1Display.DataAxesGrid.ZLabelItalic = 0
plotOverLine1Display.DataAxesGrid.ZLabelFontSize = 12
plotOverLine1Display.DataAxesGrid.ZLabelShadow = 0
plotOverLine1Display.DataAxesGrid.ZLabelOpacity = 1.0
plotOverLine1Display.DataAxesGrid.XAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.XAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.XAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.XAxisLabels = []
plotOverLine1Display.DataAxesGrid.YAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.YAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.YAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.YAxisLabels = []
plotOverLine1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
plotOverLine1Display.DataAxesGrid.ZAxisPrecision = 2
plotOverLine1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
plotOverLine1Display.DataAxesGrid.ZAxisLabels = []
plotOverLine1Display.DataAxesGrid.UseCustomBounds = 0
plotOverLine1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
plotOverLine1Display.PolarAxes.Visibility = 0
plotOverLine1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
plotOverLine1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
plotOverLine1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
plotOverLine1Display.PolarAxes.EnableCustomRange = 0
plotOverLine1Display.PolarAxes.CustomRange = [0.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisVisibility = 1
plotOverLine1Display.PolarAxes.RadialAxesVisibility = 1
plotOverLine1Display.PolarAxes.DrawRadialGridlines = 1
plotOverLine1Display.PolarAxes.PolarArcsVisibility = 1
plotOverLine1Display.PolarAxes.DrawPolarArcsGridlines = 1
plotOverLine1Display.PolarAxes.NumberOfRadialAxes = 0
plotOverLine1Display.PolarAxes.AutoSubdividePolarAxis = 1
plotOverLine1Display.PolarAxes.NumberOfPolarAxis = 0
plotOverLine1Display.PolarAxes.MinimumRadius = 0.0
plotOverLine1Display.PolarAxes.MinimumAngle = 0.0
plotOverLine1Display.PolarAxes.MaximumAngle = 90.0
plotOverLine1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
plotOverLine1Display.PolarAxes.Ratio = 1.0
plotOverLine1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
plotOverLine1Display.PolarAxes.PolarAxisTitleVisibility = 1
plotOverLine1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
plotOverLine1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
plotOverLine1Display.PolarAxes.PolarLabelVisibility = 1
plotOverLine1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
plotOverLine1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
plotOverLine1Display.PolarAxes.RadialLabelVisibility = 1
plotOverLine1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
plotOverLine1Display.PolarAxes.RadialLabelLocation = 'Bottom'
plotOverLine1Display.PolarAxes.RadialUnitsVisibility = 1
plotOverLine1Display.PolarAxes.ScreenSize = 10.0
plotOverLine1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
plotOverLine1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.PolarAxisTitleFontFile = ''
plotOverLine1Display.PolarAxes.PolarAxisTitleBold = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleItalic = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleShadow = 0
plotOverLine1Display.PolarAxes.PolarAxisTitleFontSize = 12
plotOverLine1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
plotOverLine1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.PolarAxisLabelFontFile = ''
plotOverLine1Display.PolarAxes.PolarAxisLabelBold = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelItalic = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelShadow = 0
plotOverLine1Display.PolarAxes.PolarAxisLabelFontSize = 12
plotOverLine1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontFile = ''
plotOverLine1Display.PolarAxes.LastRadialAxisTextBold = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextItalic = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextShadow = 0
plotOverLine1Display.PolarAxes.LastRadialAxisTextFontSize = 12
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
plotOverLine1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
plotOverLine1Display.PolarAxes.EnableDistanceLOD = 1
plotOverLine1Display.PolarAxes.DistanceLODThreshold = 0.7
plotOverLine1Display.PolarAxes.EnableViewAngleLOD = 1
plotOverLine1Display.PolarAxes.ViewAngleLODThreshold = 0.7
plotOverLine1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
plotOverLine1Display.PolarAxes.PolarTicksVisibility = 1
plotOverLine1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
plotOverLine1Display.PolarAxes.TickLocation = 'Both'
plotOverLine1Display.PolarAxes.AxisTickVisibility = 1
plotOverLine1Display.PolarAxes.AxisMinorTickVisibility = 0
plotOverLine1Display.PolarAxes.ArcTickVisibility = 1
plotOverLine1Display.PolarAxes.ArcMinorTickVisibility = 0
plotOverLine1Display.PolarAxes.DeltaAngleMajor = 10.0
plotOverLine1Display.PolarAxes.DeltaAngleMinor = 5.0
plotOverLine1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.ArcMajorTickSize = 0.0
plotOverLine1Display.PolarAxes.ArcTickRatioSize = 0.3
plotOverLine1Display.PolarAxes.ArcMajorTickThickness = 1.0
plotOverLine1Display.PolarAxes.ArcTickRatioThickness = 0.5
plotOverLine1Display.PolarAxes.Use2DMode = 0
plotOverLine1Display.PolarAxes.UseLogAxis = 0

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.UseCache = 0
lineChartView1.ViewSize = [400, 400]
lineChartView1.ChartTitle = ''
lineChartView1.ChartTitleAlignment = 'Center'
lineChartView1.ChartTitleFontFamily = 'Arial'
lineChartView1.ChartTitleFontFile = ''
lineChartView1.ChartTitleFontSize = 18
lineChartView1.ChartTitleBold = 0
lineChartView1.ChartTitleItalic = 0
lineChartView1.ChartTitleColor = [0.0, 0.0, 0.0]
lineChartView1.ShowLegend = 1
lineChartView1.LegendLocation = 'TopRight'
lineChartView1.LegendSymbolWidth = 25
lineChartView1.SortByXAxis = 0
lineChartView1.LegendPosition = [0, 0]
lineChartView1.LegendFontFamily = 'Arial'
lineChartView1.LegendFontFile = ''
lineChartView1.LegendFontSize = 12
lineChartView1.LegendBold = 0
lineChartView1.LegendItalic = 0
lineChartView1.TooltipNotation = 'Mixed'
lineChartView1.TooltipPrecision = 6
lineChartView1.HideTimeMarker = 0
lineChartView1.LeftAxisTitle = ''
lineChartView1.ShowLeftAxisGrid = 1
lineChartView1.LeftAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.LeftAxisColor = [0.0, 0.0, 0.0]
lineChartView1.LeftAxisTitleFontFamily = 'Arial'
lineChartView1.LeftAxisTitleFontFile = ''
lineChartView1.LeftAxisTitleFontSize = 18
lineChartView1.LeftAxisTitleBold = 1
lineChartView1.LeftAxisTitleItalic = 0
lineChartView1.LeftAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.LeftAxisLogScale = 0
lineChartView1.LeftAxisUseCustomRange = 0
lineChartView1.LeftAxisRangeMinimum = 0.0
lineChartView1.LeftAxisRangeMaximum = 1.0
lineChartView1.ShowLeftAxisLabels = 1
lineChartView1.LeftAxisLabelNotation = 'Mixed'
lineChartView1.LeftAxisLabelPrecision = 2
lineChartView1.LeftAxisUseCustomLabels = 0
lineChartView1.LeftAxisLabels = []
lineChartView1.LeftAxisLabelFontFamily = 'Arial'
lineChartView1.LeftAxisLabelFontFile = ''
lineChartView1.LeftAxisLabelFontSize = 12
lineChartView1.LeftAxisLabelBold = 0
lineChartView1.LeftAxisLabelItalic = 0
lineChartView1.LeftAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisTitle = ''
lineChartView1.ShowBottomAxisGrid = 1
lineChartView1.BottomAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.BottomAxisColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisTitleFontFamily = 'Arial'
lineChartView1.BottomAxisTitleFontFile = ''
lineChartView1.BottomAxisTitleFontSize = 18
lineChartView1.BottomAxisTitleBold = 1
lineChartView1.BottomAxisTitleItalic = 0
lineChartView1.BottomAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.BottomAxisLogScale = 0
lineChartView1.BottomAxisUseCustomRange = 0
lineChartView1.BottomAxisRangeMinimum = 0.0
lineChartView1.BottomAxisRangeMaximum = 1.0
lineChartView1.ShowBottomAxisLabels = 1
lineChartView1.BottomAxisLabelNotation = 'Mixed'
lineChartView1.BottomAxisLabelPrecision = 2
lineChartView1.BottomAxisUseCustomLabels = 0
lineChartView1.BottomAxisLabels = []
lineChartView1.BottomAxisLabelFontFamily = 'Arial'
lineChartView1.BottomAxisLabelFontFile = ''
lineChartView1.BottomAxisLabelFontSize = 12
lineChartView1.BottomAxisLabelBold = 0
lineChartView1.BottomAxisLabelItalic = 0
lineChartView1.BottomAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisTitle = ''
lineChartView1.ShowRightAxisGrid = 1
lineChartView1.RightAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.RightAxisColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisTitleFontFamily = 'Arial'
lineChartView1.RightAxisTitleFontFile = ''
lineChartView1.RightAxisTitleFontSize = 18
lineChartView1.RightAxisTitleBold = 1
lineChartView1.RightAxisTitleItalic = 0
lineChartView1.RightAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.RightAxisLogScale = 0
lineChartView1.RightAxisUseCustomRange = 0
lineChartView1.RightAxisRangeMinimum = 0.0
lineChartView1.RightAxisRangeMaximum = 1.0
lineChartView1.ShowRightAxisLabels = 1
lineChartView1.RightAxisLabelNotation = 'Mixed'
lineChartView1.RightAxisLabelPrecision = 2
lineChartView1.RightAxisUseCustomLabels = 0
lineChartView1.RightAxisLabels = []
lineChartView1.RightAxisLabelFontFamily = 'Arial'
lineChartView1.RightAxisLabelFontFile = ''
lineChartView1.RightAxisLabelFontSize = 12
lineChartView1.RightAxisLabelBold = 0
lineChartView1.RightAxisLabelItalic = 0
lineChartView1.RightAxisLabelColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisTitle = ''
lineChartView1.ShowTopAxisGrid = 1
lineChartView1.TopAxisGridColor = [0.95, 0.95, 0.95]
lineChartView1.TopAxisColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisTitleFontFamily = 'Arial'
lineChartView1.TopAxisTitleFontFile = ''
lineChartView1.TopAxisTitleFontSize = 18
lineChartView1.TopAxisTitleBold = 1
lineChartView1.TopAxisTitleItalic = 0
lineChartView1.TopAxisTitleColor = [0.0, 0.0, 0.0]
lineChartView1.TopAxisLogScale = 0
lineChartView1.TopAxisUseCustomRange = 0
lineChartView1.TopAxisRangeMinimum = 0.0
lineChartView1.TopAxisRangeMaximum = 1.0
lineChartView1.ShowTopAxisLabels = 1
lineChartView1.TopAxisLabelNotation = 'Mixed'
lineChartView1.TopAxisLabelPrecision = 2
lineChartView1.TopAxisUseCustomLabels = 0
lineChartView1.TopAxisLabels = []
lineChartView1.TopAxisLabelFontFamily = 'Arial'
lineChartView1.TopAxisLabelFontFile = ''
lineChartView1.TopAxisLabelFontSize = 12
lineChartView1.TopAxisLabelBold = 0
lineChartView1.TopAxisLabelItalic = 0
lineChartView1.TopAxisLabelColor = [0.0, 0.0, 0.0]

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, 'XYChartRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_1.CompositeDataSetIndex = [1]
plotOverLine1Display_1.AttributeType = 'Point Data'
plotOverLine1Display_1.UseIndexForXAxis = 0
plotOverLine1Display_1.XArrayName = 'arc_length'
plotOverLine1Display_1.SeriesVisibility = ['theta', 'vectors_Magnitude']
plotOverLine1Display_1.SeriesLabel = ['arc_length', 'arc_length', 'theta', 'theta', 'vectors_X', 'vectors_X', 'vectors_Y', 'vectors_Y', 'vectors_Z', 'vectors_Z', 'vectors_Magnitude', 'vectors_Magnitude', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display_1.SeriesColor = ['arc_length', '0', '0', '0', 'theta', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'vectors_X', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'vectors_Y', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155', 'vectors_Z', '0.6', '0.3100022888532845', '0.6399938963912413', 'vectors_Magnitude', '1', '0.5000076295109483', '0', 'vtkValidPointMask', '0.6500038147554742', '0.3400015259021897', '0.16000610360875867', 'Points_X', '0', '0', '0', 'Points_Y', '0.8899977111467154', '0.10000762951094835', '0.1100022888532845', 'Points_Z', '0.220004577706569', '0.4899977111467155', '0.7199969481956207', 'Points_Magnitude', '0.30000762951094834', '0.6899977111467155', '0.2899977111467155']
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1.0', 'theta', '1.0', 'vectors_X', '1.0', 'vectors_Y', '1.0', 'vectors_Z', '1.0', 'vectors_Magnitude', '1.0', 'vtkValidPointMask', '1.0', 'Points_X', '1.0', 'Points_Y', '1.0', 'Points_Z', '1.0', 'Points_Magnitude', '1.0']
plotOverLine1Display_1.SeriesPlotCorner = ['arc_length', '0', 'theta', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0', 'vectors_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesLabelPrefix = ''
plotOverLine1Display_1.SeriesLineStyle = ['arc_length', '1', 'theta', '1', 'vectors_X', '1', 'vectors_Y', '1', 'vectors_Z', '1', 'vectors_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesLineThickness = ['arc_length', '2', 'theta', '2', 'vectors_X', '2', 'vectors_Y', '2', 'vectors_Z', '2', 'vectors_Magnitude', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['arc_length', '0', 'theta', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0', 'vectors_Magnitude', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['arc_length', '4', 'theta', '4', 'vectors_X', '4', 'vectors_Y', '4', 'vectors_Z', '4', 'vectors_Magnitude', '4', 'vtkValidPointMask', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'Points_Magnitude', '4']

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = ['arc_length', '1', 'theta', '1', 'vectors_X', '1', 'vectors_Y', '1', 'vectors_Z', '1', 'vectors_Magnitude', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'theta', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'arc_length', '1', 'theta', '1', 'vectors_Magnitude', '1', 'vectors_X', '1', 'vectors_Y', '1', 'vectors_Z', '1', 'vtkValidPointMask', '1']
plotOverLine1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'arc_length', '2', 'theta', '2', 'vectors_Magnitude', '2', 'vectors_X', '2', 'vectors_Y', '2', 'vectors_Z', '2', 'vtkValidPointMask', '2']
plotOverLine1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'arc_length', '0', 'theta', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0', 'vtkValidPointMask', '0']
plotOverLine1Display_1.SeriesMarkerSize = ['Points_Magnitude', '4', 'Points_X', '4', 'Points_Y', '4', 'Points_Z', '4', 'arc_length', '4', 'theta', '4', 'vectors_Magnitude', '4', 'vectors_X', '4', 'vectors_Y', '4', 'vectors_Z', '4', 'vtkValidPointMask', '4']

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesVisibility = ['theta']

# split cell
layout1.SplitHorizontal(2, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Python View'
pythonView1 = CreateView('PythonView')
pythonView1.UseCache = 0
pythonView1.ViewSize = [400, 400]
pythonView1.Script = ''

# assign view to a particular cell in the layout
AssignViewToLayout(view=pythonView1, layout=layout1, hint=6)

# set active source
SetActiveSource(collMemb0vtk)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=plotOverLine1)

# show data in view
collMemb0vtkDisplay = Show(collMemb0vtk, pythonView1, 'PythonRepresentation')

# trace defaults for the display properties.
collMemb0vtkDisplay.Visibility = 1

# set active source
SetActiveSource(calculator1)

# show data in view
calculator1Display_1 = Show(calculator1, pythonView1, 'PythonRepresentation')

# trace defaults for the display properties.
calculator1Display_1.Visibility = 1

# set active source
SetActiveSource(plotOverLine1)

# show data in view
plotOverLine1Display_2 = Show(plotOverLine1, pythonView1, 'PythonRepresentation')

# trace defaults for the display properties.
plotOverLine1Display_2.Visibility = 1

lambd = input("twist penetration depth")

# Properties modified on pythonView1
pythonView1.Script = """from paraview import python_view
from paraview.numpy_support import *



def setup_data(view):
    view.EnableAllAttributeArrays()

def render(view, width, height):
    figure = python_view.matplotlib_figure(width, height)
    
    pl = figure.add_subplot(1,1,1)
    pl.minorticks_on()
    pl.set_title(\'Tilt/Twist Profile: $\\\\theta(r^*)$\', fontsize = 20)
    pl.set_xlabel(\'$r^*$\', fontsize = 18)
    pl.set_ylabel(\'$\\\\theta$\', fontsize = 18)
    dataObject = view.GetVisibleDataObjectForRendering(2)
    r_line = dataObject.GetPointData().GetArray(\'arc_length\')
    th_line = dataObject.GetPointData().GetArray(\'theta\')

    np_r_line = vtk_to_numpy(r_line)
    np_r2_line = (np_r_line.max() - np_r_line)/("""+str(lambd)+""")
    np_th_line = vtk_to_numpy(th_line)
    np_rfull_line = numpy.linspace(0,5,1000)
    np_fit_line = -2*numpy.arctan(numpy.tan(-numpy.arcsin(np_th_line.max()-0.05)/2)*numpy.exp(-np_r2_line))

    pl.plot(np_r2_line, np_th_line, c="black", lw=2, label = "Morpho")
    pl.plot(np_rfull_line, np_fit_line, c="blue", lw=2, label = "Theory Fit")
    pl.legend()
    pl.axis([0,5,0,1])
    pl.grid(True)
    return python_view.figure_to_image(figure)"""

# set active view
SetActiveView(lineChartView1)

# destroy lineChartView1
Delete(lineChartView1)
del lineChartView1

# close an empty frame
layout1.Collapse(5)

# set active view
SetActiveView(pythonView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1603, 786)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 5.099177360534668e-05, 6.699980032444]
renderView1.CameraFocalPoint = [0.0, 5.099177360534668e-05, 0.0]
renderView1.CameraParallelScale = 1.4141725750410292

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).