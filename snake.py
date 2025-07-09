from plot_point import PlotPoint


class SnakeMoveDierection:
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    
class SnakeChars:
    HEAD = "1"
    BODY = "0"

class Snake:
    def __init__(self, head_point: PlotPoint):
        self.points: list[PlotPoint] = []
        
        for i in range(4):
            character = SnakeChars.HEAD if i == 0 else SnakeChars.BODY
            self.points.append(PlotPoint(head_point.x + i, head_point.y, character=character))


    def move(self, direction: str, backward: bool = False):
        
        indexes_range = range(len(self.points)) if backward else range(len(self.points) - 1, -1, -1)
        
        for index in indexes_range:
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


    def append_point(self, point: PlotPoint):
        self.points.insert(0, point)
        self.points[0].character = SnakeChars.HEAD
        self.points[1].character = SnakeChars.BODY

