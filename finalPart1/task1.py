import csv
import os
import random

class TitanicDataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data

    def show(self, output_type='top', num_rows=5, separator=','):
        if output_type == 'top':
            rows = self.data[:num_rows]
        elif output_type == 'bottom':
            rows = self.data[-num_rows:]
        elif output_type == 'random':
            rows = random.sample(self.data, num_rows)
        else:
            print("Ошибка 1")
            return

        for row in rows:
            print(separator.join(row))

    def info(self):
        headers = self.data[0]
        data = self.data[1:]
        
        num_rows = len(data)
        num_columns = len(headers)
        print(f"Количество строк x столбцов: {num_rows}x{num_columns}")

        for i, header in enumerate(headers):
            non_empty_values = sum(1 for row in data if row[i])
            data_type = type(data[0][i]).__name__ if non_empty_values > 0 else "empty"
            print(f"{header:<10} {non_empty_values:<5} {data_type}")

    def del_nan(self):
        self.data = [row for row in self.data if all(field for field in row)]

    def make_ds(self):
        self.del_nan()
        random.shuffle(self.data)
        num_rows = len(self.data)
        split_index = int(0.7 * num_rows)

        learning_data = self.data[:split_index]
        testing_data = self.data[split_index:]

        learning_dir = "workdata/Learning"
        testing_dir = "workdata/Testing"

        try:
            os.makedirs(learning_dir, exist_ok=True)
            os.makedirs(testing_dir, exist_ok=True)

            with open(os.path.join(learning_dir, "train.csv"), 'w', newline='') as train_file:
                writer = csv.writer(train_file)
                writer.writerows(learning_data)

            with open(os.path.join(testing_dir, "test.csv"), 'w', newline='') as test_file:
                writer = csv.writer(test_file)
                writer.writerows(testing_data)

            print("Наборы данных")
        except Exception as e:
            print(f"Ошибка 2 {e}")

# Пример использования:

processor = TitanicDataProcessor("/Users/ruslan/Documents/GitHub/Python/finalPart1/Titanic.csv")

print("Показаны первые 5 строк:")
processor.show(output_type='top')

print("\nПоказаны нижние 5 строк:")
processor.show(output_type='bottom')

print("\nПоказаны случайные 5 строк:")
processor.show(output_type='random')

print("\nИнформация о данных:")
processor.info()

print("\nУдаление строк со значениями NaN")
processor.del_nan()

print("\nСоздание наборов данных для чтения и тестирования")
processor.make_ds()

print("\nВсе работает!!!")


