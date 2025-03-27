import pandas as pd


uri = 'https://nominatim.openstreetmap.org/ui/reverse.html?lat={}&lon={}'
lat = 51.4866216
lng = 6.6138604
print(uri.format(lat, lng))
print(9/2)