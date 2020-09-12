import json

def calc(num): #Функция считает прибыль
    nums = [float(el) for el in num if el.isdigit()]
    return float(nums[0] - nums[1])

def avr_(dict):# Функция для подсчета среднего значения
    avr = 0
    i = 0
    for rev in dict.values():
        rev = float(rev)
        if rev > 0:
            i += 1
            avr = (avr + rev)
    return avr / i

def json_(dict, avr): # Функция для создания JSON объекта
    with open("test_7.json", "w") as write_f:
        json.dump([dict, {"average_profit": avr}], write_f, ensure_ascii=False)
    print(json.dumps([dict, {"average_profit":avr}], ensure_ascii=False))


to_json = {}
with open("text_7.txt", "r", encoding="utf-8") as text_7:
    for el in text_7:
        el = el.split()
        revenue = calc(el)
        to_json[el[0]] = revenue
avr = avr_(to_json)
json_(to_json,avr)