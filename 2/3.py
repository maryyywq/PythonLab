import random
import string

# Создаем список всех возможных символов
characters = string.ascii_letters + string.digits
# Генерируем случайную строку
random_string = ''.join(random.choice(characters) for _ in range(8))
# Проверяем, содержит ли строка хотя бы одну цифру
while not any(char.isdigit() for char in random_string):
    random_string = ''.join(random.choice(characters) for _ in range(8))
# Выводим сгенерированную строку
print(random_string)
