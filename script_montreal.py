from datetime import datetime
import requests
import json

montreal_shapes_url = 'https://services5.arcgis.com/0akaykIdiPuMhFIy/arcgis/rest/services/bs_infoPannes_prod_vue/FeatureServer/1/query?returnGeometry=true&where=1=1&outFields=*&geometry={"xmin":-74.355469,"ymin":45.061347,"xmax":-72.795410,"ymax":45.943262,"spatialReference":{"wkid":4326}}&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&geometryPrecision=6&resultType=tile&f=geojson'

now = datetime.now()

geojson_shapes = json.dumps(requests.get(montreal_shapes_url).json())

with open(f"data/montreal/data-shapes-{now.strftime('%Y-%m-%d_%H%M')}.geojson", 'w') as file:
    file.write(geojson_shapes)