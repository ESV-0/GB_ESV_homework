# Домашнеее задание, урок-9, задание-1
from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def run(self):
        for key, timer in self.__color.items():
            print(key)
            sleep(timer)
t = TrafficLight({'Красный': 7, 'Желтый': 2, 'Зеленый': 7})

for i in range(10):    # в качестве примера задал 10 блоков включения, можно сделать бесконечный цикл.
    t.run()
