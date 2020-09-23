class DivZero(Exception):
    def __init__(self, text):
        self.text = text

try:
    num1 = int(input("Введите делимое: "))
    num2 = int(input("Введите делитель: "))
    if num2 == 0:
        raise DivZero("Вы ввели неправильную операцию! Деление на 0 запрещено!")
except ValueError:
    print("Вы ввели не число")
except DivZero as err:
    print(err)
else:
    print(round(num1 / num2))
