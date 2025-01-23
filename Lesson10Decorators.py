def print_before_execution(function):
   def print_then_execute(*args, **kwargs):
       print('here is what returns the function {}'.format(function.__name__))
       function(*args, **kwargs)
   return print_then_execute

@print_before_execution
def print_hello_world():
    print("hello world")

print_hello_world()


def display_doc(function):
    """
    A decorator that prints the docstring of the decorated function before executing it.
    """

    def print_doc(*args, **kwargs):
        # Print the docstring of the function
        print(f"Documentation for {function.__name__}:")
        print(function.__doc__)

        # Execute the original function and return its result
        return function(*args, **kwargs)

    return print_doc


# Example usage of the decorator
@display_doc
def add(a, b):
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b


@display_doc
def greet(name):
    """
    This function greets the user by their name.

    Parameters:
    name (str): The name of the user.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"

# Testing the decorated functions
result_add = add(3, 5)
print("Result of add:", result_add)
result_greet = greet("Alice")
print("Result of greet:", result_greet)

import pandas as pd
@display_doc
def import_csv(*args, **kwargs):
    '''
    Function to import a csv file into a pandas DataFrame.
    '''
    return pd.read_csv(*args, **kwargs)
import_csv('questions.csv')

import time

def execution_time(function):
    def timer(*args, **kwargs):
        start_time = time.time()
        results = function(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print("This function took {} seconds to run.".format(duration))
        return results
    return timer

@execution_time
def import_csv(*args, **kwargs):
    '''
    Function to import a csv file into a pandas DataFrame.
    '''
    return pd.read_csv(*args, **kwargs)

import_csv('questions.csv')

def entry_contains(a_contains):
    def decorator(function):
        def new_function(*args, **kwargs):
            if a_contains in str(args[0]):
                return function(*args, **kwargs)
            else:
                return "The first entry must contain {}".format(a_contains)
        return new_function
    return decorator


def print_before_execution(function):
    def print_then_execute(*args, **kwargs):
        print('This is what the function returns {}'.format(function.__name__))
        function(*args, **kwargs)

    return print_then_execute


@print_before_execution
def print_hello_world():
    '''
    Description of my fonction
    '''
    print("hello world")

help(print_hello_world)


### Definition of the factorial function
def factorial(n):
    if n == 1:
        return (n)
    else:
        return (n * factorial(n - 1))

### Definition of the decorated loop
@execution_time
def loop(n=5):
    L = []
    for k in range(1, n):
        L.append(factorial(k))
    return (L)
### Execution
print (loop(5))


from functools import lru_cache
@lru_cache()
def factorial(n):
    if n==1:
        return(n)
    else:
        return(n*factorial(n-1))
print (loop(5))
print("------------------")
@execution_time
@lru_cache()

def print_hello(a='hello after 5'):
    time.sleep(5)
    return a

a = print_hello()
print(print_hello())

print(a)





