from geopy.geocoders import Nominatim
Loc = Nominatim(user_agent="GetLoc")
# getLoc = Loc.geocode("Thrissur")
# print("Latitude = ", getLoc.latitude, "\n")
# print("Longitude = ", getLoc.longitude, "\n")
# print(getLoc.address)

locname = Loc.reverse("22.3511148,78.6677428")
print(locname.address)