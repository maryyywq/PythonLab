my_string = "ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;21 год;Студент 2 курса"

# Разбиваем строку на элементы
elements = my_string.split("_")

# Выводим информацию о студентах, чьи фамилии начинаются на "А" или "Б"
for i in range(1, len(elements)):
    student_info = elements[i].split(";")
    fio = student_info[0].split()
    if fio[0][0] == "А" or fio[0][0] == "Б":
        print("ФИО:", " ".join(fio))
        print("Возраст:", student_info[1])
        print("Категория:", student_info[2])
        print()
