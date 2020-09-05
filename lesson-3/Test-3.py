# Lesson-3
# Task-3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# vesrion 1
def my_func(a,b,c):
    return sum([a,b,c]) - min([a,b,c])

a = int(input("Enter 1-st number: "))
b = int(input("Enter 2-nd number: "))
c = int(input("Enter 3-rd  number: "))
print(f"The sum of the two maximum numbers is {my_func(a,b,c)} (Usual function)")

# version 2
my_func = lambda a,b,c: sum([a,b,c]) - min([a,b,c])
print(f"The sum of the two maximum numbers is {my_func(a,b,c)} (Lambda)")