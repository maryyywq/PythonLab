def print_data(data):
    print("№ ФИО                           Возраст  Группа")
    if len(data) != 0:
        for key in data:
            print(f"{key:<2}{data[key][0]:<30}{data[key][1]:<9}{data[key][2]:<10}")
    else:
        print("Данных нет")

def change_data(data):
    if len(data) != 0:
        n = input("Введите номер студента: ")
        while n not in [str(x) for x in data.keys()]:
            n = input("Такого номера нет! Введите ещё раз: ")
        n = int(n)
        print("Выберете поле, которое вы хотите изменить")
        print('1)ФИО')
        print('2)Возраст')
        print('3)Группа')
        s = input("Ваш выбор: ")
        while s != '1' and s != '2' and s != '3':
            s = input("Неизвестная команда! Введите ещё раз: ")
        match s:
            case '1':
                data[n][0] = input("Новое ФИО: ")
            case '2':
                age = input("Новый возраст: ")
                while (not age.isdigit()) or ("-" in age):
                  age = input("Неверный ввод! Введите ещё раз: ")
                data[n][1] = int(age)
            case '3':
                data[n][2] = input("Новая группа: ")
    else:
        print("Данных нет!")

data = {1: ["Иванов Иван Иванович", 23, "БО-111111"], 
       2: ["Сидоров Семен Семенович", 23, "БО-111111"], 
       3: ["Яшков Илья Петрович", 24, "БО-222222"]}

while True:
    print("Меню")
    print("1)Вывести данные")
    print("2)Изменить данные о студенте")
    print("3)Выход")
    s = input("Ваш выбор: ")
    while (not s.isdigit()) and (not ('1' <= s <= '3')):
        s = input("Неизвестная команда! Введите ещё раз: ")
    match s:
        case '1':
            print_data(data)
        case '2':
            change_data(data)
        case '3':
            break
print("Выход")
