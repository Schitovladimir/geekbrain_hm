"""Задание 4
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

number = int(input("Enter int number: "))
b = 0

while True:

    a = number % 10
    number //= 10

    if a > b:
        b = a

    if number == 0:
        print(f"The biggest number is {b}")
        break
