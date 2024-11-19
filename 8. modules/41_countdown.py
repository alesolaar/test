import random
import datetime

bday_messages = ["Hope you have a very Happy Birthday!🎈",
"It's your special day – get out there and celebrate! 🎉",
"You were born and the world got better – everybody wins! 🥳",
"Have lots of fun on your special day! 🎂",
"Another year of you going around the sun! 🌞"]

random_message = random.choice(bday_messages)

today = datetime.date.today()
next_bday = datetime.date(2025,3,6)

days_left = (next_bday - today).days

if days_left == 0:
    print('Happy Bday!!')
else:
    print(f'Your bday is in {days_left} days')