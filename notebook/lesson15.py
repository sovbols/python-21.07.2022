class Car:
    def __init__(self,speed,color):
        self.speed=speed
        self.color=color
    def BEEP(self):
        print("BEEEEEEEP")
    def saySpeed(self):
        print(f"моя скорость {self.speed}")
    def sayColor(self):
        print(f"мой цвет {self.color}")
BMW=Car(120,"black")
BMW.BEEP()
BMW.saySpeed()
BMW.sayColor()
porshe=Car(240,"silver")
porshe.BEEP()
porshe.saySpeed()
porshe.sayColor()
Zhiguli=Car(80,"red")
Zhiguli.sayColor()