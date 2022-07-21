import arcade
class Landscape(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)


    def bird(self,x,y):
        arcade.draw_arc_outline(x,y,20,20,arcade.color.BLACK,0,90)
        arcade.draw_arc_outline(x+20,y,20,20,arcade.color.BLACK,90,180)


    def tree(self,x,y):
        arcade.draw_rectangle_filled(x,y,20,90,arcade.color.BROWN)
        arcade.draw_circle_filled(x,y+30,40,arcade.color.ARMY_GREEN)


    def hause(self,x,y):
        arcade.draw_rectangle_filled(x,y,80,80,arcade.color.LAVA)
        arcade.draw_rectangle_filled(x,y,20,20,arcade.color.BLUEBERRY)
        arcade.draw_triangle_filled(x1=x,y1=y+80,x2=x-50,y2=y+40,x3=x+50,y3=y+40,color=arcade.color.RED_BROWN)


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.BABY_BLUE)
        arcade.draw_rectangle_filled(300,100,600,200,arcade.color.GREEN)
        arcade.draw_circle_filled(90,310,60,arcade.color.YELLOW)
        self.bird(300,300)
        self.bird(400,350)
        self.tree(100,100)
        self.tree(180,110)
        self.hause(300,100)
landscape=Landscape(600,400,"пейзаж")
arcade.run()