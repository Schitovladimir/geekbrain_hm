""""Задание 1.
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран."""


user_name = input("Enter your user name: ")

password_db = "1234321" #Пароль для БД
password_app = "0987654ABC" #Пароль для приложения

input_password_db = input(f"{user_name}, enter password for Data Base: ")
if input_password_db == password_db:
    print(f"{user_name}, congratulate, you entered successfully the password for DB")
else:
    print(f"{user_name}, sorry, you entered wrong password")

input_password_app = input(f"{user_name}, enter password for application: ")
if input_password_app == password_app:
    print(f"{user_name}, congratulate, you entered successfully the password for application")
else:
    print(f"{user_name}, sorry, you entered wrong password")

