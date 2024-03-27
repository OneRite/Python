def count_items_purchased(records):
    purchases = {}  # Создаем пустой словарь для хранения покупок каждого покупателя

    # Проходим по каждой записи о покупке
    for record in records:
        # Разбиваем запись на отдельные части: ID покупателя, товар и количество
        customer_id, item, quantity = record.split()

        # Преобразуем ID покупателя и количество в целые числа
        customer_id = int(customer_id)
        quantity = int(quantity)

        # Добавляем запись о покупке в словарь покупок
        if customer_id in purchases:
            purchases[customer_id].append((item, quantity))
        else:
            purchases[customer_id] = [(item, quantity)]

    # Возвращаем словарь покупок
    return purchases

# Получаем количество записей о покупках
n = int(input("Введите количество записей о покупках: "))

# Считываем записи о покупках
records = []
for _ in range(n):
    record = input("Введите запись о покупке (ID Покупателя Товар Количество): ")
    records.append(record)

# Получаем словарь покупок
purchases = count_items_purchased(records)

# Выводим список покупок для каждого покупателя
for customer_id, items in purchases.items():
    print("Покупатель ID", customer_id, "сделал следующие покупки:")
    for item, quantity in items:
        print("- Товар:", item, "| Количество:", quantity)
