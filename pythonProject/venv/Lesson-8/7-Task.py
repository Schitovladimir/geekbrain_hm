class Complex():
    def __init__(self, num):
        self.num = str(num)

    def __mul__(self, other):
        j_1 = int(''.join([el for el in self.num.split() if "j" in el])[:-1] if len(''.join([el for el in self.num.split() if "j" in el])) != 1 else 1)
        a = int(''.join([el for el in self.num.split() if el.isdigit()]))
        j_2 = int(''.join([el for el in other.num.split() if "j" in el])[:-1] if len(''.join([el for el in other.num.split() if "j" in el])) != 1 else 1)
        b = int(''.join([el for el in other.num.split() if el.isdigit()]))
        result_num =  (a * b) - (j_1 * j_2)
        result_j = (j_1 * a) + (j_2 * b)
        return f"({self.num}) * ({other.num}) = {result_j}j + {result_num}"

    def __add__(self, other):
        j_1 = int(''.join([el for el in self.num.split() if "j" in el])[:-1] if len(''.join([el for el in self.num.split() if "j" in el])) != 1 else 1)
        a = int(''.join([el for el in self.num.split() if el.isdigit()]))
        j_2 = int(''.join([el for el in other.num.split() if "j" in el])[:-1] if len(''.join([el for el in other.num.split() if "j" in el])) != 1 else 1)
        b = int(''.join([el for el in other.num.split() if el.isdigit()]))
        result_num = a + b
        result_j = j_1 + j_2
        return f"({self.num}) + ({other.num}) = {result_j}j + {result_num}"

    def __str__(self):
        return f"{self.num}"



print(Complex("5 + 5j") * Complex("5 + 6j"))
print(Complex("9 + 1j") + Complex("32 + j"))

