
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from gbfunctions import give_int

# def prime_number(n: int) -> bool:
#     '''
#     Checking a set of numbers for primes
#     Args: int number
#     Returns: True / False
#     '''
#     for second_occurrence in range(2, n+1):
#         print(n, second_occurrence, 'current')
#         if second_occurrence == n:
#             print(n, second_occurrence, 'True')
#             return True
#         if not (n % second_occurrence): 
#             print(n, second_occurrence, 'False')
#             return False


def prime_number(n: int) -> bool:
    '''
    Checking (eliminating) a set for prime numbers
    Args: int number
    Returns: True / False
    '''
    for fake_entry in range(2, n):
        if not (n % fake_entry):
            print(n, fake_entry, 'False')
            return False
    print(n, 'True')
    return True

a = 'Введите натуральное число N: \n'

num = abs(give_int(a))
short_list = [entry for entry in range(2, num + 1) if not (num % entry) and prime_number(entry)]
print('N = ', num, ' -> ', short_list)
