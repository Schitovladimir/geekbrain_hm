# import turtle
from termcolor import colored
from time import sleep

class TrafficLight():
    def __init__(self):
        self.__colors = ["red", "yellow", "green"]
        self.time_ = {"red" : 7, "yellow" : 2, "green" : 1}
    def running(self):
        try:
            i , k = 0 , 1
            while True:
                print(f"{colored(self.__colors[i],self.__colors[i])}")
                sleep(self.time_[self.__colors[i]])
                i += k
                k = k * (-1) if i % 2 == 0 else k
        except IndexError:
            self.__colors.reverse()

trafficlight = TrafficLight()
trafficlight.running()
