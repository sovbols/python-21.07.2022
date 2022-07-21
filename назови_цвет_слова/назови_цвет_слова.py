import tkinter as tk
import tkinter.messagebox as tmb
import random

colors = ["red", "green", "brown", "gray", "yellow", "purple", "blue", "black", "pink", "orange"]

score = 0
fails = 0
time = 20

window = tk.Tk()
window.geometry(newGeometry = "360x250")
window.title("Назови цвет слова")

def newWord():
    words["fg"] = random.choice(colors)
    words["text"] = random.choice(colors)

def check(event):
    global score, fails, time, insructions
    if time > 0:
        user_color = entry.get()
        word_color = words["fg"]
        if user_color == word_color:
            print("да")
            score += 1
            right["text"] = f"Правильно: {score}"
        else:
            print("нет")
            fails += 1
            fails_1["text"] = f"Неправильно: {fails}"
        newWord()
        entry.delete(0,"end")
    else:
        if score > fails:
            tmb.showinfo("КОНЕЦ ИГРЫ", "Время вышло, но у тебя отличный результат.")
        else:
            tmb.showinfo("КОНЕЦ ИГРЫ", "Время вышло, у тебя не лучший результат попробуй ещё.")

def timer():
    global time
    if time > 0:
        time -= 1
        time_1["text"] = f"Осталось времени: {time}"
        time_1.after(1000, timer)
    else:
        if score > fails:
            tmb.showinfo("КОНЕЦ ИГРЫ", "Время вышло, но у тебя отличный результат.")
        else:
            tmb.showinfo("КОНЕЦ ИГРЫ", "Время вышло, у тебя не лучший результат попробуй ещё.")
        insructions = tk.Label(window, text="Введите цвет слова! Жми 'Spaace' чтобы начать игру заново.", font=("Helvetica", 11))

def reset(event):
    global time
    time = 21



insructions = tk.Label(window, text = "Введите цвет слова!", font = ("Helvetica", 11))
insructions.place(x = 0, y = 0)

right = tk.Label(window, text = f"Правильно: {score}", font = ("Helvetica", 11))
right.place(x = 0, y = 30)

fails_1 = tk.Label(window, text = f"Неправильно: {fails}", font = ("Helvetica", 11))
fails_1.place(x = 0, y = 50)

words = tk.Label(window, text = "color", font = ("Helvetica", 50))
words.place(x = 0, y = 70)

entry = tk.Entry(window, font = ("Helevetica", 13))
entry.place(x = 5, y = 150)

time_1 = tk.Label(window, text = f"Осталось времени: {time}", font = ("Helevetica", 11))
time_1.place(x = 0, y = 175)






newWord()
timer()
window.bind("<space>", reset)
window.bind("<Return>", check)
window.mainloop()

