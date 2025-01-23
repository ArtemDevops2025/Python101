#dir(object)
# The int class
i = 10
i.__str__()
# The list class
tab = [1, 2 , 3, 4, 5, 6]
tab.__str__()


class Complex:
    def __init__(self, a=0, b=0):
        self.part_re = a
        self.part_im = b

    def __str__(self):
        if (self.part_im < 0):
            return self.part_re.__str__() + self.part_im.__str__() + 'd'  # returns 'a' '-b' 'd'

        if (self.part_im == 0):
            return self.part_re.__str__()  # returns 'a'

        if (self.part_im > 0):
            return self.part_re.__str__() + '+' + self.part_im.__str__() + 'c'  # returns 'a' '+' 'b' + 'c'
c = Complex(6, 3)
d = Complex(-1, -6)
print(c, d)
print("----------------------------------------")
# __le__ / __ge__:  / greater or equal
# __lt__ / __gt__:  / greater than
# __eq__ / __ne__: /not equal

x = 5

print(x > 3)  # True
print(x.__gt__(3)) # True
                           # These two types of syntax are strictly equivalent
print(x < 3) # False
print(x.__lt__(3)) # False
print("----------------------------------------")

import numpy as np

class Complex:
    def __init__(self, a=0, b=0):
        self.part_re = a
        self.part_im = b

    def __str__(self):
        if (self.part_im < 0):
            return self.part_re.__str__() + self.part_im.__str__() + 'i'  # returns 'a' '-b' 'i'

        if (self.part_im == 0):
            return self.part_re.__str__()  # returns 'a'

        if (self.part_im > 0):
            return self.part_re.__str__() + '+' + self.part_im.__str__() + 'i'  # returns 'a' '+' 'b' + 'i'

    def mod(self):
        return np.sqrt(self.part_re ** 2 + self.part_im ** 2)  # returns (sqrt(a² + b²))

    def __lt__(self, other):
        if (self.mod() < other.mod()):  # returns True if |self| < |other|
            return True
        else:
            return False

    def __gt__(self, other):
        if (self.mod() > other.mod()):  # returns True if |self| > |other|
            return True
        else:
            return False

z1 = Complex(3, 4)
z2 = Complex(2, 5)
print(z1)
print(z2)
print(z1 > z2)
print(z1 < z2)
