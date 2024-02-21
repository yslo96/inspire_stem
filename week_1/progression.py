import math
a = int(input("The first term of arithmetic :"))
n = int(input("The number of arithmetics :"))
d = int(input("The common diff :"))

an = a+(n-1)*d

print("The term in the arithmetic :",an)

a2 = int(input("The first term of geometric :"))
n2 = int(input("The number of geometric :"))
r = int(input("The common ratio :"))

ar = a*r**(n2-1)

print("The term in the geometic :",ar)
