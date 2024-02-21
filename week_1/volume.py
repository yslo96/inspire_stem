#this is a program to obtain volume of figures
#date:20/02/2024
#name:Lawrence Mwariri
import math

r = float(input("Enter the radius : "))

v = (4/3)*(math.pi)*r**3

print("The volume of a sphere :",v)

r2 = float(input("Enter the radius : "))
h = float(input("Enter the height : "))

v2 = (math.pi)*r**2*h

print("The volume of cylinder:",v2)