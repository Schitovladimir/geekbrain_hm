def clearing(num):
    return "".join([el for el in num if el.isdigit()]) #Оставляем в строчке только числа


def dict_sum(text_6):
    subjects = {}
    for el in text_6:
        for i in enumerate(el.split()): #Превращаем каждую строчку в список и проходим по элементам списка, одновременно применяя функцию enumerate
            if i[0] == 0: # первый элемент - это ключ, назначаем в этом условии его словарю
                key = i[1][:len(i[1])-1]
                subjects[key] = 0
            else: #очищаем числа от прочих элементов, проверяем, что это действительно число и далее складываем его в словаре
                if clearing(i[1]).isdigit():
                    subjects[key] = int(subjects[key]) + int(clearing(i[1]))
    return subjects


with open("text_6.txt", "r", encoding="utf-8") as text_6:
    print(dict_sum(text_6))



