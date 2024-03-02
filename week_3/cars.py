# This is a class that describes cars
#Date : 01/03/2024
#Name : Lawrence Mwariri

class car:
    def _init_(self,model,make,year_of_production,fuel_capacity,colour,cc):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.colour = colour
        self.cc = cc

    def print_make(self,make):
        print("The car is of {0} make" .format(self.make))

    def set_make(self,make):
        self.make = make

    def get_make(self):
        return self.make

my_car = car("AMG SL63","Mercedes Benz","2021","3200l","Blue","3298")
friends_car = car("Impalla","Chevrolet","1969","2500l","lilac","7583")

my_car.print_make("Chevrolet")

my_car.set_make("Audi")
friends_car.set_make("Subaru")

print(my_car.get_make())
print(friends_car.get_make())