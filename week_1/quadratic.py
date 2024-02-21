#This is a program to solve quadratic equations
#date:20/02/2024
#name:Lawrence Mwariri
import math

a = float(input("Enter the coefficient of first term : "))
b = float(input("Enter the coefficient of second term : "))
c = float(input("Enter the constant : "))

d = (b**2) - (4 * a * c)

x_1 = ((-b + math.sqrt(d))/2* a)
x_2 = ((-b + math.sqrt(d))/2* a)

print("The solution of the quadratic equation :",x_1)
print("The solution of the quadratic equation :",x_2)

c = float(input("Enter the constant"))
p = float(math.pi)
r = float(input("Enter the radius : "))

v = (c * p * (r**3))

print("The volume of a sphere :",v)
