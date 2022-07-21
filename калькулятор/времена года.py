# weather=input("Введите номер месяца от 1 до 12 и я скажу к какому времени года этот месяц относится: ")
# weather=int(weather)
# if 1==weather or 2==weather or 12==weather:
#     print("Это зимний месяц ")
# if 3==weather or 4==weather or 5==weather:
#     print("Это весенний месяц")
# if 6==weather or 7==weather or 8==weather:
#     print("Это летний месяц")
# if 9==weather or 10==weather or 11==weather:
#     print("Это осенний месяц")
#
#
# box="toy"



# counter = 7
# while counter > 0:
#     print(counter)
#     counter=counter-1


import random
print("у вас есть 100 очков вы должны назвать любое число от 2 до 12.После чего вы кидаете кубик.")
print("Если сумма выпавших цифр меньше 7 и игрок задумал меньше 7, он выигрывает сделанную ставку и она прибавляется к его очкам.")
print("Если сумма выпавших цифр больше 7 и игрок задумал больше 7, он выигрывает сделанную ставку и она прибавляется к его очкам.")
print("Если сумма выпавших цифр совпала с числом игрока то ставка прибавляется к очкам увеличенная в четыре раза.")
print("Если ни одно из условий не сработало то игрок теряет ставку.")
point=100
while point > 0:
    playerNum=input("назовите любое число от 2 до 12 ")
    playerNum=int(playerNum)
    playerBet=input("назовите свою ставку ")
    playerBet=int(playerBet)
    cub1=random.randint(1,6)
    cub2=random.randint(1,6)
    summCub=cub2+cub1
    if summCub < 7 and playerNum < 7:
        point=point+playerBet
        print("Ты выйграл свою ставку! ваш баланс равен "+str(point)+" "+str(summCub))
    elif summCub > 7 and playerNum > 7:
        point=point+playerBet
        print("Ты выйграл свою ставку! ваш баланс равен "+str(point)+" "+str(summCub))
    elif summCub == playerNum:
        point=point+playerBet*4
        print("Ты выйграл свою ставку в четыре раза больше! ваш баланс равен "+str(point)+" "+str(summCub))
    else:
        point=point-playerBet
        print("Ты не выйграл свою ставку! ваш баланс равен "+str(point)+" "+str(summCub))