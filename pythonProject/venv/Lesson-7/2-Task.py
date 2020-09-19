from abc import abstractmethod

class Clothes():
    def __init__(self, title, param):
        self.param = param  # Параметр одежды
        self.title = title

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):
    def __init__(self, title, param):
        super().__init__(title, param)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 16:
            self.__param1 = 16
        elif param > 116:
            self.__param = 116
        else:
            self.__param = param

    def calculate(self):
        print(f"The total fabric consumption for the {self.title} coat is {round(self.param / 6.5 + 5, 2)}")

class Suit(Clothes):
    def __init__(self, title, param):
        super().__init__(title, param)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 140:
            self.__param = 140
        elif param > 220:
            self.__param = 220
        else:
            self.__param = param

    def calculate(self):
        print(f"The total fabric consumption for the {self.title} suit is {round(self.param * 2 + 0.3, 2)}")

coat = Coat("H&M", 65)
coat.calculate()

suit = Suit("Zara", 150)
suit.calculate()


