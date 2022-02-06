'''
Import the utility function
'''
from nightlight_data_util import light_change_through_years

'''
Create two Python dictionaries, each for one year of interest.
For each dictionary, the keys are the names of the variable 
(this can be any name) and the values are the relative link to the raster files.
The keys of two raster files must match and have the same order.

Note: the raster files have been removed from the datasets folder due to file size.
Please add the raster files, and modify the below urls if necessary.
'''
raster_urls_12 = {
    'rade9': './datasets/HREA_Nigeria_2012_v1/Nigeria_rade9lnmu_2012.tif',
    'lightscore': './datasets/HREA_Nigeria_2012_v1/Nigeria_set_lightscore_sy_2012.tif',
    'prplit': './datasets/HREA_Nigeria_2012_v1/Nigeria_set_prplit_conf90_sy_2012.tif',
    'zscore': './datasets/HREA_Nigeria_2012_v1/Nigeria_set_zscore_sy_2012.tif',
}

raster_urls_18 = {
    'rade9': './datasets/HREA_Nigeria_2018_v1/Nigeria_rade9lnmu_2018.tif',
    'lightscore': './datasets/HREA_Nigeria_2018_v1/Nigeria_set_lightscore_sy_2018.tif',
    'prplit': './datasets/HREA_Nigeria_2018_v1/Nigeria_set_prplit_conf90_sy_2018.tif',
    'zscore': './datasets/HREA_Nigeria_2018_v1/Nigeria_set_zscore_sy_2018.tif',
}

'''
Execute the utility function with the necessary arguments:
- path_to_qgis: Absolute path to the QGIS application. In order to obtain this path,
                open the QGIS application, go to Plugins -> Python Console. 
                Type ```QgsApplication.prefixPath()``` and hit enter. 
                The output is the path to the QGIS application.
- raster_urls_before: raster_urls of the earlier year of interest
- raster_urls_later: raster_urls of the later year of interest
'''
light_change_through_years(path_to_qgis="C:/OSGeo4W/apps/qgis-ltr",
                           raster_urls_before=raster_urls_12,
                           raster_urls_later=raster_urls_18
                           )
