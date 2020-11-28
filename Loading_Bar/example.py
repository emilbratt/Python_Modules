#!/usr/bin/env python3
# Emil Bratt -> emilbratt@gmail.com
from doubleload import Loadbar
import random
from time import sleep

'''
    the usage is pretty simple
    call the Loadbar object
    for example: myload = Loadbar('name of task',N) where N is the number of total iterations

    throw in the object in a for loop and have it display the progress
    with the display method and watch some fancy animation

    example:
    for i in range(myload.iterations()):
        "do something with i or some other stuff"
        "feed i into the display method"
        myload.display(i)
'''

# throw a list togheter with a random amount of tasks
allNumbers = []
for i in range(0,random.randint(1,3300)):
    allNumbers.append(i)

# find the total amount of object that you are iterationg through
totalOperations = len(allNumbers)

# depending on number of items, introduce a little delay between each iteration
# for the sake of showing the loadbar
if totalOperations < 3:
    delay = lambda : sleep(0.5)
elif totalOperations < 4:
    delay = lambda : sleep(0.05)
else:
    delay = lambda : sleep(0.005)

# call the module and give it a name and the total amount of operations
mytask = Loadbar('Collect multiples of 7', totalOperations)


# simulate a task
myFavoriteNumbers = []
for i in range(mytask.iterations()):
    mytask.display(i)
    if i%7 == 0:
        myFavoriteNumbers.append(i)
    delay()

print('Complete')
print(myFavoriteNumbers)

# example calling Loadbar with all options:
# taskname, totallaps, clearscreenafterdone, headLeft, headRight, eatLeft, eatRight, trailLeft, trailRight
myothertask = Loadbar('Look, I have options!', totalOperations,'clear','<','>','(',')','-','-')
