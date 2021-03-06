from bokeh.plotting import figure, show, output_notebook
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
import xarray
import datacube

def interactive_map():
    output_notebook()

    # range bounds supplied in web mercator coordinates
    p = figure(x_range=(1035200, 1933200), y_range=(5750600, 6376100),
               x_axis_type="mercator", y_axis_type="mercator", tools='pan, wheel_zoom, reset', active_scroll='wheel_zoom')
    tile_provider = get_provider(CARTODBPOSITRON)
    p.add_tile(tile_provider)

    show(p)
    
def plot(data, **kwargs):
    
    if 'cmap' in kwargs:
        cmap = kwargs['cmap']
    else:
        cmap = 'viridis'

    if isinstance(data, xarray.Dataset):
        data_plot = data.to_array()
        data_plot.plot.imshow(x='x', 
            y='y',
            col='time',
            size=10,
            col_wrap=3,
            cmap=cmap)
    if isinstance(data, xarray.DataArray):
        data.plot.imshow(x='x', 
            y='y',
            col='time',
            size=10,
            col_wrap=3,
            cmap=cmap)
