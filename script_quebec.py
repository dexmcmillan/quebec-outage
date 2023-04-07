from datetime import datetime
import requests
import json

points_url = "https://services5.arcgis.com/0akaykIdiPuMhFIy/arcgis/rest/services/bs_infoPannes_prod_vue/FeatureServer/0/query?returnGeometry=true&where=1=1&outSR=4326&outFields=*&inSr=4326&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&geometryPrecision=6&resultType=tile&f=geojson"
shapes_url = "https://services5.arcgis.com/0akaykIdiPuMhFIy/arcgis/rest/services/bs_infoPannes_prod_vue/FeatureServer/1/query?returnGeometry=true&where=1=1&outSR=4326&outFields=*&inSr=4326&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&geometryPrecision=6&resultType=tile&f=geojson"

now = datetime.now()

geojson_points = json.dumps(requests.get(points_url).json())
geojson_shapes = json.dumps(requests.get(shapes_url).json())

with open(f"data/quebec/data-points-{now.strftime('%Y-%m-%d_%H%M')}.geojson", 'w') as file:
    file.write(geojson_points)

with open(f"data/quebec/data-shapes-{now.strftime('%Y-%m-%d_%H%M')}.geojson", 'w') as file:
    file.write(geojson_shapes)