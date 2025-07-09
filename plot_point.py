
# point = PlotPoint(10, 12, "*")
class PlotPoint:
    x: int
    y: int
    character: str
    
    def __init__(self, x, y, character = ""):
        self.x = x
        self.y = y
        self.character = character
        
        
    def move(self, x_offset, y_offset):
        self.x = self.x + x_offset
        self.y = self.y + y_offset
        
    
    def set(self, x, y):
        self.x = x
        self.y = y


    def is_equals(self, point) -> bool:
        return self.x == point.x and self.y == point.y
    

            
def get_points_from_text(start_x, start_y, text: str):
    points: list[PlotPoint] = []
    
    for i in range(len(text)):
        points.append(PlotPoint(start_x + i, start_y, text[i]))
        
    return points