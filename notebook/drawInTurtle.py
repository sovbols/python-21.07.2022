import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(100)

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)


def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()


def pentagon():
    for i in range(5):
        t.forward(50)
        t.left(72)

def polygon(sides):
    for i in range(sides):
        t.forward(10)
        t.left(360/sides)

def spyral():
    for i in range(100):
        t.forward(i)
        t.left(40)

def star():
    for i in range(5):
       t.forward(50)
       t.left(144)

def olympyc_sircle(x,y,color):
    t.color(color)
    t.width(10)
    move(x,y)
    t.circle(50)

def olympyc_sircles():
    olympyc_sircle(-120,60,"blue")
    olympyc_sircle(-5,60,"black")
    olympyc_sircle(110,60,"red")
    olympyc_sircle(-58,10,"yellow")
    olympyc_sircle(58,10,"green")

def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(-90)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def right_down():
    t.setheading(-45)
    t.forward(10)

def red():
    t.color("red")

def blue():
    t.color("blue")

t.screen.onkeypress(blue,"2")
t.screen.onkeypress(red,"1")
t.screen.onkeypress(right_down,"y")
t.screen.onkeypress(right,"Right")
t.screen.onkeypress(left,"Left")
t.screen.onkeypress(down,"Down")
t.screen.onkeypress(up,"Up")
t.screen.listen()
t.screen.mainloop()
