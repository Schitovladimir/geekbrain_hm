# Lesson - 3
# Task - 2
# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def users(**kwargs):
    user = ""
    for key, value in kwargs.items():
        user = user + "; " + key.title() + ": " + value.title() if user != "" else key.title() + ": " + value.title()
    return user
print(users(first_name=input("First name: "),last_name=input("Last_name: "),birthday=input("Birthday: "),city=input("City: "),email=input("Email: "),phone=input("Number phone: ")))