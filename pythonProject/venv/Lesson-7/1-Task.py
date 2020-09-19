import random

def matrix_generator(rows, columns):
    main_list = []
    for i in range(rows):
        main_list.append([random.randint(1, 20) for i in range(columns)])
    return main_list

class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.result = []

    def __add__(self, other):
        self.matrix, other.matrix = self.check_rows_cols(self.matrix, other.matrix) #Заполнение строк и столбцов 0
        for sublist in zip(self.matrix, other.matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            self.result.append(temp)
        res = ''
        for row in range(len(self.result)):
            for el in range(len(self.result[row])):
                res = res + " " + str(self.result[row][el])
            res = res + "\n"
        self.result = res
        return self.result

    def __str__(self):
        return f"{self.result}"

    def add_col(self, a, b): #добавление столбцов
        num = len(b[0])
        for row in range(0, len(b)):
            for col in range(num, len(a[0])):
                b[row].append(0)
        return a, b

    def check_col(self, a, b): #проверка столбцов
        if len(a[0]) > len(b[0]):
            return self.add_col(a, b)
        elif len(a[0]) < len(b[0]):
            return self.add_col(b, a)
        else:
            return a, b

    def check_rows_cols(self, a, b): #проверка строк
        if len(a) > len(b):
            return self.add_rows(a, b)
        elif len(a) < len(b):
            return self.add_rows(b, a)
        else:
            return self.check_col(a, b)

    def add_rows(self, a, b): #добавление строк
        for row in range(1, len(a) - len(b) + 1):
            b.append([])
            for el in range(1, len(b[0]) + 1):
                b[len(b) - 1].append(0)
        return self.check_col(a, b)


matrix1 = matrix_generator(4, 3)
matrix2 = matrix_generator(3, 5)

print(f"1st matrix - {matrix1}")
print(f"2nd matrix - {matrix2}")
print(Matrix(matrix1) + Matrix(matrix2))


