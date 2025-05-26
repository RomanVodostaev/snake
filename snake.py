from plot_point import PlotPoint


class SnakeMoveDierection:
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    

class Snake:
    def __init__(self, head_point: PlotPoint):
        self.points: list[PlotPoint] = []
        
        for i in range(4):
            character = "0"
            
            if i == 0:
                character = head_point.character
            
            self.points.append(PlotPoint(head_point.x + i, head_point.y, character=character))
    
        self.direction = 'RIGHT'

    def move(self, direction: str):
        for index in range(len(self.points) - 1, -1, -1):
            if index == 0:
                if direction == SnakeMoveDierection.UP:
                    self.points[index].move(0, -1)
                elif direction == SnakeMoveDierection.DOWN:
                    self.points[index].move(0, 1)
                elif direction == SnakeMoveDierection.LEFT:
                    self.points[index].move(-1, 0)
                elif direction == SnakeMoveDierection.RIGHT:
                    self.points[index].move(1, 0)
                
                break
            
            prev_index = index-1
            self.points[index].set(self.points[prev_index].x, self.points[prev_index].y)

    # def grow(self):
    #     self.body.append(self.body[-1])

