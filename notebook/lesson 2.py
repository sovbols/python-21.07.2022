import arcade
SCREEN_WIDTH=600
SCREEN_HEIGHT=600
SCREEN_TITLE="ШАБЛОН"

class OurGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.center_X=300
        self.center_Y=300
        self.radius=50
        self.change_X=5
        self.change_Y=5


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        arcade.draw_circle_filled(self.center_X,self.center_Y,self.radius,arcade.color.BLUEBERRY)

    def update(self,delta_time):
        self.center_X+=self.change_X
        if self.center_X + self.radius > SCREEN_WIDTH or self.center_X-self.radius < 0:
            self.change_X=-self.change_X
        self.center_Y+=self.change_Y
        if self.center_Y + self.radius > SCREEN_HEIGHT or self.center_Y-self.radius < 0:
            self.change_Y=-self.change_Y


game=OurGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()
