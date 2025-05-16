
# point = PlotPoint(10, 12, "*")
class PlotPoint:
    x: int
    y: int
    character: str
    
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.character = character
        
        
    def move(self, x_offset, y_offset):
        self.x = self.x + x_offset
        self.y = self.y + y_offset
        
    
    def set(self, x, y):
        self.x = x
        self.y = y