#Expression 	Example 	Meaning
# < 	x < y 	Is x less than y?
# <= 	x <= y 	Is x lesser or equal to y?
# > 	x > y 	Is x greater than y?
# >= 	x >= y 	Is x greater or equal to y?
# == 	x == y 	Is x equal to y?
# != 	x != y 	Is x different from y?

number = -2
if number == 0:
    print ("This number is 0.")
elif number > 0:
    print ("This number is positive.")
else:
    print ("This number is negative.")

size = 205
if size < 160:
    print("This person is small.")
elif 160 <= size < 180:
    print("This person is of medium height.")
elif 180 <= size < 200:
    print("This person is very tall.")
else:
    print("This person is very, very tall.")

#redouble
average=5
if average < 10:
    repeating = True
else:
     repeating = False
redouble = True if average < 10 else False