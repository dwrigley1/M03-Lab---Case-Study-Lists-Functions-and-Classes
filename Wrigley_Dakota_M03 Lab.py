# This program allows a user to enter their vehicle type, year, make, model, door count & roof type
# the Automobile class inherits its vehicle type attribute from the Vehicle super class

class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def selections(self):
        print('The vehicle type is ', self.vehicle_type)
        print('Year is', self.year)
        print('Make is ', self.make)
        print('Model is ', self.model)
        print('Number of doors is ', self.doors)
        print('The type of roof is ', self.roof)

def make_choices():
    vehicle_type = input('Enter the vehicle type ')
    year = input('Enter the year of the vehicle ')
    make = input('Enter the make of the vehicle ')
    model = input('Enter the model of the vehicle ')
    doors = input('Enter the number of doors on the vehicle ')
    roof = input('Enter the style of roof the vehicle has ')

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    print('Vehicle information :')
    car.selections()

make_choices()

     