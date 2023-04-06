import pandas as pd
import geopandas
from datetime import datetime

raw = geopandas.read_file("https://services5.arcgis.com/0akaykIdiPuMhFIy/arcgis/rest/services/bs_infoPannes_prod_vue/FeatureServer/0/query?where=1=1&outFields=*&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&resultType=tile&f=geojson")
raw = raw.set_index('OBJECTID')

now = datetime.now()

raw["timestamp"] = now

raw.to_csv(f"data/data-{now.strftime('%Y-%m-%d_%H%M')}.csv")