from plot_point import PlotPoint


class Snake:
    def __init__(self, head_point: PlotPoint):
        self.points: list[PlotPoint] = []
        
        for i in range(4):
            character = "0"
            
            if i == 0:
                character = head_point.character
            
            self.points.append(PlotPoint(head_point.x + i, head_point.y, character=character))
    
        self.direction = 'RIGHT'

    # def get_coords(self):
    #     return self.body
        
    # def move(self):
    #     head_x, head_y = self.body[0]
    #     if self.direction == 'UP':
    #         new_head = (head_x, head_y - 1)
    #     elif self.direction == 'DOWN':
    #         new_head = (head_x, head_y + 1)
    #     elif self.direction == 'LEFT':
    #         new_head = (head_x - 1, head_y)
    #     elif self.direction == 'RIGHT':
    #         new_head = (head_x + 1, head_y)
        
    #     self.body.insert(0, new_head)
    #     self.body.pop()

    # def grow(self):
    #     self.body.append(self.body[-1])
