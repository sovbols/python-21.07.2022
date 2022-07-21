import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE ="Шаблон"

class Wall(arcade.Sprite):
    def update(self):
        self.center_y-=self.change_y
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
            self.center_x = random.randint(130,SCREEN_WIDTH-130)

class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.left < 50:
            self.left = 50
        if self.right > SCREEN_WIDTH - 50:
            self.right = SCREEN_WIDTH - 50
class OurGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.background = arcade.load_texture("background — копия.png")
        self.car = Car("car — копия.png",0.8)
        self.wall = Wall("wall — копия.png",0.6)
        self.score = 0




    def setup(self):
        self.car.center_x = SCREEN_WIDTH / 2
        self.car.center_y = 100
        self.wall.center_y = SCREEN_HEIGHT
        self.wall.center_x = SCREEN_WIDTH / 2
        self.wall.change_y = 6



    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.GRAY)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.car.draw()
        self.wall.draw()
        score_text = f"счёт:{self.score}"
        arcade.draw_text(score_text,60,560,arcade.color.GRAY,20)
        if self.score == 5:
            arcade.draw_text("WIN!!!",300,300,arcade.color.BLACK,30,30)

    def update(self,delta_time):
        self.car.update()
        self.wall.update()
        if self.score == 5:
            self.car.stop()
            self.wall.stop()
        if arcade.check_for_collision(self.car,self.wall):
            self.car.stop()
            self.wall.stop()

        if self.wall.center_y <= 0:
            self.score += 1
    def on_key_press(self,key,modifiers):
        if key==arcade.key.RIGHT:
            self.car.change_x = 5
            self.car.angle = -20
        if key==arcade.key.LEFT:
            self.car.change_x = -5
            self.car.angle = 20

    def on_key_release(self,key,modifiers):
        if key==arcade.key.RIGHT or key==arcade.key.LEFT:
            self.car.change_x = 0
            self.car.angle = 0

game = OurGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
game.setup()
arcade.run()