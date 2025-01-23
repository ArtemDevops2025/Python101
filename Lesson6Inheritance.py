class Vehicle:  # Definition of the Vehicle class
    def __init__(self, a, b=None):
        self.seats = a  # nombre de places dans le vehicule
        if b == None:
            self.passengers = []  # liste contenant le nom des passagers
        else:
            self.passengers = b

    def print_passengers(self):  # Prints the names of the passengers in the vehicle
        for i in range(len(self.passengers)):
            print(self.passengers[i])

    def add(self, name):  # Adds a new passenger to the list of passengers.
        self.passengers.append(name)

class Motorcycle(Vehicle):
    def __init__(self, b, c):
        self.seats = 2  # The number of seats is automatically set to 2 and is not modified by the arguments
        self.passengers = b
        self.brand = c

    def add(self, name):
        if (len(self.passengers) < self.seats):
            self.passengers.append(name)
            print('There are', self.seats - len(self.passengers), 'seats left.')
        else:
            print("The vehicle is full.")

moto1 = Motorcycle(['Pierre', 'Dimitri','Yohann'], 'Yamaha')
moto1.add('Art')  # will not be printed
car2 = Vehicle(3, ['Antoine', 'Thomas', 'Raphaël'])
moto2 = Motorcycle(['Guillaume', 'Charles'], 'Honda')
moto2.add('Dimitri')
car2.add('Benjamin')

moto1.print_passengers()
print("-------------------------")
car2.print_passengers()
print("-------------------------")
moto2.print_passengers()
print("-------------------------")
moto2.print_passengers()
print("-------------------------")
print(car2.seats)
print("-------------------------")


class Convoy:
    def __init__(self):
        self.vehicle_list = []
        self.vehicle_list.append(Vehicle(4))  # vehicule_list is initialized with a list containing 1 vehicle
        self.length = 1  # the length attribute is initialized to 1

    def add_vehicle(self, vehicle):
        self.vehicle_list.append(vehicle)  # a Vehicle is added at the end of the list
        self.length = self.length + 1  # update the length of the convoy


convoy1 = Convoy()                                     # Instanciation of the convoy

convoy1.vehicle_list[0].add('Albert')                  # "Albert" is added to the first vehicle in the convoy

convoy1.add_vehicle(Motorcycle(['Raphael'] , 'Honda')) # We have to remember that the first argument of the Motorcycle
                                                       # constructor is a list and not a string.

for vehicle in convoy1.vehicle_list: # We go through the list of vehicles in the convoy
    vehicle.print_passengers()       # We use the print_passengers method of the Vehicle class





