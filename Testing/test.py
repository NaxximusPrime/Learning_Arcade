import arcade

SCREEM_WIDTH = 800
SCREEM_HEIGHT = 600

arcade.open_window(SCREEM_WIDTH, SCREEM_HEIGHT, "Drawing")

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()

arcade.draw_circle_filled(SCREEM_WIDTH / 2, SCREEM_HEIGHT / 2, 50, arcade.color.FOREST_GREEN)

arcade.finish_render()

arcade.run()
