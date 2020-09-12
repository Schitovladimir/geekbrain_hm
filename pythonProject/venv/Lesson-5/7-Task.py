# import json
#
# def calc(num): #Функция считает прибыль
#     nums = [float(el) for el in num if el.isdigit()]
#     return float(nums[0] - nums[1])
#
# def avr_(dict):# Функция для подсчета среднего значения
#     avr = 0
#     i = 0
#     for rev in dict.values():
#         rev = float(rev)
#         if rev > 0:
#             i += 1
#             avr = (avr + rev)
#     return avr / i
#
# def json_(dict, avr): # Функция для создания JSON объекта
#     with open("test_7.json", "w") as write_f:
#         json.dump([dict, {"average_profit": avr}], write_f, ensure_ascii=False)
#     print(json.dumps([dict, {"average_profit":avr}], ensure_ascii=False))
#
#
# to_json = {}
# with open("text_7.txt", "r", encoding="utf-8") as text_7:
#     for el in text_7:
#         el = el.split()
#         revenue = calc(el)
#         to_json[el[0]] = revenue
# avr = avr_(to_json)
# json_(to_json,avr)

#--------------Version2-------------------
import json

def join_dict(list_1, list_2):
    max_len = max(len(list_1),len(list_2))
    for i in range(max_len):
        yield list_1[i], list_2[i]

def json_(dict): # Функция для создания JSON объекта
    with open("test_7.json", "w") as write_f:
        json.dump(dict, write_f, ensure_ascii=False)
    print(json.dumps(dict, ensure_ascii=False))


with open("text_7.txt","r",encoding="utf-8") as file:
    companies = []
    revenue = []
    for el in file:
        companies.append(el.split()[0])
        revenue.append(float(el.split()[2])-float(el.split()[3]))
dict = [{el1: el2 for el1, el2 in join_dict(companies, revenue)}, {"average_profit": sum([el for el in revenue if el > 0])/len([el for el in revenue if el > 0])}]
json_(dict)

