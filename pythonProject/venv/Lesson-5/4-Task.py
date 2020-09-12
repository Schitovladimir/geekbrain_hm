def create_list(file): #Создаем лист с русским переводом и помещаем его в новый файл
    num = []
    rus_num = {1 : "Один",2 : "Два", 3 : "Три", 4 : "Четыре", 5 : "Пять", 6 : "Шесть"}
    for el in file.readlines():
        list_ = el.split()
        for key, value in rus_num.items():
            if str(key) in list_:
                list_[0] = value
                num.append(list_)
    with open("text_4_2.txt", "w", encoding="utf-8") as numbers_2:
        [numbers_2.writelines(" ".join(el) + "\n") for el in num] #Помещаем список в новый файл

with open("text_4.txt", "r", encoding="utf-8") as file:
    num = create_list(file)

