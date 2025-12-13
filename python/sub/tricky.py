import phonenumbers
from phonenumbers import geocoder
phoneNum=phonenumbers.parse("+91 8801886004")
print(geocoder.description_for_number(phoneNum, "en"))