# Strings in python
#Date: 22/02/2024
# Name: Lawrence Mwariri

city = "nairobi"

#convert to uppercase

print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[5])
print(city[6])

print("\n")# prints a new line
print(city.upper())
name = "LAWRENCE MWARIRI"

print(name)
print(name.lower())# converts string to lower case

town = "  Naivasha  "

print(town)
print("\t")# new tab
print(town.strip())

f_name = "Lawrence"
s_name = "Mwariri"

full_name = f_name + s_name

print(full_name)

#replacing a character

fruit = "Apple"

print(fruit.replace("A","Y"))

subject = "Physical,Science"

print(subject.split(","))

age = 17
height = 1.4

print("I am {0} years old and {1} metres tall " .format(age,height))