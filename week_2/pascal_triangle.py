# This is a program to print pascal's triangle
#Date: 22/02/2024
#Name: Lawrence Mwariri

n = 7

for i in range(n):
    print(' '*(n-1), end=" ")
    print(' '.join(map(str, str(11**i))))
    