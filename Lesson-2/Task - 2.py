"""Lesson - 2
Task -2
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""


values = [] #Переменная для списка
i = 1
print("Hello, enter any type of value. You can only enter 9 number of values. \nIf you want to finish cycle, enter 'q' ")

#Ввод значений списка
while len(values) <= 9:

    value = input(f"{i} number: ")

    if value == "q".lower(): #Если ввели "q", то выход из цикла
        break
    else:
        values.append(value) #Добавление нового элемента в список
        i += 1 #Счетчик для выхода из цикла

print(f"You entered the following values: {values}")

#Цикл для обмена значениями соседних элементов
for i in range(0,len(values),2):

    if(i+1 == len(values) and i+1 % 2 != 0): #Если значение счетчика предпоследнее и длина списка нечетная, то ничего не меняем - выходим из цикла
        break

    free_num = values[i]
    values[i] = values[i+1]
    values[i+1] = free_num

print(f"You got the following {values}")