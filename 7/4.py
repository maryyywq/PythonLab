import csv

def read_students(file_name):
    with open(file_name, encoding="utf8") as csvfile:
        f_reader = list(csv.reader(csvfile, delimiter=';'))
    return {int(student[0]): {'ФИО': student[1], 'Возраст': int(student[2]), 'Группа': student[3]} for student in f_reader[1:]}

def filter_students_by_age(students_data, min_age):
    return {student_id: student_info for student_id, student_info in students_data.items() if student_info['Возраст'] > min_age}

def age_add(students_data, file_name):
    for student_id, student_info in students_data.items():
        student_info['Возраст'] -= 1
    write_students(students_data, file_name)

def write_students(students_data, file_name):
    with open(file_name, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["№", "ФИО", "Возраст", "Группа"])
        for student_id, student_info in students_data.items():
            writer.writerow([student_id, student_info['ФИО'], student_info['Возраст'], student_info['Группа']])

students_data = read_students('students.csv')

while True:
    print("Меню")
    print("1) Вывести студентов старше 22 лет")
    print("2) Уменьшить возраст всех студентов на 1")
    print("3) Выйти из программы")
    choice = input("Выберите действие: ")
    if choice == '1':
        filtered_students = filter_students_by_age(students_data, 22)
        for student_id, student_info in filtered_students.items():
            print(f"{student_id}: {student_info}")
    elif choice == '2':
        age_add(students_data, 'students.csv')
        print("Возраст всех студентов уменьшен на 1")
        for student_id, student_info in students_data.items():
            print(f"{student_id}: {student_info}")
    elif choice == '3':
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
print("Выход...")
