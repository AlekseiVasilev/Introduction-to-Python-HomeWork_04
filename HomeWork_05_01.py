
# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

text = 'Пугать ты галок пугай'
search_text = 'пугай'


text = list(text.split(' '))
mod_text = ' '.join(list(filter(lambda x: x != search_text, text)))

print(text, mod_text)

