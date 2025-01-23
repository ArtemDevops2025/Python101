b = 'Hello World'
print(type(b))

variable = 'string'
print(type(variable))
variable = 3
print(type(variable))

variable_1 = 5

variable_2 = 5
print(id(5))  #id function, display the locations of the two created variables
print(id(variable_1))
print(id(variable_2))


def area(l: float, L: float) -> float:
    return l * L
print(area.__annotations__)


def display(variable : str) -> str:
    print(variable)
print(display.__annotations__)

display(3)

#%%typecheck


def function(L: list) -> list:
    L = L + ['2']
    return (L)
print(function(['1+1 =']))

def double(a : int) -> int:
    a = a*2
    return(a)
double(27.6)

import numpy as np
vec = np.array([2,4,6])
a = double(vec)
print(a)

