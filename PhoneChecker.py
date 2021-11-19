import phonenumbers
from phonenumbers import geocoder
phone=input('Type in the phone number in a shape like this: +551140028922')
phone_number=phonenumbers.parse(phone)
print(geocoder.description_for_number(phone_number, 'pt'))