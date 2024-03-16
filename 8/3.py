lst = [[1, "Иванов Иван Иванович", 23, "БО-111111"], [2, "Сидоров Семен Семенович", 23, "БО-111111"], [3, "Яшков Илья Петрович", 24, "БО-222222"]]

# Создаем словарь, где ключ - это номер студента, а значение - список с информацией о студенте
res = {x[0]: x[1:] for x in lst}

# Меню для пользователя
while True:
    print("\nМеню:")
    print("1. Изменить ФИО студента")
    print("2. Поиск по ФИО студента")
    print("3. Вывести список студентов (с номерами 1-10)")
    print("4. Выйти из программы")
    choice = input("Выберите действие (1, 2, 3, 4): ")

    if choice == "1":
        old_name = input("Введите старое ФИО студента: ")
        new_name = input("Введите новое ФИО студента: ")
        for key, value in res.items():
            if value[0] == old_name:
                value[0] = new_name
                break
    elif choice == "2":
        search_name = input("Введите ФИО студента для поиска: ")
        found = False
        for key, value in res.items():
            if value[0] == search_name:
                print(f"Найден студент с номером {key}: {value}")
                found = True
                break
        if not found:
            print("Студент не найден.")
    elif choice == "3":
        print("Список студентов с номерами 1-10:")
        for key in range(1, 11):
            if key in res:
                print(f"{key}: {res[key]}")
            else:
                print(f"{key}: Нет информации")
    elif choice == "4":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

print("Программа завершена.")
