from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

planet_radio = {
    'Mercury': 2440,
    'Venus': 6052,
    'Earth': 6371,
    'Mars': 3390,
    'Saturn': 58232
}

random_planet=ch(planets)

if random_planet in planet_radio:
    r = planet_radio[random_planet]
    area= 4*pi*r**2
    print(f'The area of {random_planet} is {area}')
    
else:
    print("Oops! An error occurred.")

