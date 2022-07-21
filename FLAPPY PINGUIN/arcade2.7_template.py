import arcade

# устанавливаем константы
SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Шаблон"


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    # начальные значения
    def setup(self):
        pass

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)

    # игровая логика
    def update(self, delta_time):
        pass

    # нажать на клавишу
    def on_key_press(self, key, modifiers):
        pass

    # отпустить клавишу 

    def on_key_release(self, key, modifiers): 
        pass



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
