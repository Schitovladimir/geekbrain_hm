# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def check(sen):
    eng_alph = [chr(32)]
    for i in range(ord("a"), ord("z") + 1):
        eng_alph.append(chr(i))
    sen = set(sen)
    for letter in sen:
        if letter in eng_alph:
            continue
        else:
            print("We required to enter only latin letters with spaces, please remake it")
            return False
    return True

def int_func(word):
    word = list(word)
    word[0] = chr(ord(word[0]) - 32)
    return "".join(word)

bool_ = False
while bool_ == False:
    sentences = input('Enter sentences with latin letters here: ').lower()
    bool_ = check(sentences) #Проверка на латинские буквы
sentences = sentences.split()

for i in range(len(sentences)):
    sentences[i] = int_func(sentences[i]) #Возврат прописной буквы для каждого введенного слова
print(f'Capital letters: {" ".join(sentences)}')






