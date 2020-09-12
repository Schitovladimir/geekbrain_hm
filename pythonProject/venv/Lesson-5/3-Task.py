def salary(task_3):
    [print(f"{el.split()[0]} получает зарплату {el.split()[1]} рублей") for el in task_3.readlines() if
     float(el.split()[1]) < 20000]


with open("text_3.txt", "r", encoding="utf-8") as task_3:
    salary(task_3)

