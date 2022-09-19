import phonenumbers
import opencage
from text import number
from phonenumbers import geocoder

ch_number = phonenumbers.parse(number,"CH")
print(ch_number)
location = geocoder.description_for_number(ch_number, "en")
print(location)
from phonenumbers import carrier
service_provider = carrier.name_for_valid_number(ch_number,'en')
print(service_provider)
from opencage.geocoder import OpenCageGeocode
key = "5527fcd50792488fb0f0e91605d21337"
geocoder = OpenCageGeocode(key)
query = str(location)
result =geocoder.geocode(query)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)
# print(result)



