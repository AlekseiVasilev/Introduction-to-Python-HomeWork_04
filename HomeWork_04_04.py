# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ,
# считывает текст и дешифровывает его.

import string
from gbfunctions import give_int

def cesar_crypt(text: str, key: int, decrypt=False):
    '''
    Accepts text in Russian / English and encodes / decodes with a character shift
    Arguments: Text: str, Key: int
    '''
    new_text = ''
    key = key if not decrypt else - key
    for index, letter in enumerate(text): #.lower() - Return a copy of the string with all the cased characters 4 converted to lowercase.
        use_abc = rus_abc if letter in rus_abc else eng_abc
        letter_index = use_abc.find(letter)
        new_place = (letter_index+key) % len(use_abc)
        print(use_abc[letter_index], '-', letter_index, '/', use_abc[new_place], '-', new_place, '/', letter)
        if letter in use_abc:
            new_text += use_abc[new_place]
        else:
            new_text += letter
    return new_text

eng_abc = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
rus_abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' + 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #неправильно декодировало из-за повторного набора символов string.punctuation

text = 'Zoo time is she and you time \
 The mammals are your favourite type, and you want her tonight \
 Heartbeat, increasing heartbeat \
 You hear the thunder of stampeding rhinos, elephants and tacky tigers'

# text = 'Время зоопарка - она ​​и у вас время \
#  Млекопитающие - ваш любимый тип, и вы хотите ее сегодня вечером \
#  Сердцебиение, увеличивая сердцебиение \
#  Вы слышите громом штамповки носорогов, слонов и липких тигров'

print(list(enumerate(eng_abc, start=0)))
print(list(enumerate(rus_abc, start=0)))

a = 'Введите длину ключа:\n'
cesar_key = give_int(a)

crypted_text = cesar_crypt(text, cesar_key, decrypt=False)
print(crypted_text)
encrypted_text = cesar_crypt(crypted_text, cesar_key, decrypt=True)
print(encrypted_text)

