import arcade
import random

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Шаблон"

class ColumnTop(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= -30:
            self.center_x = SCREEN_WIDTH + 50
            self.center_y = random.randint(390, 480)
            window.score += 1

class ColumnBotom(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= -30:
            self.center_x = SCREEN_WIDTH + 50
            self.center_y = random.randint(0,90)

class Pinguin(arcade.AnimatedTimeSprite):
    def __init__(self):
        super().__init__(1)
        self.textures = []
        self.textures.append(arcade.load_texture("penguin1.png"))
        self.textures.append(arcade.load_texture("penguin2.png"))
        self.textures.append(arcade.load_texture("penguin3.png"))

    def update(self):
        self.center_y+=self.change_y
        self.angle+=self.change_angle
        self.change_y -= 0.4
        if self.center_y < 10:
            self.center_y = 10
        if self.center_y > SCREEN_HEIGHT - 10:
            self.center_y = SCREEN_HEIGHT - 10
        self.change_angle -= 0.4
        if self.angle > 40:
            self.angle = 40
        if self.angle < -30:
            self.angle = -30

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super(). __init__(width,height,title)
        self.background = arcade.load_texture("space.png")
        self.pinguin = Pinguin()
        self.columns = arcade.SpriteList()
        self.score = 0
        self.stop = False

    def setup(self):
        self.pinguin.center_x = 100
        self.pinguin.center_y = 180
        self.pinguin.change_y = 0
        self.pinguin.change_angle = 0
        for i in range(5):
            columnTop = ColumnTop("column_top.png", 1)
            columnTop.center_x = 150 * i + SCREEN_WIDTH
            columnTop.center_y = random.randint(390, 480)
            columnTop.change_x = 3
            self.columns.append(columnTop)
            columnBotom = ColumnBotom("column_bottom.png", 1)
            columnBotom.center_x = 150 * i + SCREEN_WIDTH
            columnBotom.center_y = random.randint(0,90)
            columnBotom.change_x = 3
            self.columns.append(columnBotom)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.pinguin.draw()
        self.columns.draw()
        score_text = f"Счёт: {self.score}"
        arcade.draw_text(score_text,30,SCREEN_HEIGHT - 50,arcade.color.REDWOOD,30)

    def update(self, delta_time):
        self.pinguin.update_animation()
        self.pinguin.update()
        self.columns.update()
        hit_list = arcade.check_for_collision_with_list(self.pinguin, self.columns)
        if len(hit_list) > 0:
            self.pinguin.stop()
            self.stop = True
            for column in self.columns:
                column.stop()

    def on_key_press(self,key,modifiers):
        if arcade.key.SPACE == key and self.stop == False:
            self.pinguin.change_y = 5
            self.pinguin.change_angle = 5

window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
window.setup()
arcade.run()