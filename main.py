
import time

from game_field import GameField
from plot_point import PlotPoint
from screen_renderer import ScreenRenderer
from snake import Snake, SnakeMoveDierection

import keyboard

field = GameField(64, 12)
snake = Snake(PlotPoint(10, 3, "Q"))

renderer = ScreenRenderer()

snake_direction = SnakeMoveDierection.LEFT

snake_state = {"direction": SnakeMoveDierection.LEFT}

keyboard.add_hotkey('down', lambda: snake_state.update({"direction": SnakeMoveDierection.DOWN}))
keyboard.add_hotkey('left', lambda: snake_state.update({"direction": SnakeMoveDierection.LEFT}))
keyboard.add_hotkey('right', lambda: snake_state.update({"direction": SnakeMoveDierection.RIGHT}))
keyboard.add_hotkey('up', lambda: snake_state.update({"direction": SnakeMoveDierection.UP}))
# keyboard.wait()

try:
    while True:
        renderer.clear_screan()
        
        
        
        snake.move(snake_state["direction"])
        
        renderer.render(field.points + snake.points)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nGame over")