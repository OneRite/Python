import json

try:
    with open('/Users/ruslan/Documents/GitHub/Python/laba№5/input.json', 'r') as f:
        data = json.load(f)

    # Получаем список пользователей из JSON
    users = data["users"]

    # Создаем заголовок CSV, используя ключи первого пользователя
    header = ",".join(users[0].keys())

    # Формируем строки CSV
    rows = []
    for user in users:
        row = ",".join(str(value) for value in user.values())
        rows.append(row)

    # Собираем весь CSV-файл
    csv_content = header + "\n" + "\n".join(rows)

    # Выводим содержимое CSV на экран
    print(csv_content)

    # Записываем содержимое CSV в файл output.csv
    with open('/Users/ruslan/Documents/GitHub/Python/laba№5/output.csv', 'w') as f:
        f.write(csv_content)

except Exception as ex: 
    print(f'Ошибка: {str(ex)}')
