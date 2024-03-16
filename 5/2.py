import csv

# Считываем информацию из файла
with open('students.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    students = [row for row in reader if int(row['Возраст']) > 22]

# Выводим информацию о студентах
for student in students:
    print(f"{student['№']}. {student['ФИО']}, {student['Возраст']} лет, {student['Группа']}")
