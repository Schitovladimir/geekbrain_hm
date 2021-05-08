"""Lesson - 2
Task -3
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. """

season_dict = {11 : "Winter", 0 : "Winter", 1 : "Winter",
        2 : "Spring", 3 : "Spring", 4 : "Spring",
        5 : "Summer", 6 : "Summer", 7 : "Summer",
        8 : "Autumn", 9 : "Autumn", 10 : "Autumn"}

season_list = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
               "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter"]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print("If you want to get out, enter 'q', otherwise ")

while True:
    number_of_month = input("enter number of month from 1 to 12: ")
    if number_of_month.isdigit():
        number_of_month = int(number_of_month)
        if number_of_month < 0 or number_of_month >= 12:
            print("This month is not existed")
        elif 12 >= number_of_month > 0:
            number_of_month -= 1
            print(f"{months[number_of_month]} is {season_dict[number_of_month]} season (via dict)  \n{months[number_of_month]} is {season_list[number_of_month]} season (via list)")
    elif number_of_month.lower() == 'q':
        break
    else:
        print("Something weird")
