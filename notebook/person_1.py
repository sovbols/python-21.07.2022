class Man():
    def __init__(self,name,age,wayf):
        self.name=name
        self.age=age
        self.wayf=wayf
    def sayName(self):
        print(f"my name is {self.name}")
    def sayAge(self):
        print(f"my age {self.age}")
    def sayWayf(self):
        print(f"I am from {self.wayf}")
nikita=Man("Nikita",13,"Russia")
nikita.sayName()
nikita.sayWayf()
nikita.sayAge()

viktoria=Man("Viktoria",20,"Itali")
viktoria.sayName()
viktoria.sayWayf()
viktoria.sayAge()