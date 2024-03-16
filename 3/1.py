input_string = input("Введите строку: ")
words = input_string.split()  # Разбиваем строку на слова
result = []  # Создаем пустой список для хранения слов с "ов"

for word in words:
    if word[-2:] == "ов":  # Проверяем две последние буквы слова
        result.append(word)  # Добавляем слово в список результатов

result_string = " ".join(result)  # Объединяем слова из списка в одну строку с пробелами

print("Результат:", result_string)
