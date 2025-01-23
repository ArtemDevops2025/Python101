def double(number) :
    return 2*number
print (double(number=4))


def list_product(list_of_numbers):
# We initialize the product to 1
    product = 1
# For each number in the list
    for number in list_of_numbers:
# We multiply the product with this number
        product *= number
    return product

test_list = [1, 0.12, -54, 12, 0.33, 12]
print(list_product(test_list))


def uniques(list_of_elements):
# We initialize the list of unique values
    unique_values = []
# For each item in the list
    for element in list_of_elements:
 # If the element is not in the list of unique values
        if element not in unique_values:
# We add it
            unique_values.append(element)

    return unique_values
print(uniques([1, 1, 2, 2, 2, 3, 3, "Hello"]))

#------------ function can have several parameters and several outputs.
#---------function power4, which takes as argument a number x
# and returns the first 4 powers of this number (i.e. 𝑥1,𝑥2,𝑥3,𝑥4)
def power4(x):
    return x**1, x**2, x**3, x**4
x_1, x_2, x_3, x_4 = power4(x = 8)
print(power4(x = 8))

#----function power_diff taking as argument 4 numbers x_1, x_2, x_3 and x_4
def power_diff(x_1, x_2, x_3, x_4):
    diff1 = x_2 - x_1
    diff2 = x_3 - x_2
    diff3 = x_4 - x_3

    return diff1, diff2, diff3
diff1, diff2, diff3 = power_diff(x_1, x_2, x_3, x_4)
print(diff1, diff2, diff3)


#--------------Documentation

help(len)

# The len function returns the number of elements in a container

def total_len(list_of_lists):
    """
    This function counts the total number of items in a list of lists.

    Parameters:
    -----------
    list_of_lists: A list of lists.

    Returns:
    --------
    n_elements: the total number of elements in list_of_lists.
    """
    # We initialize the number of elements to 0
    n_elements = 0

    # For each list in the list of lists
    for a_list in list_of_lists:
        # We count the number of elements in the list
        n_elements += len(a_list)

    return n_elements


test_list = [[1, 23, 1201, 21, 213, 2],
             [2311, 12, 3, 4],
             [11, 32, 1, 1, 2, 3, 3],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print("The list test_list contains", total_len(test_list), "elements.")
print("-------------------------------------------")

#--------------Recursion
def factorial(n):
    if n < 0:
        return "Negative number."  # Stops the function if the number is negative
# The simple case where n == 0
    if n == 0:
        return 1
    else:
 # We use the recurrence n! = n * (n-1)!
        return n * factorial(n - 1)
print(factorial(n=5))


def how_many_handshakes(N):
    """
    This function counts the number of handshakes
    needed for N persons to greet each other.
    """
    # If there are only 2 people
    if N == 2:
        # There can only be one handshake
        return 1
    # Otherwise
    else:
        # We count N-1 handshakes + the number of handshakes
        # between the remaining N-1 people
        return N-1 + how_many_handshakes(N-1)
print(how_many_handshakes(4))