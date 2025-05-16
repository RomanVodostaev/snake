
import time

from game_field import GameField
from plot_point import PlotPoint
from screen_renderer import ScreenRenderer

field = GameField(20, 10)

points = [
    PlotPoint(0, 0, "*"),
    PlotPoint(0, 1, "*"),
    PlotPoint(0, 2, "*"),
    PlotPoint(0, 3, "*"),
    
    PlotPoint(1, 0, "*"),
    PlotPoint(2, 0, "*"),
    PlotPoint(3, 0, "*"),
    
    
    PlotPoint(3, 1, "*"),
    PlotPoint(3, 2, "*"),
    PlotPoint(3, 3, "*"),
    
    
    PlotPoint(1, 3, "*"),
    PlotPoint(2, 3, "*"),
]

renderer = ScreenRenderer()
renderer.render(points)

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