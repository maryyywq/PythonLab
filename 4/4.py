my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
          ['БОВ-421102', ['Иванов Иван', 'Петров Петр']],
          ['БО-331103', ['Сидорова Ольга', 'Попова Анна']]]

student_counter = 1

for group_info in my_len:
    group_name = group_info[0]
    students = group_info[1]
    for student in students:
        if student_counter % 2 == 0:
            print(f'{student_counter}. {group_name}: {student}')
        student_counter += 1
