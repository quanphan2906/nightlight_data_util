from .get_abs_path import get_abs_path
from qgis.core import *
from qgis.analysis import QgsRasterCalculatorEntry, QgsRasterCalculator
from osgeo import gdal


def light_change_through_years(path_to_qgis, raster_urls_before, raster_urls_later):

    # Inits app
    QgsApplication.setPrefixPath(path_to_qgis, True)
    qgs = QgsApplication([], False)
    qgs.initQgis()
    transformContext = QgsProject.instance().transformContext()

    for light_var in raster_urls_before:
        nigeria12 = QgsRasterLayer(raster_urls_before[light_var])
        nigeria18 = QgsRasterLayer(raster_urls_later[light_var])

        output = get_abs_path("temp/{}_18_12_diff.tif".format(light_var))
        entries = []

        ras = QgsRasterCalculatorEntry()
        ras.ref = 'ras@1'
        ras.raster = nigeria12
        ras.bandNumber = 1
        entries.append(ras)

        ras = QgsRasterCalculatorEntry()
        ras.ref = 'ras@2'
        ras.raster = nigeria18
        ras.bandNumber = 1
        entries.append(ras)

        calc = QgsRasterCalculator('ras@2 - ras@1', output, 'GTiff',
                                   nigeria12.extent(
                                   ), nigeria12.width(),
                                   nigeria12.height(), entries, transformContext)

        calc.processCalculation()

        outfn = './{}_18_12_diff_compressed.tif'.format(light_var)

        ds = gdal.Translate(outfn, output, creationOptions=[
                            "COMPRESS=LZW", "TILED=YES"])
        ds = None
