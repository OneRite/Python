compressed_string = input("Введите сжатую строку: ")

original_string = ""
current_char = ""
repeat_count = ""

for char in compressed_string:
    if char.isalpha():
        if repeat_count:
            original_string += current_char * int(repeat_count)
        current_char = char
        repeat_count = ""
    else:
        repeat_count += char

if repeat_count:
    original_string += current_char * int(repeat_count)

print("Исходная строка:", original_string)
