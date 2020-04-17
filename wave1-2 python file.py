import math 

# Online Python complier to run Python online.
# Write Python 3 code
# Python program to find Volume & Surface Area of a Cylinder
PI = 3.14 
radius = float(input('Please Enter the Radius of a cylinder:')) 
height = float(input('Please Enter the Height of a cylinder:'))
CircularArea = PI*radius*radius
Volume = CircularArea*height 
print("The volume of a cylinder= %.2f"%Volume)
