from plot_point import PlotPoint
import random


class Food:
    def __init__(self):
        self.point = PlotPoint(0, 0, "@")
        
        
    # max_x and max_y not inclusive
    def random_place(self, max_x, max_y):
        self.point.set(random.randint(1, max_x - 2), random.randint(1, max_y - 2))
        
    
class FoodCollection:
    def __init__(self):
        self.items: list[Food] = []
        
        
    def place_random_food(self, max_x, max_y):
        food = Food()
        food.random_place(max_x, max_y)
        
        self.items.append(food)
        
        
    def get_food_points(self):
        points = []
        
        for f in self.items:
            points.append(f.point)
            
        return points
    
    
    def has_any(self):
        return len(self.items) > 0
    
    
    def clear(self):
        self.items.clear()