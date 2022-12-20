import random

def random_list_min_max(list_length, min, max):
    '''
    \n****
    \nAccepts an empty list and the number of elements of the future list,
    \nreturns a list filled with random numbers
    \n****
    \nParameters: list length, minimum and maximum values
    \nReturns: a list of random numbers
    \n****
    '''
    numbers = []
    for i in range(list_length):
        numbers.append(random.randint(min, max))
    return numbers    

def random_list(list_length):
    '''
    \n****
    \nAccepts an empty list and the number of elements of the future list,
    \nreturns a list filled with random numbers
    \n****
    \nParameters: list length
    \nReturns: a list of random numbers
    \n****
    '''
    numbers = []
    for i in range(list_length):
        numbers.append(random.randint(0, 99))
    return numbers    

def give_int(a: str) -> int:
    n = int(input(a))
    return n
