def sum_num(num):
    try:
        with open("Task-5.txt", "a", encoding="utf-8") as task_5:
            print(f"{'+'.join(list(num.split()))} = {sum(list(map(int, num.split())))}", file = task_5)
    except (ValueError, NameError, IOError, TypeError) as er:
        print(er)

sum_num(input("Enter numbers separated by spaces: "))

