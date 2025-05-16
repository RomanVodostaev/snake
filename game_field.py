from snake import Snake
import keyboard
import os

class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(width // 2, height // 2)
    
    def render(self):
        self.clear_screan()
        
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    print('*', end='')
                elif (x, y) in self.snake.get_coords():
                    print('O', end='')
                else:
                    print(' ', end='')
            print()
    
    def update(self):
        self.snake.move()

    def handle_input(self):
        if keyboard.is_pressed('up') and self.snake.direction != 'DOWN':
            self.snake.direction = 'UP'
        elif keyboard.is_pressed('down') and self.snake.direction != 'UP':
            self.snake.direction = 'DOWN'
        elif keyboard.is_pressed('left') and self.snake.direction != 'RIGHT':
            self.snake.direction = 'LEFT'
        elif keyboard.is_pressed('right') and self.snake.direction != 'LEFT':
            self.snake.direction = 'RIGHT'
            
    def clear_screan(self):
        os.system('cls' if os.name == 'nt' else 'clear')

