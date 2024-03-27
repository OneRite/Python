def count(text):
    word_counts = {}  # Создаем пустой словарь для подсчета встреч слов

    # Разбиваем строку на слова и проходим по каждому слову
    words = text.split()
    result = []
    for word in words:
        # Если слово уже встречалось ранее, выводим количество вхождений
        if word in word_counts:
            result.append(str(word_counts[word]))
        else:
            result.append('0')

        # Увеличиваем количество вхождений слова в словаре
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return ' '.join(result)  # Возвращаем результат в виде строки


# Получаем текст от пользователя
input_text = input("Введите текст: ")

# Выводим результат подсчета встреч слов
print("Вывод программы:", count(input_text))
