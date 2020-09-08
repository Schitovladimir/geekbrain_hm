# Lesson - 4
# Task - 7
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(a):
    try:
        a = int(a)
        if a >= 1:
            for _ in range(1, a + 1):
                yield _
        else:
            print("Enter a positive integer")
    except ValueError:
        print("Enter a positive integer")


i = 1
count_ = 0
str_ = ""
while count_ == 0:
    for el in fact(input("Enter number for factorial: ")):
        i *= el
        count_ += i
        str_ = str_ + " * " + str(el)

print(f"{str_[3:len(str_)]} = {i}")
