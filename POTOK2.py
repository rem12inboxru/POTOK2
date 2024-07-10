import threading
import time
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали')
        dn = 0
        wr = 100
        while wr >= self.power:
            wr -= self.power
            dn +=1
            print(f'{self.name} сражается {dn} дней, осталось {wr} врагов')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {dn} дней')


first_knight = Knight('Добрыня', 10)
second_knight = Knight('Илья', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
