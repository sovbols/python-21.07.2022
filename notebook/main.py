import tkinter as tk
import random
import time
stop=False
colors=["red","purple","black","orange","green","blue","brown","gray","pink"]
window=tk.Tk()
window.geometry("650x500")
window.title("Цветные фигуры")

canvas=tk.Canvas(window,bg="white",width=500,height=500)
canvas.place(x=0,y=0)
def stopDraw():
    global stop
    stop=True
def drawCircle():
    color=random.choice(colors)
    x=random.randint(0,500)
    y=random.randint(0,500)
    canvas.create_oval(x,y,x+20,y+20,fill=color,)
def drawOval():
    color=random.choice(colors)
    x=random.randint(0,500)
    y=random.randint(0,500)
    d1=random.randint(0,100)
    d2=random.randint(0,100)
    canvas.create_oval(x,y,x+d1,y+d2,fill=color)
def drawRectangle():
    color=random.choice(colors)
    x=random.randint(0,500)
    y=random.randint(0,500)
    canvas.create_rectangle(x,y,x+20,y+20,fill=color)
def drawCircles():
    global stop
    while True:
        drawCircle()
        window.update()
        time.sleep(1)
        if stop:
            stop=False
            break

def animateCircles():
    color=random.choice(colors)
    d=random.randint(1,100)
    x=random.randint(0,500-d)
    y=random.randint(0,500-d)
    circle=canvas.create_oval(x,y,x+d,y+d,fill=color)
    dx=2
    dy=2
    while True:
        coords=canvas.coords(circle)
        print(coords)
        left=coords[0]
        top=coords[1]
        right=coords[2]
        bottom=coords[3]
        if left <= 0 or right >=500:
            dx = -dx
        if top <= 0 or bottom >=500:
            dy = -dy


        canvas.move(circle,dx,dy)
        time.sleep(0.01)
        window.update()




button_circle=tk.Button(window,width=17,text="Нарисовать круг",command=drawCircle)
button_circle.place(x=510,y=20)
button_oval=tk.Button(window,width=17,text="Нарисовать овал",command=drawOval)
button_oval.place(x=510,y=100)
button_rectangle=tk.Button(window,width=17,text="Нарисовать квадрат",command=drawRectangle)
button_rectangle.place(x=510,y=180)
button_infinityCircle=tk.Button(window,width=17,text="Бесконечные круги",command=drawCircles)
button_infinityCircle.place(x=510,y=260)
button_animationCircle=tk.Button(window,width=17,text="Анимировать круг",command=animateCircles)
button_animationCircle.place(x=510,y=340)
stop_button=tk.Button(window,width=17,text="Стоп",command=stopDraw)
stop_button.place(x=510,y=420)
window.mainloop()