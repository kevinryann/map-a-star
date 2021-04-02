import osmapi as osm

api = osm.OsmApi()

node = api.NodeGet(1989098258)
print(node["lon"])
print(node["lat"])