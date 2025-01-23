i = 1
# While i is less than 5
while i <= 5:
# We print i
    print(i)
# We increase i by 1
    i += 1
print ("-----------------------------------")

results = [9.81, 9.89, 9.91, 9.93, 9.94, 9.95, 9.96, 9.97, 9.98, 10.03, 10.04, 10.05, 10.06, 10.08, 10.11, 10.23]
# The variable n will count the number of athletes who have
# 100m in less than 10 seconds
n = 0
# The variable i will iterate through the indexes of the results list
i = 0
# While i is less than the length of the list
while i < len(results):    #len() is a built-in function that returns the length
# if the result of the athlete at index i is less than 10
    if results[i] < 10:
# We increment n by 1
      n += 1
# We increment i by 1 to go to the next athlete
    i += 1
print("The number of athletes with a time less than 10s is", n)
print ("-----------------------------------")

bad_marks = [0, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 8, 8, 9, 10, 10, 10, 11, 12, 14]
# Computation of the class' average mark
total = 0
# We sum all the students' marks
for mark in bad_marks:
    total += mark
# The sum of the grades is divided by the number of students to obtain the average
average = total / 30
print("Initial average:", average)
# The average is 6.7, so we add 4 points to each student:
good_marks = []
# For each mark in bad_marks
for mark in bad_marks:
# We add the mark increased by 4 points to good_marks
    good_marks.append(mark + 4)
# Compute the new class average
total = 0
for mark in good_marks:
    total += mark
average = total / 30
print("Final average:", average)
print ("-----------------------------------")

text = ['The', '21', 'World', 'Cup', 'tournaments', 'have', 'been', 'won', 'by', 'eight',
        'national', 'teams.', 'Brazil', 'have', 'won', 'five', 'times', ',', 'and',
        'they', 'are', 'the', 'only', 'team', 'to', 'have', 'played', 'in', 'every', '.']
# The number of times the character 'e' appears
# will be stored in the variable n
n = 0
# For each word in the text
for word in text :
# For each letter in word
    for letter in word :
# If the letter is 'e'
        if letter == 'e':
# We increase n by 1
            n += 1
print("The character 'e' appears", n, "times in the text.")
print ("-----------------------------------")

#------------range function
# The first two terms of the Fibonnaci Sequence
u = [0, 1]
# For i going from 2 to 5
for i in range(2, 5):
# We compute u_i with u[i-1] and u[i-2]
    u_i = u[i - 1] + u[i - 2]
# We add u_i at the end of the list u
    u.append(u_i)
    print(u_i)
print ("-----------------------------------")

#------------List comprehension-----------------
# The list of numbers for the last two questions
numbers_list = [10, 12, 7, 3, 26, 2, 19]

powers_three = [3**k for k in range(10)]
print(numbers_list)

double_list = [number*2 for number in numbers_list]
print(numbers_list)
even_list = ["even" if number%2 == 0 else "odd" for number in numbers_list]
print(numbers_list)
print ("-----------------------------------")
#-------------enumerate function-------------------------
L = [22, 65, 75, 93, 64, 47, 91, 53, 86, 53, 88, 17, 94, 39]
maximum=0
max_index=0
# For each element in the list L
for index, element in enumerate(L):
# If the element is greater than those we have seen before
    if element > maximum:
# We overwrite the maximum with its value
        maximum = element
        max_index = index
print("The maximum of the list is at the index", max_index)
print("Its value is", maximum)
print ("-----------------------------------")
#------------zip function
incomes = [1200, 2000, 1500, 0, 1000, 4500, 1200, 500, 1350, 2200, 1650, 1300, 2300]
expenses = [1000, 1700, 2000, 700, 1200, 3500, 200, 500, 1000, 3500, 1350, 1050, 1850]
savings = []

for income, expense in zip(incomes, expenses):
    saving = income - expense
    savings.append(saving)
print(savings)

