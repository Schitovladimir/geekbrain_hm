class Date():
    @classmethod
    def is_digit(cls, date):
        try:
            Date.check_date([int(el) for el in date.split('-')])
        except ValueError as val:
            print(val)
        except TypeError as typ:
            print(typ)
    @staticmethod
    def check_date(date):
        day = date[0]
        month = date[1]
        year = date[2]
        days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if year >= 1900 and year <= 2020:
            if month > 0 and month <= 12:
                if month == 2:
                    if year % 4 == 0:
                        if 0 < day <= 29:
                            print(f"{day}:{month}:{year}")
                        else:
                            print(f"{day} - такого дня в {month} месяце не существуют")
                    else:
                        if 0 < day <= days_in_month[month]:
                            print(f"{day}:{month}:{year}")
                        else:
                            print(f"{day} - такого дня в {month} месяце не существуют")
                else:
                    if 0 < day <= days_in_month[month]:
                        print(f"{day}:{month}:{year}")
                    else:
                        print(f"{day} - такого дня в {month} месяце не существуют")
            else:
                print(f"{month} месяца не существуют")
        else:
            print(f"{year} - вы ввели некорректный год")

Date.is_digit(input("Введите дату в формате dd-mm-yyyy: "))