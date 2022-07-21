import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "STAR WARS"
LASER_SPEED = 5
ENEMY_SPEED = 1
ENEMY_DISTANCE = 50

class Meteorit(arcade.Sprite):
    def __init__(self):
        super().__init__("meteorit.png", 0.5)
        self.center_x = random.randint(0, SCREEN_WIDTH)
        self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT * 3)
        self.change_y = ENEMY_SPEED + LASER_SPEED
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT * 3)
            self.center_x = random.randint(0, SCREEN_WIDTH)

class TieFighter(arcade.Sprite):
    def __init__(self):
        super().__init__("TieFighter.png",0.3)
        self.change_y = ENEMY_SPEED

    def update(self):
        self.center_y -= self.change_y
        if self.center_y < -10:
            self.kill()



class Millennium_Falcon(arcade.Sprite):
    def __init__(self):
        super().__init__("falcon.png",0.3)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = 100

    def update(self):
        self.center_x += self.change_x



class Laser(arcade.Sprite):
    def __init__(self):
        super().__init__("laser.png", 0.8)
        self.center_x = window.falcon.center_x
        self.bottom = window.falcon.top
        self.change_y = LASER_SPEED
        self.laser_sound = arcade.load_sound("laser.wav")

    def update(self):
        self.center_y += self.change_y
        if self.center_y > SCREEN_HEIGHT:
            self.kill()



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("background.jpg")
        self.falcon = Millennium_Falcon()
        self.set_mouse_visible(False)
        self.lasers = arcade.SpriteList()
        self.enemies = arcade.SpriteList()
        self.game = True
        self.setup()
        self.win = arcade.load_texture("win.png")
        self.meteor = Meteorit()
        self.song_for_war = arcade.load_sound("A New Hope.mp3")
        self.player = arcade.play_sound(self.song_for_war, 0.2)

    def on_mouse_press(self,x,y,button,modifiers):
        if self.game:
            if button == arcade.MOUSE_BUTTON_LEFT:
                laser = Laser()
                self.lasers.append(laser)
                arcade.play_sound(sound=laser.laser_sound,volume=10)

    def on_mouse_motion(self,x,y,dx,dy):
        if self.game:
            self.falcon.center_x = x

    def setup(self):
        for i in range(50):
            tie_fighter = TieFighter()
            tie_fighter.center_x = random.randint(0,SCREEN_WIDTH)
            tie_fighter.center_y = SCREEN_HEIGHT + i * ENEMY_DISTANCE
            self.enemies.append(tie_fighter)




    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
        self.falcon.draw()
        self.lasers.draw()
        self.enemies.draw()
        if len(self.enemies) == 0:
            self.game = False
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win,)
        self.meteor.draw()

    def update(self, delta_time):
        if self.game:
            self.falcon.update()
            self.lasers.update()
            self.enemies.update()
            for laser in self.lasers:
                hit_list = arcade.check_for_collision_with_list(laser, self.enemies)
                if hit_list:
                    laser.kill()
                    for enemy in hit_list:
                        enemy.kill()
            self.meteor.update()
        if arcade.check_for_collision(self.meteor, self.falcon):
            # arcade.stop_sound(self.song_for_war)
            # arcade.stop_sound(self.player)
            self.game = False



window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()