string = input("Введите строку: ")
digits_string = ""
letters_string = ""
for char in string:
    if char.isdigit():
        digits_string += char
    elif char.isalpha():
        letters_string += char
print(digits_string)
print(letters_string)