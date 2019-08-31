from pygeocoder import Geocoder
areas = ["Vijayawada", "Amalapuram", "Hyderabad", "Pune", "Mumbai"]
for i in range(len(areas)):
    result = Geocoder('AIzaSyD52UafJ5JF-uUbp_7OIbBCBNMSQTvxqCs').geocode(areas[i])
    print(result[0].coordinates)
    print(result[0])


