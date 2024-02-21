#This is a program that shows employee records
#Date:21/02/2024
#Name:Lawrence Mwariri

#Employees detail

n = input("Name : ")
a = input("Age : ")
s = float(input("Salary : "))
b = float(input("Bonus : "))

t = s + b

print("Employee's name :",n)
print("Employee's age :",a)
print("Employee's basic salary :",s)
print("Employee's bonus :",b)
print("Employee's total income :",t)

s2 = (130 / 100 * s)
t2 = s2 + b

print("Employee's new basic salary :",s2)
print("Employee's new total income :",t2)

b2 = b - 5000
t2 = s2 + b2

print("Employee's new bonus :",b2)
print("Employee's final total income :",t2)
