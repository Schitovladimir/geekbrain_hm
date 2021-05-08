# Lesson - 3
# Task - 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a,b):
    while True:
        try:
            return float(a/b)
        except ZeroDivisionError:
            print("You can't divide on 0, please enter another number")
            b = float(input("Enter the divisor: "))
        else:
            break
while True:
    try:
        a = float(input("Enter the divisible value: "))
        b = float(input("Enter the divisor: "))
        print(f"{a} / {b} = {division(a,b):.3f}")
        break
    except ValueError:
        print("Enter only numbers")


