# dir(list)
# help(list)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1.reverse() # reverses the order of the elements of the list calling it.
                 # this method WILL MODIFY the list that calls it.
print(list_1)
print("---------------------------------")

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2.insert(4, 10) # inserts the value 10 at the index 4 (fifth position in Python) of the list.
print(list_2)
print("---------------------------------")

list_3 = [5, 2, 4, 9, 6, 7, 8, 3, 10, 1]
list_3.sort() # sorts the element of a list in increasing order.
              # this method WILL MODIFY the list that calls it.
print(list_3)
print("---------------------------------")



