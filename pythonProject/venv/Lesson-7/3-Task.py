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
        [print("*" * (self.number // row)) for _ in range(0,row)]

cell_1 = Cells(8)
cell_2 = Cells(4)

print(f"Сумма клеток: {Cells(8) + Cells(4)}.")
Cells(cell_1.number + cell_2.number).make_order(2)
print(f"Умножение клеток: {Cells(8) * Cells(4)}.")
Cells(cell_1.number * cell_2.number).make_order(2)
print(f"Целочисленное деление клеток: {Cells(8) // Cells(4)}.")
Cells(cell_1.number // cell_2.number).make_order(2)
print(f"Вычитание клеток: {Cells(8) - Cells(4)}.")
Cells(cell_1.number - cell_2.number).make_order(2)

