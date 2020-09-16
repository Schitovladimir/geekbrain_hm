from termcolor import colored

class Car():
    def __init__(self, speed, name, color, is_police):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police
    def go(self):
        print(f"{self.color} car {self.name} went")
    def stop(self):
        print(f"{self.color} car {self.name} stopped")
    def turn_right(self):
        print(f"{self.color} car {self.name} turned to the right")
    def turn_left(self):
        print(f"{self.color} car {self.name} turned to the left")
    def show_speed(self):
        print(f"Speed of the car is {self.speed}")

class TownCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)
    def show_speed(self):
        if int(self.speed) > 60:
            print(f"{colored(self.speed,'red')} bigger than 60")
        else:
            print(f"Speed of the car is normal {colored(self.speed, 'green')}")

class SportCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)

class WorkCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)
    def show_speed(self):
        if int(self.speed) > 40:
            print(f"{colored(self.speed,'red')} bigger than 40")
        else:
            print(f"Speed of the car is normally {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, name, color, is_police):
        super().__init__(speed, name, color, is_police)

print(f"{60 * '-'}")
towncar = TownCar("50","Mazda","White",False)
towncar.go()
towncar.stop()
towncar.turn_right()
towncar.turn_left()
towncar.show_speed()
print(f"{60 * '-'}")
sportcar = SportCar("200","Lambordgini","Orange",False)
sportcar.go()
sportcar.stop()
sportcar.turn_right()
sportcar.turn_left()
sportcar.show_speed()
print(f"{60 * '-'}")
workcar = WorkCar("50","Lada","Grey",False)
workcar.go()
workcar.stop()
workcar.turn_right()
workcar.turn_left()
workcar.show_speed()
print(f"{60 * '-'}")
policecar = PoliceCar("200","Ford","Blue",True)
policecar.go()
policecar.stop()
policecar.turn_right()
policecar.turn_left()
policecar.show_speed()
print(f"{60 * '-'}")