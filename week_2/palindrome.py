# This is a program to identify whether a word is a palindrome
#Date: 22/02/2024
#Name: Lawrence Mwariri

w = input("Enter the word : ")

rw = (" ")

for y in w:
    rw= y + rw
    print("The reversed word of",w,"is",rw)