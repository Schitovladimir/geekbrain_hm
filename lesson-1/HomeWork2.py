""""Задание 2.
Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк."""

while True:

    seconds = int(input("Enter any number of seconds: "))

    if 86400 >= seconds >= 0:
        ss = seconds % 60
        mm = (seconds - ss) // 60 % 60
        hh =  ((seconds - ss) // 60 - mm) // 60
        print(f"{hh:02d}:{mm:02d}:{ss:02d}")
        break
    else:
        print("Enter number in range from 0 to 86400")


