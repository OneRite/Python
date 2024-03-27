input_string = input("Введите строку: ")
compressed_string = ""

current_char = input_string[0]
count = 1

for i in range(1, len(input_string)):
    if input_string[i] == current_char:
        count += 1
    else:
        if count > 1:
            compressed_string += current_char + str(count)
        else:
            compressed_string += current_char
        current_char = input_string[i]
        count = 1

if count > 1:
    compressed_string += current_char + str(count)
else:
    compressed_string += current_char

print("Сжатая строка:", compressed_string)
