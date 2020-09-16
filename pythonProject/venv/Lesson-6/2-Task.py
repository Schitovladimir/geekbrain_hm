class Road():
    def __init__(self, length, width):
            self._lenght = length
            self._width = width
            self.thickness = 5
            self.weight = 25
    def calculate(self):
        try:
            print(f"To cover the entire roadway, you need {round(int(self._lenght) * int(self._width) * self.thickness * self.weight * 0.001)} tons of asphalt")
        except (ValueError):
            print("Please enter only numbers")

road = Road(input("Enter the length of the asphalt: "), input("Enter the width of the asphalt: "))
road.calculate()