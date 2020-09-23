import tkinter
from tkinter.ttk import Combobox
from tkinter import messagebox


class Company():
    comp = {
        "Бухгалтерия": { "Принтер": 0, "Сканер": 0, "Ксерокс": 0},
        "Логистика": {"Принтер": 0, "Сканер": 0, "Ксерокс": 0},
        "Склад": {"Принтер": 0, "Сканер": 0, "Ксерокс": 0},
    }
    num = 0

class Accounting(Company):
    pass

class Logistics(Company):
    pass

class OfficeEq(Company):

    @classmethod
    def add_eq(cls, division, quantity, title):
        if cls.check_num(quantity):
            quantity = int(quantity)
            if division == "Бухгалтерия":
                remains = cls.comp["Склад"][title] - quantity
                if cls.check_sum(remains):
                    cls.comp["Склад"][title] = remains
                    cls.comp["Бухгалтерия"][title] = cls.comp["Бухгалтерия"][title] + quantity
            elif division == "Логистика":
                remains = cls.comp["Склад"][title] - quantity
                if cls.check_sum(remains):
                    cls.comp["Склад"][title] = remains
                    cls.comp["Логистика"][title] = cls.comp["Логистика"][title] + quantity
            elif division == "Склад":
                cls.comp["Склад"][title] = cls.comp["Склад"][title] + quantity

    @staticmethod
    def check_sum(num):
        if num >= 0:
            return True
        else:
            messagebox.showinfo('Ошибка', 'Вы не можете вывести со склада больше, чем там есть')

    @staticmethod
    def check_num(num):
        try:
            if int(num) > 0:
                return True
            else:
                False
        except ValueError:
            messagebox.showinfo("Ошибка ввода", "Введеное значение не может быть строковым и меньше или равным нулю или отсутствовать")

class Printer(OfficeEq):
    pass

class Scanner(OfficeEq):
    pass

class Xerox(OfficeEq):
    pass

#Функция для бередачи данных в классы
def clicked():
    division = combo_1.get()
    equipement = combo_2.get()
    quantity = txt.get()
    Printer.add_eq(division, quantity, equipement)
    messagebox.showinfo("Изменения", f"Бухгалтерия: \n сканеры - {OfficeEq.comp['Бухгалтерия']['Сканер']}, \
    принтеры - {OfficeEq.comp['Бухгалтерия']['Принтер']}, ксероксы - {OfficeEq.comp['Бухгалтерия']['Ксерокс']} \n \
    Логистика: \n сканеры - {OfficeEq.comp['Логистика']['Сканер']}, принтеры - {OfficeEq.comp['Логистика']['Принтер']}, \
    ксероксы - {OfficeEq.comp['Логистика']['Ксерокс']} \n Склад: \n сканеры - {OfficeEq.comp['Склад']['Сканер']}, \
    принтеры - {OfficeEq.comp['Склад']['Принтер']}, ксероксы - {OfficeEq.comp['Склад']['Ксерокс']}")

divisions = ("Бухгалтерия","Логистика","Склад")
equipements = ("Принтер","Сканер","Ксерокс")
#Создание окна с вводом данных
window = tkinter.Tk()
window.title("Добро пожаловать в автоматизированную систему")
window.geometry('500x250')
#Первый бокс с возможностью выбора подразделения
combo_1 = Combobox(window, state="readonly")
combo_1['values'] = divisions
combo_1.current(2)
combo_1.grid(column=1, row =0)
lbl_2 = tkinter.Label(window)
lbl_2 = tkinter.Label(window, text="Выберите подразделение: ")
lbl_2.grid(column=0, row=0)
#Второй бокс с возможностью выбора оборудования
combo_2 = Combobox(window, state="readonly")
combo_2['values'] = equipements
combo_2.current(2)
combo_2.grid(column=1, row =1)
lbl_3 = tkinter.Label(window)
lbl_3 = tkinter.Label(window, text="Выберите оборудование: ")
lbl_3.grid(column=0, row=1)
#Ввод некоторого количества оборудования
txt = tkinter.Entry(window)
txt.grid(column=1, row=2)
txt.focus()
lbl_1 = tkinter.Label(window)
lbl_1 = tkinter.Label(window, text="Напишите количество оборудования: ")
lbl_1.grid(column=0, row=2)

btn_1 = tkinter.Button(window, text="Передать оборудование", command = clicked)
btn_1.grid(column=0, row=3)

btn_2 = tkinter.Button(window, text="Закрыть", command = window.destroy)
btn_2.grid(column=0, row=5)

window.mainloop()
