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

def move_up(): 
    global snake_direction
    
    if snake_direction == SnakeMoveDierection.DOWN:
        return
    
    snake_direction = SnakeMoveDierection.UP

def move_left(): 
    global snake_direction
    
    if snake_direction == SnakeMoveDierection.RIGHT:
        return
    
    snake_direction = SnakeMoveDierection.LEFT
    
def move_right(): 
    global snake_direction
    
    if snake_direction == SnakeMoveDierection.LEFT:
        return

    snake_direction = SnakeMoveDierection.RIGHT
    
def move_down(): 
    global snake_direction
    
    if snake_direction == SnakeMoveDierection.UP:
        return

    snake_direction = SnakeMoveDierection.DOWN


keyboard.add_hotkey('down', move_down)
keyboard.add_hotkey('left', move_left)
keyboard.add_hotkey('right', move_right)
keyboard.add_hotkey('up', move_up)

try:
    while True:
        renderer.clear_screan()
        renderer.render(field.points + snake.points)
        
        snake.move(snake_direction)

        

        time.sleep(0.15)
except KeyboardInterrupt:
    print("\nGame over")
