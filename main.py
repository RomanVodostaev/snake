import time

from game_field import GameField
from plot_point import *
from screen_renderer import *
from snake import Snake, SnakeMoveDierection
from snake_collapsed_with_object_error import SnakeCollapsedWithObjectError
from food import *
import asyncio
import keyboard

field = GameField(64, 12)
snake = Snake(PlotPoint(10, 3))

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

food_collection = FoodCollection()

render_delay = 0.005
snake_movement_delay = 0.01
snake_speed = 4

async def render_screan():
    global snake
    global field
    global food_collection
    global renderer
    global render_delay
    
    while True:
        renderer.clear_screan()
        renderer.render(field.points + food_collection.get_food_points() + snake.points)
        await asyncio.sleep(render_delay)


async def check_points_collision():
    global snake
    global field
    global food_collection
    global render_delay
    global snake_speed
    
    while True:
        
        # check if snake collades field barrier
        for snake_p in snake.points:
            for field_p in field.points:
                if snake_p.is_equals(field_p):
                    raise SnakeCollapsedWithObjectError()
                
        
        # check if snake eats any food
        for food_p in food_collection.get_food_points():
            if snake.points[0].is_equals(food_p):
                food_collection.clear()
                snake.append_point(food_p)
                snake.move(snake_direction, backward=True)
                snake_speed += 0.3
        
        
        # place food                
        if not food_collection.has_any():
            food_collection.place_random_food(field.width, field.height)


        await asyncio.sleep(render_delay)


async def move_snake():
    global snake
    global snake_movement_delay
    global snake_speed
    
    while True:
        snake.move(snake_direction)
        await asyncio.sleep(snake_movement_delay * (20 - snake_speed))


def render_game_over():
    renderer.clear_screan()
    
    game_over_text_points = get_points_from_text(25, 5, "GAME OVER!")
    renderer.render(field.points + game_over_text_points)


async def main():
    await asyncio.gather(
        asyncio.create_task(render_screan()),
        asyncio.create_task(move_snake()),
        asyncio.create_task(check_points_collision()),
    )


try:
    asyncio.run(main())
except KeyboardInterrupt:
    render_game_over()
except SnakeCollapsedWithObjectError:
    render_game_over()