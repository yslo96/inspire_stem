#This is a program to calculate hire purchase#
#Date:21/02/2024
#Name:Lawrence Mwariri

d = int(input("Enter the deposit : "))
m = int(input("Enter number of months : "))
mi = int(input("Enter the monthly installments : "))

hp = d + (m * mi)

print("Total amount paid :",hp)
