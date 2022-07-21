import arcade
class OurPicture(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.PINK)
        arcade.draw_circle_filled(300,300,200,arcade.color.YELLOW)
        arcade.draw_circle_filled(220,380,50,arcade.color.BLACK)
        arcade.draw_circle_filled(380,380,50,arcade.color.BLACK)

        centerX=300
        centerY=230
        width=150
        height=80
        startAngle=0
        endAngle=360
        lineWidth=50
        arcade.draw_arc_outline(centerX,centerY,width,height,arcade.color.BLACK,startAngle,endAngle,lineWidth)

window=OurPicture(600,600,"смайлик")
arcade.run()