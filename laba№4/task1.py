def count_unique_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)

# Получение ввода от пользователя
input_numbers = input("Введите числа через запятую: ")
numbers = [int(x) for x in input_numbers.split(",")]

print("Выходные значения:", count_unique_numbers(numbers))

