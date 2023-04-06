from datetime import datetime
import requests
import json

shapes_url = "https://outages.hydroottawa.com/geojson/outage_polygons_public.json"

now = datetime.now()

geojson_shapes = json.dumps(requests.get(shapes_url).json())

with open(f"data/ottawa/data-shapes-{now.strftime('%Y-%m-%d_%H%M')}.geojson", 'w') as file:
    file.write(geojson_shapes)