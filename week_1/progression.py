#This is a program to calculate terms on a sequence
#Date:21/02/2024
#Name:Lawrence Mwariri

import math

#Arithmetic sequence

a = int(input("The first term of sequence :"))
n = int(input("The number of sequence :"))
d = int(input("The common diff :"))

an = a+(n-1)*d

print("The term in the arithmetic :",an)

#Geometric sequence

a = int(input("The first term of sequence :"))
n = int(input("The number of sequence :"))
r = int(input("The common ratio :"))

ar = a*r**(n-1)

print("The term in the geometic :",ar)
