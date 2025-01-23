
#For a list, we use square brackets: []
my_list = [4, -1, 2, -3, 3]

# Update the elements of the list
my_list[0] = -3
my_list[1] = -1
my_list[2] = 2
my_list[3] = 3
my_list[4] = 4

# Display the list
print(my_list)
a_long_list = [-16, 6, -4, -18, 18, 20, 21, -6, 19, 25, 11,
               2, 9, 7, -16, 16, 4, -15, 11, 7, 17, 18, 4,
               25, 17, 28, -6, 17, 1, 14, -20, -15, 20, -15,
               -8, 8, -19, -11, -20, -16, 3, 3, -10, -5, 10,
               24, -1, 1, -10, 6, 10, -6, -14, 25, 8, -11,
               -17, -9, 0, 21, 3, 14, 7, 10, 25, 24, -18, -11,
               2, 29, 17, -6, 6, -11, 2, -18, 20, -15, -11,
               15, -10, 8, -15, 25, -15, 10, 28, -12, 11, 14,
               27, -1, 10, -2, -15, -10, 19, 26, 3, 27]

# Display the 10 first elements
print(a_long_list[:10])
# Display the last 10 elements
print(a_long_list[-10:])


my_list = [1, 5, "Hello", -1.4, "how", 103, "are", "you"]
# Deletion of "Hello" which is at the 3rd position (index 2)
my_list.pop(2)
# Deletion of "how" which is at the 4th position (index 3)
my_list.pop(3)
# Deletion of "are" which is at the second to last position
my_list.pop(-2)
# Deletion of "you" which is at the last position
my_list.pop(-1)
# Display of the list
print(my_list)


my_list = [1, 5, "Hello", -1.4, "how", 103, "are", "you"]
# Removal of numbers
my_list.pop(0)
my_list.pop(0)
my_list.pop(1)
my_list.pop(-3)
# Insertion of the elements "Bonjour", "comment", "ça" and "va"
my_list.insert(1, "Bonjour")
my_list.insert(3, "comment")
my_list.insert(5, "ça")
my_list.insert(7, "va")
# Display of the list
print(my_list)


x = 0
a_list = [x]
x = x + 1
a_list.append(x)
print(a_list)


### Merging 2 lists with the extended method
list_1 = ["Hello", "how", "are", "you", "?"]
list_2 = ["Fine", "and", "you", "?"]
# Merging the elements of list_2 with list_1
list_1.extend(list_2)
# Display of list_1
print(list_1)

### Merging 2 lists with the + operator
list_1 = ["Hello", "how", "are", "you", "?"]
list_2 = ["Fine", "and", "you", "?"]
# Merging the elements of list_2 with list_1
list_1 = list_1 + list_2
print(list_1)