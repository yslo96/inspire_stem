# This is a program to calculate factorial of numbers
#Date: 22/02/2024
#Name: Lawrence Mwariri

n = int(input("Enter the number :"))
f = 1

for y in range(1,n+1):
    f =f * y
    n = y
    print("The factorial of",n,"is",f)

for x in range(0,20,2):
    print(x)

for x in range(1,20,2):
    print(x)