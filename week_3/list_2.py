# List of friends
#Date : 28/02/2024
#Name : Lawrence Mwariri

friends = ["lawrence","ioane","chrysallis","davis","jane"]
for friend in friends :
    print(friend)

enemies = friends[:]#To copy one list onto another
print(enemies)

fruits = ["apple","mango","banana","strawberry","pineapple"]

#slice the list to get part of the list

print(fruits[0:3])

del fruits[0]
print(fruits)

squares = [] # initiates an empty list

for y in range(0,11):
    squares.append(y**2)

print(squares)