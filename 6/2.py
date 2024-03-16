def func_1():
    print("Первая функция: ")
    a = int(input("Введите переменную a: "))
    b = int(input("Введите переменную b: "))
    c = int(input("Введите переменную c: "))
    d = int(input("Введите переменную d: "))
    f = int(input("Введите переменную f: "))
    try: 
        y = abs(a - b * c * d**3 + (c**5 - a**2)/a +f**3 *(a - 213))
    except:
        print("Ошибка! Деление на ноль")
    else: 
        print(f"Результат:{y}")

def func_2():
    print("Вторая функция: ")
    a = []
    print("Вводите элементы списка(для окончания ввода используется пустая строка):")
    while (s := input()) != "":
        a.append(s)
    print("Нечетные элементы:")
    for i in a:
        if i.isdigit() and int(i) % 2 != 0:
            print(i)

def func_3():
    print("Третья функция: ")
    a = []
    pr = 1
    print("Вводите элементы списка(для окончания ввода используется пустая строка):")
    while (s := input()) != "":
        a.append(int(s))
    for i in [x for x in a if x < 10]:
        pr *= i
    print(f"Результат умножения всех чисел меньше 10: {pr}")

def func_4():
    print("Четвертая функция: ")
    a = []
    print("Вводите элементы списка(для окончания ввода используется пустая строка):")
    while (s := input()) != "":
        a.append(int(s))

    medium = a[len(a) // 2]
    print(f"Средний элемент массива: {medium}")

def main_menu():
    while True:
        print("Меню")
        print("0 - Выход из программы")
        print("1 - Вызов первой функции")
        print("2 - Вызов второй функции")
        print("3 - Вызов третьей функции")
        print("4 - Вызов четвертой функции")
        choice = input("Выберите действие: ")
        if choice == '0':
            break
        elif choice == '1':
            func_1()
        elif choice == '2':
            func_2()
        elif choice == '3':
            func_3()
        elif choice == '4':
            func_4()
        else:
            print("Некорректный ввод. Попробуйте снова.")
        
        continue_execution = input("Вы хотите продолжить? (yes/no): ")
        if continue_execution.lower() not in ['yes', 'y', '1']:
            break

main_menu()
