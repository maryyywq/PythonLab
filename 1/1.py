a = []
print("Вводите элементы списка(для окончания ввода используется пустая строка):")
while (s := input()) != "":
    a.append(s)
print("Нечетные элементы:")
for i in a:
    if i.isdigit() and int(i) % 2 != 0:
        print(i)
