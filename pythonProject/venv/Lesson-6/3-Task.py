class Worker:
    def __init__(self, name, surname, wage, bonus):
        self._name = name
        self._surname = surname
        self._income = {"wage" : wage, "bonus" : bonus}

class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)
    def get_full_name(self):
        print(f"Worker: {self._surname} {self._name}")
    def get_total_income(self):
        try:
            print(f"Income: {int(self._income['wage']) + int(self._income['bonus'])}")
        except (ValueError):
            print("Please enter only numbers")

position = Position(input("Enter the employee's name: "), input("Enter the employee's surname: "), input("Enter the employee's wage: "), input("Enter the employee's bonus: "))

position.get_full_name()
position.get_total_income()