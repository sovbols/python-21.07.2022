def checkWinner():
    if area[0][0]=="X" and area[0][1]=="X" and area[0][2]=="X":
        return "X"
    if area[1][0]=="X" and area[1][1]=="X" and area[1][2]=="X":
        return "X"
    if area[2][0]=="X" and area[2][1]=="X" and area[2][2]=="X":
        return "X"
    if area[0][0]=="X" and area[1][0]=="X" and area[2][0]=="X":
        return "X"
    if area[0][1]=="X" and area[1][1]=="X" and area[2][1]=="X":
        return "X"
    if area[0][2]=="X" and area[1][2]=="X" and area[2][2]=="X":
        return "X"
    if area[0][0]=="X" and area[1][1]=="X" and area[2][2]=="X":
        return "X"
    if area[0][2]=="X" and area[1][1]=="X" and area[2][0]=="X":
        return "X"

    if area[0][0]=="О" and area[0][1]=="О" and area[0][2]=="О":
        return "О"
    if area[1][0]=="О" and area[1][1]=="О" and area[1][2]=="О":
        return "О"
    if area[2][0]=="О" and area[2][1]=="О" and area[2][2]=="О":
        return "О"
    if area[0][0]=="О" and area[1][0]=="О" and area[2][0]=="О":
        return "О"
    if area[0][1]=="О" and area[1][1]=="О" and area[2][1]=="О":
        return "О"
    if area[0][2]=="О" and area[1][2]=="О" and area[2][2]=="О":
        return "О"
    if area[0][0]=="О" and area[1][1]=="О" and area[2][2]=="О":
        return "О"
    if area[0][2]=="О" and area[1][1]=="О" and area[2][0]=="О":
        return "О"
    return "*"


area = [["*","*","*"],["*","*","*"],["*","*","*"]]
for turn in range(1,10):
    print(f"Ход:{turn}")
    if turn %2 == 0:
        turnChar = "О"
        print("Ходят нолики")
    else:
        turnChar = "X"
        print("Ходят крестики")

    rou = input("введите номер строки 0, 1 или 2 ")
    column = input("введите номер столбца 0, 1 или 2 ")
    rou = int(rou)
    column = int(column)
    if area[rou][column]=="*":
        area[rou][column]=turnChar
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        if turn==9:
            print("Ничья!!!")
    for cell in area:
        print(cell)
    if checkWinner()== "X":
        print("Победа крестиков!!!")
        break
    if checkWinner()=="О":
        print("Победа ноликов!!!")
        break
    if checkWinner()=="*" and turn==9:
        print("Ничья!!!")
        break
