class Transport:
    def __init__(self,speed,color,owner):
        super().__init__(speed,color,owner)

    def BEEP(self):
        print("BEEEEEEEP")
    def saySpeed(self):
        print(f"скорость машины {self.speed}")
    def sayColor(self):
        print(f"цвет машины {self.color}")
    def sayOwner(self):
        print(f"эта машина принадлежит {self.owner}")

gelentvagen=Transport(170,"чёрный","Влада")
gelentvagen.sayColor()
