# Folium a mapping lib
import folium
import pandas

# Importing Volcanic Data
data = pandas.read_csv("Volcanoes.txt")
latS = list(data["LAT"])
lonS = list(data["LON"])
elevS = list(data["ELEV"])
nameS = list(data["NAME"])

# Html Editing
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


map = folium.Map(location=[38.55, -99.09],
                 zoom_start=6, titles="Stamen Terrain")

# Adding elements to the Map
fg = folium.FeatureGroup(name="My Map")

# Adding Markers
for lat, lon, elev, name in zip(latS, lonS, elevS, nameS):
    iframe = folium.IFrame(html=html % (
        name, name, str(elev)), width=200, height=100)
    fg.add_child(folium.Marker(location=[lat, lon],
                               popup=folium.Popup(iframe), icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map_html_popup_simple.html")
