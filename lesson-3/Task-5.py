# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_n(numbers):
    sum = 0
    numbers = numbers.split()
    for number in numbers:
        if number.isdigit():
            sum = sum + float(number)
        else:
            if number.lower() == "q":
                break
    return sum, number

sum = 0
while True:
    numbers = input("Enter the numbers in order: ")
    sum_, quit = sum_n(numbers)
    sum = sum_ + sum
    print(sum)
    if quit == "q":
        break