def abbreviation(phrase):
    # Разбиваем строку на слова
    words = phrase.split()

    # Извлекаем первую букву каждого слова и преобразуем в верхний регистр
    acronym = ''.join(word[0].upper() for word in words)

    return acronym

# Ввод строки от пользователя
phrase = input("Введите строку: ")

# Генерация аббревиатуры и вывод результата
acronym = abbreviation(phrase)
print("Аббревиатура:", acronym)
