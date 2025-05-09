
import time
import keyboard
import os

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = 'o'
        self.body = [(x, y)]
        self.direction = 'RIGHT'

    def get_coords(self):
        return self.body
        
    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'UP':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
        
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(width // 2, height // 2)
    
    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
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

field = GameField(20, 10)

try:
    while True:
        field.handle_input()
        field.render()
        field.update()
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nИгра окончена!")