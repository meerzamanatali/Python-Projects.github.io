# Before entering your phone number enter a national code of your country

import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
a= input ("Enter your phoneNumber: ")
phoneNumber=phonenumbers.parse(a)
timeZone = timezone.time_zones_for_number(phoneNumber)
Region = geocoder.description_for_number(phoneNumber,'en')
Carrier = carrier.name_for_number(phoneNumber,'en')

print(phoneNumber)
print(timeZone)
print(Region)
print(Carrier)
print('\n')