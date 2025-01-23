# Definition of name_function which returns the first name given as an argument after 10 seconds of waiting
import asyncio
import time

async def example():  # We define the coroutine with async def

 print("We are trying out coroutines.")

def name_function(firstname):
    name = firstname
    time.sleep(10)
    print(name)

# Definition of the main function which displays the execution completion time of name_function
# for three different arguments

def main():
    print("Name :")
    start_time = time.time()
    name_function('Daniel')
    name_function('Donna')
    name_function('Diane')
    end_time = time.time()
    print("Total running time : %.2f seconds" % (end_time - start_time))

main()

# Definition of the name_async coroutine which in return displays the first name
# given in argument after 10 seconds of waiting

async def name_async(firstname):
    name = firstname
    await asyncio.sleep(10)
    print(name)

# Definition of the main coroutine which displays the execution completion time of the
# function for three different arguments

async def main():
    print("\nCoroutine :")
    start_time = time.time()
    await asyncio.gather(name_async('Daniel'), name_async('Donna'), name_async('Diane'))
    end_time = time.time()
    print("Total running time : %.2f seconds" % (end_time - start_time))
    await main()

# We notice that the execution time is divided by three.