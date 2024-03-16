import csv

def read_students(file_name):
    with open(file_name, encoding="utf8") as csvfile:
        f_reader = list(csv.reader(csvfile, delimiter=';'))
    return f_reader

def filter_students_by_age(students_data, min_age):
    return [student for student in students_data if int(student[2]) > min_age]

def age_add(students_data):
    for student in students_data[1:]:
        student[2] = str(int(student[2]) - 1)
    return students_data

students_data = read_students('students.csv')

while True:
    print("Меню")
    print("1) Вывести студентов старше 22 лет")
    print("2) Уменьшить возраст всех студентов на 1")
    print("3) Выйти из программы")
    choice = input("Выберите действие: ")
    if choice == '1':
        filtered_students = filter_students_by_age(students_data[1:], 22)
        for student in filtered_students:
            print(student)
    elif choice == '2':
        students_data = age_add(students_data)
        print("Возраст всех студентов уменьшен на 1")
        for student in students_data[1:]:
            print(student)
    elif choice == '3':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
print("Выход...")
