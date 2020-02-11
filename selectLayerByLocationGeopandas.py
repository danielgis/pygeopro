# SelectLayerByLocation with geopandas by DanielGIS

import geopandas as gpd

geometryImput = '' # Shapefile a filtrar espacialmente
geometryTarget = '' # Shapefile de area de consulta
outPath = '' # Ubicacion de salida de archivo shapefile

def SelectLayerByLocation(geometryImput, geometryTarget, outPath):
	_FIELD_DISSOLVE = 'dissolve'

	gdfInput = gpd.read_file(geometryImput)
	gdfTarget = gpd.read_file(geometryTarget)

	gdfTarget[_FIELD_DISSOLVE] = _FIELD_DISSOLVE
	geom = gdfTarget.dissolve(by=_FIELD_DISSOLVE).geometry[0]
	gdfLayer = gdfInput[gdfInput.within(geom)]

	gdfLayer.to_file(outPath)


if __name__ == '__main__':
	SelectLayerByLocation(geometryImput, geometryTarget, outPath)