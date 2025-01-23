from threading import Thread
import time

def sleep_3():
    time.sleep(3)
    print("I am executed in 3 seconds")

def sleep_2():
    time.sleep(2)
    print("I am executed in 2 seconds")

# Sequential execution
t1 = time.time()  # We start the time measurement
sleep_3()  # The sleep_3 function is executed
sleep_2()  # The sleep_2 function is executed
t2 = time.time()  # We stop the measurement of time
print("\nCompletion of the program in sequence takes : ", t2 - t1, "\n")

# Threaded execution

th1 = Thread(target=sleep_3)  # First thread with the sleep_3 function
th2 = Thread(target=sleep_2)  # Second thread with the sleep_2 function
t1 = time.time()  # We start the time measurement
th1.start()  # We start the 1st thread
th2.start()  # We start the 2nd thread
th1.join()  # We ensure the completion of thread 1
th2.join()  #We ensure the completion of thread 2
t2 = time.time()  # We stop the measurement of time
print("\nCompletion of the threaded program takes: ", t2 - t1)

print("--------------------------------------------------")

import wikipedia

# The language of choice is defined
wikipedia.set_lang("en")

# We define a list of page titles whose content we wish to obtain
pages = ["Multithreading (computer architecture)", "Threading", "Concurrent programming"]

# We define a function that returns the first line of each wikipedia page
# whose name appears in the list of pages defined above
def wikipedia_function(page):
    wiki = wikipedia.page(page)
    text = wiki.content
    print("\n", page, ' : ', text.split('.', 1)[0], "\n")
t1 = time.time()  # We start the time measurement

# Sequential launch using a loop
for page in pages:
    wikipedia_function(page)
t2 = time.time()  # We stop the measurement of time
print(" \n Duration: ", (t2 - t1))

print("_______________________________________")


# We define the calcul_while function
def calculation_while(x):
    while x > 0:
        x -= 1

# We define the list of values
numbers = [
    5000000, 3000000, 6000000, 4000000, 320000000, 2000000, 50000000, 10000000
]

t1 = time.time()  # We start the time measurement

# sequentially executed

for nb in numbers:
    calculation_while(nb)

t2 = time.time()  # We stop the measurement of time

print("Duration in sequential : ", t2 - t1)
# Solution 1
from multiprocessing import Pool
t1 = time.time()  # We start the time measurement
pool = Pool()  # Processes are created

# Execution is distributed between the cores
result = pool.map(calculation_while, numbers)
t2 = time.time()  # We stop the time measurement
print("Duration of the solution 1 : ", t2 - t1)

# Solution n°2

# The syntax of the Process class resembles that of the Thread class in every way class of the threading library
from multiprocessing import Process

# Processes are created
processes = [Process(target=calculation_while, args=(nb, )) for nb in numbers]
t1 = time.time()  # We stop the time measurement

if __name__ == '__main__':

    # We start the threads
    for process in processes:
        process.start()

    # We ensure the completion of the threads
    for process in processes:
        process.join()

t2 = time.time()  # We stop the time measurement

print("Duration of the solution 2 : ", t2 - t1)
# The times are roughly equivalent between the solutions.
# The Process class and the Pool class are not equivalent.
# The use of the Pool class will be more appropriate for a large number of tasks
# that will be distributed between the cores (specified number).
# The Process class is more appropriate for a limited number of tasks.
# The completion time is much shorter than that obtained with sequential execution.
