class SmartPhone():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def sayBrand(self):
        print(f"я от бренда {self.brand}")
    def sayColor(self):
        print(f"мой цвет {self.color}")

iphone=SmartPhone("apple","чёрный")
iphone.sayColor()
iphone.sayBrand()