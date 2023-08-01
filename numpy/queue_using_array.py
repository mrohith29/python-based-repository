import numpy
import sys

queue = numpy.array([])

def enqueue(value):
    global queue
    queue = numpy.append(queue, value)

def dequeue():
    global queue
    if len(queue) == 0:
        print('queue is empty and nothing to delete')
    else:
        queue = numpy.delete(queue, 0)

def display():
    global queue
    if len(queue) == 0:
        print('queue is empty nothing to display')
    else:
        print(queue)

while True:
    print('Select the option')
    print('1. enqueue')
    print('2. dequeue')
    print('3. display')
    print('4. exit')
    option = int(input())
    if option == 1:
        value = int(input())
        enqueue(value)
    elif option == 2:
        dequeue()
    elif option == 3:
        display()
    elif option == 4:
        sys.exit()
    else:
        print("invalid choice - please select a correct choice")