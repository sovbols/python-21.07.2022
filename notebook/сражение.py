class Enemy():
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
    def be_attack(self,attack):
        self.health = self.health-attack


batman = Enemy(200, 10)
joker = Enemy(200, 10)
#batman.be_attack(10)
#print(batman.health)


hits=0
#while True:
#    batman.be_attack(joker.attack)
#    joker.be_attack(batman.attack)
#    hits+=1
#    print(f"удар номер {hits} у бетмена осталось {batman.health} у джокера осталось {joker.health}")

while True:
    if batman.health<=0 and joker.health<=0:
        print("draw")
        break
    elif batman.health<=0:
        print("joker win")
        break
    elif joker.health<=0:
        print("batman win")
        break
    batman.be_attack(joker.attack)
    joker.be_attack(batman.attack)
    hits+=1

