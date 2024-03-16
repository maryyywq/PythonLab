from random import *

n = randint(3, 6)
matrix = [[randint(-9, 9) for i in range(n)] for i in range(n)]
print("Исходная матрица:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
print(f"Сумма всех элементов матрицы: {sum([sum(x) for x in matrix])}")
