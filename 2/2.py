a = []
print("Вводите элементы списка(для окончания ввода используется пустая строка):")
while (s := input()) != "":
    a.append(s)
print("Строки, начинающиеся с r:")
for i in a:
    if i.startswith("r"):
        print(i)
