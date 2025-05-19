
import time

from game_field import GameField
from plot_point import PlotPoint
from screen_renderer import ScreenRenderer
from snake import Snake

field = GameField(64, 12)
snake = Snake(PlotPoint(10, 3, "Q"))

renderer = ScreenRenderer()
renderer.render(field.points + snake.points)

# try:
#     while True:
#         field.handle_input()
#         field.render()
#         field.update()
#         time.sleep(0.2)
# except KeyboardInterrupt:
#     # TODO: please use either English or Urkainian :)
#     print("\nGame over")
    
# TODO: General recomendation - separate logic, classes by modules (python files)