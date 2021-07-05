"""Задание 3.
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

while True:

    n = int(input("Enter any number from 1 to 9: "))

    if 9 >= n >= 1:
        nn = (n * 10) + n
        nnn = (nn * 10) + n
        print(f"result: {nnn+nn+n}")
        break
    else:
        print(f"{n} is not in range from 1 to 9")