lst = [[1, "Иванов Иван Иванович", 23, "БО-111111"], [2, "Сидоров Семен Семенович", 23, "БО-111111"], [3, "Яшков Илья Петрович", 24, "БО-222222"]]

res = {x[0]: x[1:] for x in lst}
print(res)