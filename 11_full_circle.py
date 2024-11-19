import math

def circle_area(radio):
    return radio**2*math.pi

radio_circle = 5
exact_circle_area = circle_area(radio_circle)

print('The area of the circle is:', exact_circle_area)