# Task - 6
# Lesson - 4
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count
from itertools import cycle


def count_func(start_number, end_number):
    try:
        start_number = int(start_number)
        end_number = int(end_number)
        if end_number > start_number:
            n = start_number
            elements = count(start_number)
            list_chr = []
            while n <= end_number:
                list_chr.append(chr(next(elements)))
                n += 1
            print(f"{' '.join(list_chr)}")
            return list_chr
        else:
            print("Enter end number more than start number")
    except (ValueError, TypeError):
        print("You can enter only positive numbers")


def cycle_func(chars_, number):
    try:
        i = 0
        list_chars = []
        chars_ = chars_.split()
        chars_ = cycle(chars_)
        while int(number) > i:
            list_chars.append(next(chars_))
            i += 1
        print(" ".join(list_chars))
    except ValueError:
        print("You can enter only positive numbers")


chars = " ".join(count_func(input("Enter the number to START the loop with (from 65 to 90 or from 97 to 122): "), input(
    "Enter the number more than start_number where the cycle WILL END (from 65 to 90 or from 97 to 122): ")))
cycle_func(chars, input("Enter the number of repetitions for the characters: "))

# for el in count(a):
#     if el > a + 10:
#         break
#     else:
#         elements.append(el)
#         print(el)
# print(elements)
#
# for el in cycle(elements):
#     if el == 15:
#         print(el)
#         break
#     else:
#         print(el)
