import numpy as np
import sys

stack = np.array([])

def push(value):
    global stack
    stack = np.append(stack, value)

def pop():
    global stack
    if len(stack)>0:
        stack = np.delete(stack, -1)
    else:
        print('stack is empty nothing to display')

def display():
    if len(stack)>0:
        print(stack)
    else:
        print('stack is empty - nothing to display')
    print('stack is of',stack.nbytes)

while True:
    print('Options')
    print('1. push')
    print('2. pop')
    print('3. display')
    print('4. exit')

    option = int(input())
    if option == 1:
        value = int(input())
        push(value)
    elif option == 2:
        pop()
    elif option == 3:
        display()
    elif option == 4:
        sys.exit()
    else:
        print('please enter a valid option')
