#dictionary
#Date : 28/02/2024
#Name : Lawrence Mwariri

my_laptop = {"make":"lenovo","colour":"black","weight":"3","man_year":"2019"}

print(my_laptop["make"])
print(my_laptop["colour"])
print(my_laptop["weight"])
print(my_laptop["man_year"])

#to change the value
my_laptop["colour"] = "dark blue"
my_laptop["man_year"] = "2021"

for key,value in my_laptop.items() :
    print(key)
    print(value)
    print("\n")

my_laptop["size"] = "1200mm x 600mm"
print(my_laptop)

del my_laptop["colour"]

print(my_laptop)

siz_laptop = my_laptop.copy
print(siz_laptop)