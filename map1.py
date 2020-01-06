# Folium a mapping lib
import folium
import pandas

# Importing Volcanic Data
data = pandas.read_csv("Volcanoes.txt")
latS = list(data["LAT"])
lonS = list(data["LON"])
elevS = list(data["ELEV"])
nameS = list(data["NAME"])

# Function to Change the marker color depending on Elevation


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# Html Editing from python script
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# Map Initial Display
map = folium.Map(location=[38.55, -99.09],
                 zoom_start=6, titles="Stamen Terrain")

# Adding elements to the Map
# ---------------------------

# Adding Markers for the volcanos locations layer
fg_markers = folium.FeatureGroup(name="Volcanoes")


for lat, lon, elev, name in zip(latS, lonS, elevS, nameS):
    iframe = folium.IFrame(html=html % (
        name, name, str(elev)), width=200, height=100)
    fg_markers.add_child(folium.CircleMarker(location=[lat, lon], radius=6,
                                             popup=folium.Popup(iframe), fill_color=color_producer(elev), color="grey", fill_opacity=0.7))

map.add_child(fg_markers)

# Adding colors for locations per population layer
fg_color = folium.FeatureGroup(name="Population")
fg_color.add_child(folium.GeoJson(
    data=open("world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg_color)

# adding a layer control
map.add_child(folium.LayerControl())


map.save("Map_html_popup_simple.html")
