import folium
import pandas

df = pandas.read_csv("dataset.csv")
LAT = df['LAT'].mean() #Creating our own macros in Python.
LON = df['LON'].mean()
DEFAULT = 15

map = folium.Map(location = [LAT,LON],zoom_start = DEFAULT)
fg = folium.FeatureGroup(name = 'Garden Locations') #Making a feature group so that we can select all gardens at once.

for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):        # To create Garden markers by traversing through the file.
    fg.add_child(folium.Marker(location =[lat,lon],popup=name,icon=folium.Icon(color='green')))
map.add_child(fg)

map.add_child(folium.LayerControl())        #Creates filters on drop down menu on map of all the things under add_child.

map.save('map.html')
