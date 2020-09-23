class Numbers(Exception):
    def __init__(self, txt):
        self.txt = txt

all = []
count = 0
bool = False

while bool is not True:
    try:
        numbers = input("Enter numbers: ")
        for el in numbers.split():
            if el.isdigit():
                all.append(el)
            elif el.lower() == "stop":
                bool = True
                break
            else:
                count += 1
        if count >= 1:
            raise Numbers(f"Entered {count} words.")
    except Numbers as err:
        print(err)
    finally:
        print(all)
