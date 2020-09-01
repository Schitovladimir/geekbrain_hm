"""Lesson - 2
Task -4
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове. """

"""Version 1"""
sentence = input("Enter any sentence: ")

words = sentence.split()

for ind, word  in enumerate(words):
    if len(word) <=10:
        print(f"{ind+1} word is {word}")
    else:
        print(f"{ind+1} word is {word[:10]}")


"""Version 2"""
sentence = input("Enter any sentence: ")

words = sentence.split()

for i in range(len(words)):
    if len(words[i]) <=10:
        print(f"{i+1} word is {words[i]}")
    else:
        print(f"{i+1} word is {words[i][:10]}")

