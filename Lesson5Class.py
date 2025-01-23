class Complex:
    def __init__(self, a, b):
        self.part_re = a
        self.part_im = b
    def display(self):
        if(self.part_im < 0):
            print(self.part_re,'-', -self.part_im,'i')
        if(self.part_im == 0):
            print(self.part_re)
        if(self.part_im > 0):
            print(self.part_re, '+',self.part_im,'i')
C1 = Complex(4,5)
C1.display()
C2 = Complex(3,-2)
C2.display()
print("--------------------------------")

class Vehicle:
    def __init__(self, a, b = None):
        self.seats = a
        self.passengers = b if b else []
    def print_passengers(self):
        for i in range(len(self.passengers)):
            print(self.passengers[i])



# Run the cell. You can modify the instantiation so that the changes are reflected.
car2 = Vehicle(4,['Dimitri', 'Charles', 'Yohan'])

print(car2.seats)          # Display of the 'seats' attribute
car2.print_passengers()    # Calling of the print_passengers method
print("--------------------------------")


class Vehicle:
    def __init__(self, a, b=None):
        self.seats = a
        self.passengers = b if b else []

    def print_passengers(self):
        for i in range(len(self.passengers)):
            print(self.passengers[i])

    def add(self, name):  # New methd
        self.passengers.append(name)


car1 = Vehicle(4, ['Charles', 'Paul'])
car1.add('Raphaël')

car1.print_passengers()
print("--------------------------------")
#Define in the Complex class an add method which takes as argument a Complex  object and adds it to the instance calling the method
#The result of this sum will be stored in the attributes of the Complex calling the method.
#Test the new add method on two instances of the Complex class and display their sum

class Complex:
    def __init__(self, a, b):
        self.part_re = a
        self.part_im = b

    def display(self):
        if self.part_im < 0:
            print(self.part_re, '-', -self.part_im, 'i')
        elif self.part_im == 0:
            print(self.part_re)
        else:
            print(self.part_re, '+', self.part_im, 'i')

    def add(self, c):
        try:
            # Check if the input is a Complex object
            if not isinstance(c, Complex):
                raise TypeError("Input must be a Complex object")

            # Add the real and imaginary parts of the complex number c to self
            self.part_re += c.part_re
            self.part_im += c.part_im

        except TypeError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
# Example usage
C1 = Complex(4, -1)
C2 = Complex(-1, 3)

# Adding two Complex objects
C1.add(C2)
C1.display()  # Output: 3 + 2i

# Testing exception handling with invalid input
C3 = "Not a Complex object"
C1.add(C3)  # Output: Error: Input must be a Complex object