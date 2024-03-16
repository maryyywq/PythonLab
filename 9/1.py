def print_data(data):
    print("№ ФИО                           Возраст  Группа")
    if len(data) != 0:
        for key in data:
            print(f"{key:<2}{data[key][0]:<30}{data[key][1]:<9}{data[key][2]:<10}")
    else:
        print("Данных нет")

def add_data(data):
    n = max(data.keys()) + 1
    data[n] = []
    name = input("Введите ФИО: ")
    data[n].append(name)
    age = input("Возраст: ")
    while (not age.isdigit()) or ("-" in age):
        age = input("Неверный ввод! Введите ещё раз: ")
    data[n].append(int(age))
    group = input("Введите группу: ")
    data[n].append(group)
    print("Успешно!")

data = {1: ["Иванов Иван Иванович", 23, "БО-111111"], 
       2: ["Сидоров Семен Семенович", 23, "БО-111111"], 
       3: ["Яшков Илья Петрович", 24, "БО-222222"]}

while True:
    print("Меню")
    print("1)Вывести данные")
    print("2)Добавить нового студента")
    print("3)Выход")
    s = input("Ваш выбор: ")
    while (not s.isdigit()) and (not ('1' <= s <= '3')):
        s = input("Неизвестная команда! Введите ещё раз: ")
    match s:
        case '1':
            print_data(data)
        case '2':
            add_data(data)
        case '3':
            break
print("Выход")
