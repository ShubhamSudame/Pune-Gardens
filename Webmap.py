import folium
import pandas

df = pandas.read_csv("dataset.csv")
LAT = df['LAT'].mean() #Creating our own macros in Python.
LON = df['LON'].mean()
DEFAULT = 6

map = folium.Map(location = [LAT,LON],zoom_start = DEFAULT)

map.simple_marker(location =[18.5467,73.7925],popup='Home',marker_color='green')
map.simple_marker(location =[18.5312,73.8557],popup='College',marker_color='red')
#Hello.
map.save('map.html')
