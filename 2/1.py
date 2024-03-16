from random import *
my_number = randint(1, 100)
user_number = int(input("Введите число: "))
while user_number <= my_number:
    print("Ваше число меньше, чем заданное!")
    user_number = int(input("Введите число ещё раз: "))
print(f"Число my_number: {my_number}; ваше число: {user_number}")
