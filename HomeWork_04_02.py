# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from gbfunctions import give_int
a = 'Введите наибольшее число в последовательности: \n'
max_num = give_int(a)

# base_list = []
# for i in range(0, max_num):
#     for j in range(0, max_num-i,):
#         base_list.append(i+1)

base_list = [i for i in range(1, max_num + 1) for j in range(0, max_num - i+1)]

unique_list = []
[unique_list.append(i) for i in base_list if i not in unique_list]
print(base_list, ' - > ', unique_list)