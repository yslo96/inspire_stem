#this is a program to obtain volume of figures
#date:20/02/2024
#name:Lawrence Mwariri
import math

#The volume of a sphere

r = float(input("Enter the radius : "))

v = (4/3)*(math.pi)*r**3

print("The volume of a sphere :",v)

#The volume of cylinder

r = float(input("Enter the radius : "))
h = float(input("Enter the height : "))

v = (math.pi)*r**2*h

print("The volume of cylinder:",v)
