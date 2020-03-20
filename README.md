# Austrian Datacube Examples

<div style='padding-bottom:150px'>
    <img style='width: 220px;height: 100px;float: left;' src="./Supplementary_data/EODC-Logo-Final.png" height='100px' width='220px'/>
    <img style='width: 200px;height: 100px;float: left;' src="./Supplementary_data/BMNT_DE_Logo_dreizeilig_srgb.svg" height='100px' width='200px'/> 
    <img style='width: 200px;height: 100px;float: left;' src="./Supplementary_data/bmlv.svg" height='100px' width='200px'/>
    <img style='width: 200px;height: 100px;float: left;' src="./Supplementary_data/LOGO_TUW_GEO.png" height='100px' width='200px'/>
    <img style='width: 100px;height: 100px;float: left;' src="./Supplementary_data/Boku-wien.svg" height='100px' width='100px'/>
    <img style='width: 150px;height: 100px;float: right;' src="./Supplementary_data/ADC_Logo_final_transparent.png" height='100px' width='150px'/>
</div>

This repository contains example notebooks on how to access and manipulate raster data in `jupyterlab` using the `datacube` package for the Austrian Data Cube service provided by [EODC](https://eodc.eu).


## 1. Jupyterlab

JupyterLab is the next-generation web-based user interface for Project Jupyter.

JupyterLab provides flexible building blocks for interactive, exploratory computing. While JupyterLab has many features found in traditional integrated development environments (IDEs), it remains focused on interactive, exploratory computing.

The JupyterLab interface consists of a main work area containing tabs of documents and activities, a collapsible left sidebar, and a menu bar. The left sidebar contains a file browser, the list of running kernels and terminals, the command palette, the notebook cell tools inspector, and the tabs list.

For more information refer to the `Help` -> `JupyterLab Reference` or visit [the documentation website](https://jupyterlab.readthedocs.io/en/stable/index.html).

## 2. OpenDataCube

The Open Data Cube (ODC) is an Open Source Geospatial Data Management and Analysis Software project that helps you harness the power of Satellite data. At its core, the ODC is a set of Python libraries and PostgreSQL database that helps you work with geospatial raster data.

Your jupyterlab instance is configured to connect to the `datacube` database. To establish a connection to the database simply run (using the datacube environment):

```python
import datacube
acube = datacube.Datacube(app='test')
```

To list all available products after connecting run:

```python
acube.list_products().dropna(axis=1)
```

To find out if a product is available in your desired area and time run:

```python
product = 'MMENSIG0_Sentinel_1'           # PRODUCT NAME FROM ABOVE CODE
query = {
    'lat': (48.15, 48.35),                # DESIRED LATTITUDE BOUNDS
    'lon': (16.3, 16.5),                  # DESIRED LONGITUDE BOUNDS
    'time': ('2017-04-01', '2017-10-31')  # DESIRED TEMPORAL BOUNDS
}

for dataset in acube.find_datasets_lazy(product=product, **query):
    print(dataset.id)
```

If there is data in the given `query` the function should print out the dataset identifiers. If there is no data nothing gets printed.

To load data run:

```python
data = acube.load(product=product, output_crs='EPSG:32633', resolution=(-10, 10), **query)
data
```

For further information on opendatacube refer to the [documentation website](https://datacube-core.readthedocs.io/en/latest/).

## 3. Austrian Datacube examples

This repository contains self documenting notebooks on how to use the `datacube` package for raster data querying and manipulation. Some notebooks are extended with the `acube_functions` for providing easier access and possibilities to desired functionalities. The functions can be manually extended or can be outright skipped for more control over the `datacube`.

The ACube_products folder contains a notebook example for each product in the ACube. Additionally it shows the product definition with direct references, how to query the data and howe to plot the data.

For more information on the Austrian Data Cube project and products, visit [the ACube wiki](https://austriandatacube.eodc.eu/xwiki/bin/view/Main/)