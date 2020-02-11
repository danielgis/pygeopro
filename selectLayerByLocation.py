#SelectLayerByLocation by DanielGIS

from osgeo import ogr

geometryImput = '' # Shapefile a filtrar espacialmente
geometryTarget = '' # Shapefile de area de consulta
outPath = '' # Ubicacion de salida de archivo shapefile

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
	layer = src.CreateLayer(outPath, spatialReference, layerInput.GetGeomType())

	rows = list()
	for i in layerTarget:
		layerInput.SetSpatialFilter(i.GetGeometryRef())
		rows.extend(map(lambda i: layer.CreateFeature(i), layerInput))
		layerInput.SetSpatialFilter(None)


if __name__ == '__main__':
	SelectLayerByLocation(geometryImput, geometryTarget, outPath)