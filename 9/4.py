def print_data(data):
    if len(data) != 0:
        n = input("Введите номер студента: ")
        while n not in [str(x) for x in data.keys()]:
            n = input("Такого номера нет! Введите ещё раз: ")
        n = int(n)
        print("№ ФИО                           Возраст  Группа")
        print(f"{n:<2}{data[n][0]:<30}{data[n][1]:<9}{data[n][2]:<10}")
    else:
        print("Данных нет")

data = {1: ["Иванов Иван Иванович", 23, "БО-111111"], 
       2: ["Сидоров Семен Семенович", 23, "БО-111111"], 
       3: ["Яшков Илья Петрович", 24, "БО-222222"]}

while True:
    print("Меню")
    print("1)Вывести данные об определенном студенте")
    print("2)Выход")
    s = input("Ваш выбор: ")
    while (not s.isdigit()) and (not ('1' <= s <= '2')):
        s = input("Неизвестная команда! Введите ещё раз: ")
    match s:
        case '1':
            print_data(data)
        case '2':
            break
print("Выход")
