import random

# Создаем список из 10 элементов
original_list = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", original_list)

# Добавляем 5 новых элементов
for _ in range(5):
    original_list.append(random.randint(1, 100))

# Оставляем все нечетные элементы
odd_elements = [x for x in original_list if x % 2 != 0]

# Выводим итоговый список на экран
print("Итоговый список с нечетными элементами:", odd_elements)