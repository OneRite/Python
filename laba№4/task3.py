def check_city(city, cities_list):
    if city in cities_list:
        return "REPEAT"
    else:
        cities_list.append(city)
        return "OK"

# Считываем количество городов
n = int(input())

# Список для хранения названных городов
cities = []

# Считываем названия городов и проверяем их
for _ in range(n):
    city = input()
    result = check_city(city, cities)
    print(result)
