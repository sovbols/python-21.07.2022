import tkinter as tk
import random

window = tk.Tk()
window.geometry(newGeometry= "290x200")
window.title("Угадай число")

attempts_1 = 10
secret_number = random.randint(1,100)

def check(event):
    global attempts_1
    number = number_entry.get()
    if number == "":
        more["text"] = "Введите число от 1 до 100"
    else:
        if attempts_1 > 0:
            attempts_1 -= 1
            number = int(number)
            if number == secret_number:
                more["text"] = "Поздравляю ты угадал!"
                attempts_1 = 0
                check_button.configure(state = tk.DISABLED)
                replay.configure(state = tk.NORMAL)
            if number > secret_number:
                more["text"] = "Секретное число меньше!"
            if number < secret_number:
                more["text"] = "Секретное число больше!"
            attempts ["text"] = f"Количество попыток: {attempts_1}"
            number_entry.delete(0, "end")
        else:
            more["text"] = "Можешь повторить попытку!"
            replay.configure(state=tk.NORMAL)
            check_button.configure(state=tk.DISABLED)

def reset():
    global secret_number
    global attempts_1
    secret_number = random.randint(1, 100)
    attempts_1 = 10
    attempts["text"] = f"Количество попыток: {attempts_1}"
    more["text"] = "Введите число от 1 до 100"

more = tk.Label(window, text = "Введите число от 1 до 100", font = ("Helevetica", 12))
more.place(x = 0, y = 0)
attempts = tk.Label(window, text = f"Количество попыток: {attempts_1}", font = ("Helevetica",12))
attempts.place(x = 0, y = 30)
number_entry = tk.Entry(window, font = ("Helevetica", 12), width = 17)
number_entry.place(x = 4, y = 55)
check_button = tk.Button(window, text = "Проверить", font = ("Helevetica",14), width = 14, command = lambda e="<Return>":check(e))
check_button.place(x = 3, y = 85)
replay = tk.Button(window, text = "Играть снова", font = ("Helevetica", 14), width = 14, state = tk.DISABLED, command = reset)
replay.place(x = 3, y = 130)





window.bind("<Return>", check)
window.mainloop()