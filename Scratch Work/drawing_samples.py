# importing the arcade library
import arcade

# creating a window with the width and height of 600 and a title
arcade.open_window(600, 600, "Drawing Example")

# setting a default background color for the window to SKY_BLUE
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# telling the program to start drawing something
arcade.start_render()

# draw a rectangle as grass at the bottom of the window
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)

# drawing a tree trunk
arcade.draw_rectangle_filled(100, 300, 20, 60, arcade.csscolor.SIENNA)
# drawing the tree top as circle
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.GREEN)

# drawing a tree with an ellipse top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.GREEN)

# drawing a tree with an arc top
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.GREEN, 0, 180)

# drawing a tree with a triangle top
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.GREEN)

# drawing a tree with a polygon top
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400), (480, 360), (470, 320), (530, 320), (520, 360)), arcade.csscolor.DARK_GREEN)

# draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.csscolor.YELLOW)

# draw rays to the left, right, up and down
arcade.draw_line(500, 550, 400, 550, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.csscolor.YELLOW, 3)

# draw diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.csscolor.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.csscolor.YELLOW, 3)

# draw text at (150, 230) with a font size of 24 pts.
arcade.draw_text("Arbor Day - Plant a Tree!", 150, 230, arcade.csscolor.BLACK, 24)

# telling the program to stop drawing
arcade.finish_render()

# telling the program to start until it will be closed
arcade.run()
