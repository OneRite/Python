def sort_words(text):
    # Разбиваем текст на слова и подсчитываем количество вхождений каждого слова
    word_counts = {}
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Сортируем слова по убыванию их количества появления, а при одинаковой частоте появления — в лексикографическом порядке
    sorted_words = sorted(word_counts.keys(), key=lambda x: (-word_counts[x], x))

    # Выводим отсортированные слова по одному на каждую строку
    for word in sorted_words:
        print(word)

# Получаем текст от пользователя
text = input("Введите текст: ")

# Вызываем функцию для сортировки слов и вывода результата
sort_words(text)
