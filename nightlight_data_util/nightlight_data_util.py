from cgi import print_form
from qgis.core import *
from qgis.PyQt.QtCore import QVariant
from qgis.analysis import QgsZonalStatistics

import pandas as pd
import os

def get_abs_path(relative_path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, relative_path)
    return filename


def match_coords_w_nightlight_data(
        path_to_qgis = "C:/OSGeo4W/apps/qgis-ltr",
        radius = 5000,
        segment = 18,
        data_url = "datasets/nga_householdgeovars_y4.csv",
        id_col_name = "hhid",
        lon_col_name = "lon_dd_mod",
        lat_col_name = "lat_dd_mod",
        destination_csv = "nigeria_nightlight_data.csv",
        raster_urls = {}):

    # Inits app
    QgsApplication.setPrefixPath(path_to_qgis, True)
    qgs = QgsApplication([], False)
    qgs.initQgis()

    # Sets up original CRS
    epsg4326 = QgsCoordinateReferenceSystem("EPSG:4326")
    transformContext = QgsProject.instance().transformContext()

    # Creates shapefile to write buffer into
    filename = get_abs_path("temp/buffers.shp")

    fields = QgsFields()
    fields.append(QgsField(id_col_name, QVariant.Int))
    fields.append(QgsField(lon_col_name, QVariant.Double))
    fields.append(QgsField(lat_col_name, QVariant.Double))

    save_options = QgsVectorFileWriter.SaveVectorOptions()
    save_options.driverName = "ESRI Shapefile"
    save_options.fileEncoding = "UTF-8"

    writer = QgsVectorFileWriter.create(
        filename, 
        fields,
        QgsWkbTypes.Polygon,
        epsg4326,
        transformContext,
        save_options
    )

    # Loads .csv file as vector layer
    vlayer = QgsVectorLayer(data_url, "coordinates", "ogr")
    features = vlayer.getFeatures()

    field_names = [ field.name() for field in vlayer.fields() ]
    id_col_idx = field_names.index(id_col_name)
    lat_col_idx = field_names.index(lat_col_name)
    lon_col_idx = field_names.index(lon_col_name)

    count = 0
    for f in features: # each feature is a point
        attributes = f.attributes()
        hhid = int(attributes[id_col_idx])
        lat = float(attributes[lat_col_idx])
        lon = float(attributes[lon_col_idx])

        # Sets up projected CRS and transformer
        local_azimuthal = QgsCoordinateReferenceSystem()
        proj4_str = "+proj=aeqd +R=6371000 +units=m +lat_0={} +lon_0={}".format(lat, lon)
        local_azimuthal.createFromProj(proj4_str)

        wgs84_to_azimuthal = QgsCoordinateTransform(epsg4326, local_azimuthal, transformContext)
        azimuthal_to_wgs84 = QgsCoordinateTransform(local_azimuthal, epsg4326, transformContext)

        # Projects the point, creates buffer, and reprojects to original CRS
        projected_point = wgs84_to_azimuthal.transform(QgsPointXY(lon, lat))
        point_geom = QgsGeometry.fromPointXY(projected_point)
        buffer = point_geom.buffer(radius, segment)
        buffer.transform(azimuthal_to_wgs84)

        # Writes buffer to file
        fet = QgsFeature()
        fet.setGeometry(buffer)
        fet.setAttributes([hhid, lon, lat])
        writer.addFeature(fet)

        count += 1
        if count % 500 == 0:
            print("{count} buffers created".format(count = count))

    print("In total, {count} buffers created".format(count = count))

    # flush file to avoid memory leak
    del writer
    del vlayer

    # Reads in the buffer shape files
    filename = get_abs_path("temp/buffers.shp")
    vlayer = QgsVectorLayer(filename, "buffers", "ogr")

    # Calculates zonal mean-s for each raster
    for light_variable, url in raster_urls.items():
        raster = QgsRasterLayer(url)
        zoneStats = QgsZonalStatistics(vlayer, raster, stats = QgsZonalStatistics.Statistics(QgsZonalStatistics.Mean))
        zoneStats.calculateStatistics(None)
        print("Finish calculating aggregate mean of", light_variable)

    # Writes zonal mean-s to csv
    destUrl = get_abs_path("temp/nightlight_data.csv")
    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "CSV"
    QgsVectorFileWriter.writeAsVectorFormatV2(vlayer, destUrl, transformContext, options)

    del vlayer

    # Renames column
    light_df = pd.read_csv(get_abs_path("temp/nightlight_data.csv"))
    count = 0
    for light_variable in raster_urls.keys():
        if count == 0:
            light_df.rename(columns = {"mean": light_variable + "_aggregated_mean"}, inplace = True)
        else:
            light_df.rename(columns = {"mean_" + str(count): light_variable + "_aggregated_mean"}, inplace = True)

        count += 1

    light_df.to_csv(destination_csv, sep=",")

    print("Done")

    

    


