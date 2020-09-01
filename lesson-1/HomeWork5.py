"""Задание 5
1) Запросите у пользователя значения выручки и издержек фирмы.
2) Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
3) Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
4) Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

revenue = int(input("Enter revenue for your company: "))
cost = int(input("Enter cost for your company: "))

x = revenue - cost

if x > 0:
    profit = x
    print(f"Congratulate, profit of your company is {profit}")
    return_on_revenue = float(profit) / float(revenue)
    print(f"Return on revenue is {return_on_revenue}")
    num_emp = int(input("Enter number employees of your company: "))
    print(f"The company's profit per employee is {int(profit/num_emp)}")
else:
    cost = x
    print(f"Work harder, because profit of your company is {cost}")
