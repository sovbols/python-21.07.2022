import tkinter as tk

window = tk.Tk()
window.geometry(newGeometry= "300x300")
window.title = "Крестики нолики"
window.resizable(False, False)

area = []
turn = 1
def push(button):
    global turn
    if turn %2 == 0:
        turn_char = "O"
    else:
        turn_char = "X"
    print(f"совершают ход: {turn_char}")
    if button["text"] == "":
        button["text"] = turn_char
        turn += 1


for x in range(3):
    area.append([])
    for y in range(3):
        button = tk.Button(window, text="", width = 13, height = 6)
        area[x].append(button)
        area[x][y].place(x = x * 100, y = y * 100)
        area [x][y]["command"] = lambda selected_button=button: push(selected_button)




window.mainloop()