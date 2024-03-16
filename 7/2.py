import csv

# Создаем словарь для хранения информации о студентах
students_info = {}

# Открываем файл students.csv на чтение
with open('students.csv', mode='r', encoding='utf-8') as file:
    # Создаем объект csv.reader для чтения файла
    reader = csv.reader(file, delimiter=';')
    # Пропускаем заголовок файла
    next(reader)
    # Читаем строки файла и добавляем информацию в словарь
    for row in reader:
        student_number, full_name, age, group = row
        students_info[int(student_number)] = [full_name, int(age), group]

# Выводим информацию о студентах старше 22 лет
for student_number, student_info in students_info.items():
    if student_info[1] > 22:
        print(f"Студент №{student_number}: {student_info[0]}, Возраст: {student_info[1]}, Группа: {student_info[2]}")
