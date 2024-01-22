from paraview import python_view
from paraview.numpy_support import *



def setup_data(view):
    view.EnableAllAttributeArrays()

def render(view, width, height):
    figure = python_view.matplotlib_figure(width, height)
    
    pl = figure.add_subplot(1,1,1)
    pl.minorticks_on()
    pl.set_title('Twist Profile: $\\theta$', fontsize = 20)
    pl.set_xlabel('$r^*$', fontsize = 18)
    pl.set_ylabel('$\\theta$', fontsize = 18)
    dataObject = view.GetVisibleDataObjectForRendering(2)
    r_line = dataObject.GetPointData().GetArray('arc_length')
    th_line = dataObject.GetPointData().GetArray('theta')

    np_r_line = vtk_to_numpy(r_line)
    np_r2_line = (np_r_line.max() - np_r_line)*5
    np_th_line = vtk_to_numpy(th_line)

    np_fit_line = -2*numpy.arctan(numpy.tan(-numpy.arcsin(np_th_line.max())/2)*numpy.exp(-np_r2_line))

    pl.plot(np_r2_line, np_th_line, c="black", lw=2)
    pl.plot(np_r2_line, np_fit_line, c="blue", lw=2)
    return python_view.figure_to_image(figure)