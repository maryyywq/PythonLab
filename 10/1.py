matr = [[1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2]]

def multiplication():
    for i in matr:
        pr = 1
        for j in range(0, len(i)):
            pr *= i[j]
        print(i, ' = ', pr, sep='')

def sum():
    summa = 0
    for i in matr:
        for j in range(0, len(i)):
            summa += i[j]
    return summa

def sumIf():
    sum1 = 0
    sum2 = 0
    for i in matr:
        for j in range(0, len(i)):
            if i[j] < 5:
                sum1 += i[j]
            else:
                sum2 += i[j]
    if sum1 > sum2:
        return sum1
    else:
        return sum2

def nullElements():
    for i in matr:
        for j in range(0, len(i)):
            i[j] = 0

while True:
    print("\nМеню:")
    print("1. Умножить элементы в каждой строке")
    print("2. Вычислить сумму всех элементов")
    print("3. Сравнить сумму элементов меньше 5, больше или равных 5 и вывести большую из них")
    print("4. Заменить все элементы на 0")
    print("5. Выйти из программы")
    choice = input("Выберите действие (1, 2, 3, 4, 5): ")

    if choice == "1":
        multiplication()
    elif choice == "2":
        print(sum())
    elif choice == "3":
        print(sumIf())
    elif choice == "4":
        nullElements()
        print("Все элементы заменены на 0.")
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

print("Программа завершена.")