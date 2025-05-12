
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
