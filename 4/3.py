my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
          ['БОВ-421102', ['Иванов Иван', 'Петров Петр']],
          ['БО-331103', ['Сидорова Ольга', 'Попова Анна']]]

for group_info in my_len:
    group_name = group_info[0]
    if group_name.startswith('БО'):
        students = ', '.join(group_info[1])
        print(f'{group_name}: {students}')
