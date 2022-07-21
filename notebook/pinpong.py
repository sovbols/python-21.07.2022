import arcade

SCREEN_WIDTH=600
SCREEN_HEIGHT=600
SCREEN_TITLE="ШАБЛОН"

class Ball(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        self.center_y+=self.change_y
        if self.left<0 or self.right>SCREEN_WIDTH:
            self.change_x=-self.change_x
        if self.bottom<0 or self.top>SCREEN_HEIGHT:
            self.change_y=-self.change_y


class Bar(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        if self.right>SCREEN_WIDTH:
            self.right=SCREEN_WIDTH
        if self.left<0:
            self.left=0

class OurGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.ball=Ball("ball.png",0.7)
        self.bar=Bar("bar.png",0.5)
        self.score=0
        self.attempts=3
    def setup(self):
        self.ball.center_x=300
        self.ball.center_y=300
        self.ball.change_x=4
        self.ball.change_y=4
        self.bar.center_x=300
        self.bar.center_y=150
        self.bar.change_x=0

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.DUTCH_WHITE)
        self.ball.draw()
        self.bar.draw()
        text_score=f"Счёт: {self.score}"
        arcade.draw_text(text_score,10,570,arcade.color.BLACK,20)
        attempts=f"Жизни: {self.attempts}"
        arcade.draw_text(attempts,470,570,arcade.color.BLACK,20)
        speed_x=f"Скорость {self.ball.change_x}"
        arcade.draw_text(speed_x,300,570,arcade.color.RED_DEVIL)
        speed_y = f"Скорость {self.ball.change_y}"
        arcade.draw_text(speed_y,100, 570, arcade.color.RED_DEVIL)


    def update (self,delta_time):
        self.ball.update()
        self.bar.update()
        if arcade.check_for_collision(self.bar,self.ball):
            self.ball.bottom=self.bar.top
            self.ball.change_y=-self.ball.change_y
            self.score+=1
            print(self.score)
        if self.ball.bottom<0:
            self.attempts-=1
            self.ball.center_y=500

    def on_key_press(self,key,modifiers):
        if key==arcade.key.RIGHT:
            self.bar.change_x=10
        if key==arcade.key.LEFT:
            self.bar.change_x=-10

    # def on_key_release(self,key,modifiers):
    #     if key==arcade.key.RIGHT or key==arcade.key.LEFT:
    #         self.bar.change_x=0

game=OurGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
game.setup()
arcade.run()