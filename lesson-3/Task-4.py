# Lesson-3
# Task-4
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def check_y(y):
    while y >= 0:
        y = int(input("Sorry, you did something another, enter a negative integer y: "))
    return y

def check_x(x):
    while x <= 0:
        x = float(input("Sorry, you did something another, enter a real positive number x: "))
    return x

def my_func(x,y):

    z = 1
    for i in range(0,abs(y)):
        z *= 1/x
    return z
while True:
    try:
        x = float(input("Enter a real positive number x: "))
        y = int(input("Enter a negative integer y: "))
        x = check_x(x)
        y = check_y(y)
    except (ValueError, NameError):
        print("You entered wrong value, please change it")
    else:
        print(f"{x}^({y}) = {my_func(x,y):.5f} - without function")
        print(f"{x}^({y}) = {x**y:.5f} - function")
        if input("If you want to get out, please enter 'q', otherwise press 'enter'").lower() == "q":
            break
