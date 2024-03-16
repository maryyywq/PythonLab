from os import *
s = input("Введите путь: ")
files = listdir(path=s)
print(f"В папке {len(files)} файлов")
