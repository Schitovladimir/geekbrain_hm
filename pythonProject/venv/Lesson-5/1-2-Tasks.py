def write_data(file_): #Записываем данные в файл
    try:
        while True:
            text = input("Enter the text you would like to record in the file, in case exit, to entry a blank line: ")
            if text == "": break
            print(text, file=file_)
    except IOError:
        print("File error")

def count_char(file): #Считаем количество символов и строк
    file.seek(0)
    for i, str_ in enumerate(file):
        print(f"{i+1} line contains {len(str_)} characters")
    file.seek(0)
    print(f"Total strings - {i+1}\nTotal characters - {len(file.read())}")

with open('1-2-Tasks.txt', 'w+', encoding='utf-8') as task_1:
    write_data(task_1)
    count_char(task_1)
