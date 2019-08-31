import pygmaps

lat_list = [16.506174, 16.572090, 17.385044]
lon_list = [80.648018, 82.000854, 78.486671]
mymap = pygmaps.maps(30.3164945, 78.03219179999, 15)
for i in range(len(lat_list)):
	mymap.addpoint(lat_list[i], lon_list[i], "#ff0000")
mymap.draw('maps.html')
