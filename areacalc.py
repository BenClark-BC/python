"""This program will calculate the area of a Circle or a Triangle. The user will be prompted to choose a shape and also input some dimensions."""

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The calculater is starting up!"

print 'Current time: %s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute)

sleep(1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle or T for Triangle: ")
option = option.upper()
if option == 'C':
    radius = float(raw_input("Enter the radius - the distance around the circle: "))
    area = pi * radius**2
    print "The pi is baking...har har har!"
    sleep(1)
    print "Processing..."
    sleep(1)
    print "Almost got it..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
    base = float(raw_input("Enter the length of the base of the triangle: "))
    height = float(raw_input("Enter the height of the triangle: "))
    area = (0.5)*base*height
    print "Uni Bi Tri..."
    sleep(1)
    print "Abracadabra!"
    sleep(1)
    print "Ta-DA!!!"
    print ("Area: %.2f. \n%s" % (area, hint))
else:
    print "You have entered an incorrect value, please restart the ptogram and enter an integer. \nExiting..."
