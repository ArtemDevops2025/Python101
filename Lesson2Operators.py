#Expression 	Example 	Meaning
# + 	Addition 	6+4 returns10
# - 	Subtraction 	6-4 returns2
# * 	Multiplication 	6*4 returns24
# / 	Real division 	6 / 4 returns1.5
# // 	Floor division 	6.0 // 4 returns1
# ** 	Exponentiation 	6 ** 4 returns1296
# % 	Modulus 	6 % 4 returns2



# Distance in km between Paris and Marseille
distance = 750
# Average speed of a walker in km/h
speed = 4.8
# Time in hours it would take to go from Paris to Marseille without stopping
time = distance/speed
# Number of days of walking
days = time // 24
# Number of hours remaining
hours_remaining = time % 24
print("The walker would need", days, "days and", hours_remaining, "hours.")

prime_numbers = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
x = prime_numbers[0]
# We square x
x **= 2
# We add 17 to x
x += 17
# We keep the remainder of the floor division of x by 12
x %= 12
print(x)
# The magician is right

#determine with a boolean value if 7 divides 37+214.
print((3**7 + 2**14) % 7 == 0)

# determine if 7 divides 32𝑛+1+24𝑛+2 for 𝑛=4,5 and 10.
n = 4
x = 3**(2*n + 1) + 2**(4*n + 2)
print(x % 7 == 0)
n = 5
x = 3**(2*n + 1) + 2**(4*n + 2)
print(x%7 == 0)
n = 10
x = 3**(2*n + 1) + 2**(4*n + 2)
print(x%7 == 0)

#Membership operators: not in, IN
excerpt = [ 'France','each', ';and', 'England', 'and', 'Spain', ',', 'with', 'one', 'title', 'each', '.']
# Is France mentionned in the excerpt?
print("France" in excerpt)
# Is Croatia NOT mentionned in this exceprt?
print("Croatie" not in excerpt)
print("Croatie1" in excerpt)