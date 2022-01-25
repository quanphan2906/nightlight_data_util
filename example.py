'''
Import the utility function
'''
from nightlight_data_util import match_coords_w_nightlight_data

'''
Create a Python dictionary, with keys are the names of the variable 
(this can be any name) and the values are the relative link to the raster files.
Note: the raster files have been removed from the datasets folder due to file size.
Please add the raster files, and modify the below urls if necessary.
'''
raster_urls = {
    'rade9': 'datasets/HREA_Nigeria_2018_v1/Nigeria_rade9lnmu_2018.tif',
    'lightscore': 'datasets/HREA_Nigeria_2018_v1/Nigeria_set_lightscore_sy_2018.tif',
    'prplit': 'datasets/HREA_Nigeria_2018_v1/Nigeria_set_prplit_conf90_sy_2018.tif',
    'zscore': 'datasets/HREA_Nigeria_2018_v1/Nigeria_set_zscore_sy_2018.tif',
}

'''
Execute the utility function with the necessary arguments:
- path_to_qgis: Absolute path to the QGIS application. In order to obtain this path, 
                you must first download the QGIS software from here: 
                https://qgis.org/en/site/forusers/download.html. 
                Open the QGIS application, go to Plugins -> Python Console. 
                Type ```QgsApplication.prefixPath()``` and hit enter. 
                The output is the path to the QGIS application.
- radius: The radius of each aggregated circles (in meters) (optional, default to 5000)
- segment: The number of edges the aggregated circles have every 90 degree (optional, default to 18)
- data_url: Relative path to the household coordinates dataset
- id_col_name: Name of the household id column (optional, default to "hhid")
- lon_col_name: Name of the household longtitude column (optional, default to "lon_dd_mod")
- lat_col_name: Name of the household latitude column (optional, default to "lat_dd_mod")
- destination_csv: Relative path to the result csv
- raster_urls: The aforementioned raster_urls
'''
match_coords_w_nightlight_data( path_to_qgis = "C:/OSGeo4W/apps/qgis-ltr",
                                radius = 5000, # in meters
                                segment = 18,
                                data_url = "datasets/nga_householdgeovars_y4.csv",
                                id_col_name = "hhid",
                                lon_col_name = "lon_dd_mod",
                                lat_col_name = "lat_dd_mod",
                                destination_csv = "nigeria_nightlight_data.csv",
                                raster_urls = raster_urls )