<<<<<<< HEAD
# A block of code running together as a unit
#Date : 29/02/2024
#Name : Lawrence Mwariri
 
#define the function
def print_name():
    print("My name is Lawrence Mwariri")

#calling the function
print_name()

def print_details(name, age, id, gender):
    print("I am {0},{1} years old.My id no is {2} and gender is {3}".format(name, age, id, gender))

print_details("Lawrence Mwariri", "17", "0318852", "male")
print_details("Jane Forester", "24", "89659832" ,"female")

#sum of numbers
def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)

#product of numbers
def prod_nums(x,y):
    return x * y

print(prod_nums(8,6))

def print_odds(first_number, last_number):
    for y in range(first_number, last_number):
        print(y % 2)

=======
# A block of code running together as a unit
#Date : 29/02/2024
#Name : Lawrence Mwariri
 
#define the function
def print_name():
    print("My name is Lawrence Mwariri")

#calling the function
print_name()

def print_details(name, age, id, gender):
    print("I am {0},{1} years old.My id no is {2} and gender is {3}".format(name, age, id, gender))

print_details("Lawrence Mwariri", "17", "0318852", "male")
print_details("Jane Forester", "24", "89659832" ,"female")

#sum of numbers
def sum_nums(x,y):
    return x + y

z = sum_nums(10,20)
print(z)

#product of numbers
def prod_nums(x,y):
    return x * y

print(prod_nums(8,6))

def print_odds(first_number, last_number):
    for y in range(first_number, last_number):
        print(y % 2)

>>>>>>> 317343e0576eee95ce444520709c3e30c276fb8d
print_odds(0,15)