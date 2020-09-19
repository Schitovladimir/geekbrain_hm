import math

class Cells():
    def __init__(self, number):
        self.number = number
    """Сложение"""
    def __add__(self, other):
        return Cells(self.number + other.number)
    """Вычитание"""
    def __sub__(self, other):
        if self.number >= other.number:
            return Cells(self.number - other.number)
        else:
            return "Количество ячеек в первой клетке, должно быть больше чем во второй"
    """Умножение"""
    def __mul__(self, other):
        return Cells(self.number * other.number)
    """Целочисленное деление"""
    def __floordiv__(self, other):
        return Cells(self.number // other.number)
    """Функция __str__"""
    def __str__(self):
        return f"{self.number}"
    def make_order(self, row):
        if self.number % row == 0:
            [print("*" * row) for _ in range(0,math.ceil(self.number / row))]
        else:
            [print("*" * row) for _ in range(0, int(self.number / row))]
            print("*" * (self.number % row))

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
row = int(input("Введите требуемое количество строк для вывода ячеек: "))

cell_1 = Cells(num1)
cell_2 = Cells(num2)


print("-" * 90)
print(f"Сумма клеток {num1} + {num2} равна: {Cells(num1) + Cells(num2)}.")
Cells(cell_1.number + cell_2.number).make_order(row)
print("-" * 90)
print(f"Умножение клеток {num1} * {num2} равна: {Cells(num1) * Cells(num2)}.")
Cells(cell_1.number * cell_2.number).make_order(row)
print("-" * 90)
print(f"Целочисленное деление клеток {num1} // {num2} равна: {Cells(num1) // Cells(num2)}.")
Cells(cell_1.number // cell_2.number).make_order(row)
print("-" * 90)
print(f"Вычитание клеток {num1} - {num2} равна: {Cells(num1) - Cells(num2)}.")
Cells(cell_1.number - cell_2.number).make_order(row)

