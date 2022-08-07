import random
import numpy as np
MESSAGE = """Press "A" to get a random integer.
Press "B" to toss a coin.
Or enter an integer. It will return its factorial (n!).
Press "E" to exit.
"""
def get_factorial(value: int):
    '''Returns the factorial of the input value.'''
    list_values = np.arange(1, value + 1)
    factorial = list_values.prod()
    return factorial
def get_rand():
    '''Returns a random integer.'''
    """TODO: Add your code here 
        Hint: Using random.randint() function.
    """
    my_randint = random.randint(1, 100)
    return my_randint
def toss_coin():
    '''Return either Head or Tail'''
    """TODO: Add your code here
        Hint: Using random.randint() function.
    """
    numerop = random.randint(0, 1)
    if numerop == 0:
        return("Tail")
    coin = 'Head'
    return coin
def read_input():
    my_input = input(MESSAGE)
    if my_input.lower() == 'e':
        exit()
    elif my_input.lower() == 'a':
        res = get_rand()
        print(res)
    elif my_input.lower() == 'b':
        res = toss_coin()
        print(res)
    elif my_input.isnumeric():
        res = get_factorial(int(my_input))
        print(f'{my_input}! = {res}')
    else:
        print(f'{my_input} is not a valid integer!')
    read_input()
if __name__ == '__main__':
    print('This is a toy toolbox.\nIt can do the following:')
    read_input()

""" Hey man really cool code bro"""