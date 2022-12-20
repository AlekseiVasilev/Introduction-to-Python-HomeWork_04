# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

from gbfunctions import give_int
from pathlib import Path
from tempfile import NamedTemporaryFile

def capital_letters(rating_list, rating: str):
    '''
    Accepts a file with grades and uppercases the students with the required grade
    Arguments: file with grades, rating
    '''
    with rating_list.open(encoding='UTF8') as file, NamedTemporaryFile('w', dir = str(rating_list.parent), delete=False) as output_file:
        for line in file:
            persona = str(line.strip())
            print(persona.upper() if line.strip()[-1] == rating else persona, file = output_file)
    Path(output_file.name).replace(rating_list)

rating = str(give_int('Введите '))
rating_list = Path('HomeWork_04\data_HomeWork_04_03.txt')

capital_letters(rating_list, rating)