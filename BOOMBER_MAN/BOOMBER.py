import arcade
import random
import animate

SCREEN_TITLE = "Boomberman"
CELL_WIDTH = 60
CELL_HEIGHT = 60
ROW_COUNT = 11
COLUMN_COUNT = 11
SCREEN_WIDTH = CELL_WIDTH * COLUMN_COUNT
SCREEN_HEIGHT = CELL_HEIGHT * ROW_COUNT
PLAYER_1_SPEED = 2

def difference(coordinate, distance):
    return coordinate * distance + distance / 2

def justify_x(position_x):
    pass

def justify_y(position_y):
    pass


class BOOMBER_MAN(animate.Animate):
    def __init__(self, speed):
        super().__init__("file/Bomberman/Front/Bman_F_f00.png",0.5)
        # Front
        self.walk_down_frames = []
        for i in range(8):
            self.walk_down_frames.append(arcade.load_texture(f"file/Bomberman/Front/Bman_F_f0{i}.png"))
        # Back
        self.walk_up_frames = []
        for i in range(8):
            self.walk_up_frames.append(arcade.load_texture(f"file/Bomberman/Back/Bman_B_f0{i}.png"))
        # Right
        self.walk_right_frames = []
        for i in range(8):
            self.walk_right_frames.append(arcade.load_texture(f"file/Bomberman/Side/Bman_F_f0{i}.png"))
        # Left
        self.walk_left_frames = []
        for i in range(8):
            self.walk_left_frames.append(arcade.load_texture(f"file/Bomberman/Side/Bman_F_f0{i}.png",
            flipped_horizontally = True)
            )
        self.direction = 3
        self.motion = 0
        self.speed = speed
    def costume_change(self):
        if self.direction == 1:
            self.textures = self.walk_left_frames
        elif self.direction == 2:
            self.textures = self.walk_right_frames
        elif self.direction == 3:
            self.textures = self.walk_up_frames
        elif self.direction == 4:
            self.textures = self.walk_down_frames

    def to_up(self):
        if not self.motion:
            self.motion = 1
            self.direction = 3
            self.change_y = self.speed
    def to_down(self):
        if not self.motion:
            self.motion = 1
            self.direction = 4
            self.change_y = -self.speed
    def to_left(self):
        if not self.motion:
            self.motion = 1
            self.direction = 1
            self.change_x = -self.speed
    def to_right(self):
        if not self.motion:
            self.motion = 1
            self.direction = 2
            self.change_x = self.speed

    def to_stop(self):
        self.change_x = 0
        self.change_y = 0
        self.motion = 0
        self.direction = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        if self.bottom < 0:
            self.bottom = 0
        block_hit = arcade.check_for_collision_with_list(self, window.solid_blocks)
        if len(block_hit) > 0:
            for block in block_hit:
                if self.left < block.right and self.direction == 1:
                    self.left = block.right
                if self.right > block.left and self.direction == 2:
                    self.right  = block.left
                if self.top > block.bottom and self.direction == 3:
                    self.top = block.bottom
                if self.bottom < block.top and self.direction == 4:
                    self.bottom = block.top
        self.collisions(window.solid_blocks)
        self.collisions(window.exploadable_blocks)

    def collisions(self, spritelist):
        block_hit = arcade.check_for_collision_with_list(self,spritelist)
        if len(block_hit) > 0:
            for block in block_hit:
                if self.direction == 3 and self.top >= block.bottom:
                    self.top = block.bottom
                elif self.direction == 4 and self.bottom <= block.top:
                    self.bottom = block.top
                elif self.direction == 2 and self.right >= block.left:
                    self.right = block.left
                elif self.direction == 1 and self.left <= block.right:
                    self.left = block.right

class Bomb(animate.Animate):
    def __init__(self):
        super().__init__(f"file/Bomb/Bomb_f00.png", 0.7)
        for i in range(3):
            self.append_texture(arcade.load_texture(f"file/Bomb/Bomb_f0{i}.png"))


class Exploadable_block(arcade.Sprite):
    def __init__(self):
        super().__init__("file/Blocks/ExplodableBlock.png", 1)

class Solid_block(arcade.Sprite):
    def __init__(self):
        super().__init__("file/Blocks/SolidBlock.png", 1)

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("file/Blocks/BackgroundTile.png")
        self.solid_blocks = arcade.SpriteList()
        self.exploadable_blocks = arcade.SpriteList()
        self.bombs_player1 = arcade.SpriteList()
        self.bomberman = BOOMBER_MAN(PLAYER_1_SPEED)
        self.setup()


    def setup(self):
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                if x%2 == 1 and y%2 == 1:
                    solid_block = arcade.Sprite("file/Blocks/SolidBlock.png")
                    solid_block.center_x = difference(x, CELL_WIDTH)
                    solid_block.center_y = difference(y, CELL_HEIGHT)
                    self.solid_blocks.append(solid_block)


                elif random.randint(1,2) == 1:
                    if (not(x == 0 and x <= 2)
                    and not (y == 0 and x <=2)
                    and not(x == ROW_COUNT-1 and y >= COLUMN_COUNT - 3)
                    and not(y == COLUMN_COUNT - 1 and x >= ROW_COUNT - 3)):
                        exp_block = Exploadable_block()
                        exp_block.center_x = difference(x, CELL_WIDTH)
                        exp_block.center_y = difference(y, CELL_HEIGHT)
                        self.exploadable_blocks.append(exp_block)

        x = SCREEN_WIDTH / COLUMN_COUNT - CELL_WIDTH / 2
        y = SCREEN_HEIGHT / ROW_COUNT - CELL_HEIGHT / 2
        self.bomberman.set_position(x, y)

    def draw_background(self):
        for y in range(ROW_COUNT):
            for x in range(COLUMN_COUNT):
                arcade.draw_texture_rectangle(x * CELL_WIDTH + CELL_WIDTH / 2, y * CELL_HEIGHT + CELL_HEIGHT / 2, CELL_WIDTH, CELL_HEIGHT, self.bg)

    def on_draw(self):
        self.clear()
        self.draw_background()
        self.solid_blocks.draw()
        self.exploadable_blocks.draw()
        self.bomberman.draw()
        self.bombs_player1.draw()

    def update(self, delta_time):
        self.bomberman.update_animation(delta_time)
        self.bomberman.update()
        self.bombs_player1.update()
        self.bombs_player1.update_animation(delta_time)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
           self.bomberman.to_left()

        elif key == arcade.key.RIGHT:
            self.bomberman.to_right()

        elif key == arcade.key.UP:
            self.bomberman.to_up()

        elif  key == arcade.key.DOWN:
            self.bomberman.to_down()

        self.bomberman.costume_change()

        if key == arcade.key.SPACE:
            bomb = Bomb()
            bomb.center_x = self.bomberman.center_x
            bomb.center_y = self.bomberman.center_y
            self.bombs_player1.append(bomb)

    def on_key_release(self, key, modifiers):
        if arcade.key.LEFT == key or arcade.key.RIGHT == key or arcade.key.UP == key or arcade.key.DOWN == key:
            self.bomberman.to_stop()

window = Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
arcade.run()