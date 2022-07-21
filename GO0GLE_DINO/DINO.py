import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "ШАБЛОН"

class Cactus(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x
        if self.center_x <= 0:
            self.center_x = SCREEN_WIDTH
            window.score += 1

class DINO(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.5
        if self.center_y<=200:
            self.center_y = 200
            self.jump = False


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.background = arcade.load_texture("desert.png")
        self.dino = DINO(0.5)
        self.dino.textures = []
        self.dino.textures.append(arcade.load_texture("dino1.png"))
        self.dino.textures.append(arcade.load_texture("dino2.png"))
        self.dino.textures.append(arcade.load_texture("dino3.png"))
        self.cactus = Cactus("cactus2.png",0.5)
        self.score = 0
        self.game_over = arcade.load_texture("desertGO.png")
        self.game = True

    def setup(self):
        self.dino.center_x = 100
        self.dino.center_y = 200
        self.cactus.center_x = SCREEN_WIDTH
        self.cactus.center_y = 200
        self.cactus.change_x = 6


    def on_draw(self):
        arcade.start_render()
        if self.game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        else:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.game_over)
        arcade.set_background_color(arcade.color.AMAZON)
        self.dino.draw()
        self.cactus.draw()
        score_text = f"счёт:{self.score}"
        arcade.draw_text(score_text,330,550,arcade.color.RED_DEVIL,30)



    def update(self,delta_time):
        self.dino.update_animation()
        self.dino.update()
        self.cactus.update()
        if arcade.check_for_collision(self.cactus,self.dino):
            self.dino.stop()
            self.cactus.stop()
            self.game = False


    def on_key_release(self, key, modifiers):
        pass


    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.dino.jump == False:
            self.dino.change_y = 12
            self.dino.jump = True


window = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
window.setup()
arcade.run()