"""5)Lesson - 2
Task -5
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

print("Hello, dear user. Please enter several numbers in turn and see the result")

rates = []

while True:
    rate = input("Enter rate for the film: ")
    if rate.isdigit(): #Условия для проверки на число
        if len(rates) == 0: #Если еще не вводили числа рейтинга, то добавляем первый раз
            rates.append(int(rate))
        else: #Если вводим третье число, то запускаем проверку по остальным числам
            for i in range(len(rates)):
                rate = int(rate)
                if rates[i] >= rate:
                    if rate == rates[i]:
                        if rates.count(i) > 1:
                            rates.insert((rates.index(rate)+count(i)-1),rate)
                            break
                        else:
                            rates.insert(rates.index(rate), rate)
                            break
                    else:
                        if i == len(rates)-1:
                            rates.append(rate)
                            break
                else:
                    rates.insert(i,rate)
                    break
        rates_ = ""
        for el in rates:
            if rates_ == "":
                rates_ = str(el)
            else:
                rates_ = rates_ + ", " + str(el)

        print(f"User entered {rate}. Result is {rates_}")
    else:
        print("You have to enter only numbers...")



