#SelectLayerByLocation by DanielGIS

from osgeo import ogr

geometryImput = 'ccpp_prj.shp' # Shapefile a filtrar spacialmente
geometryTarget = 'polygon.shp' # Shapefile de área de consulta
outPath = 'out.shp' # Ubicación de salida de archivo shapefile

def SelectLayerByLocation(geometryImput, geometryTarget, outPath):

	_DRIVER_SHP = "ESRI Shapefile"

	inputDataSource = ogr.Open(geometryImput)
	layerInput = inputDataSource.GetLayer()
	
	targetDataSource = ogr.Open(geometryTarget)
	layerTarget = targetDataSource.GetLayer()

	geometryType = layerInput.GetGeomType()
	spatialReference = layerInput.GetSpatialRef()

	driver = ogr.GetDriverByName(_DRIVER_SHP)
	src = driver.CreateDataSource(outPath)
	layer = src.CreateLayer(outPath, spatialReference, geom_type=layerInput.GetGeomType())

	rows = list()
	for i in layerTarget:
		layerInput.SetSpatialFilter(i.GetGeometryRef())
		rows.extend(map(lambda i: layer.CreateFeature(i), layerInput))
		layerInput.SetSpatialFilter(None)


if __name__ == '__main__':
	SelectLayerByLocation(geometryImput, geometryTarget, outPath)