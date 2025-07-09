from snake import Snake
import keyboard
import os
from plot_point import PlotPoint

class GameField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.points: list[PlotPoint] = []
        
        for hi in range(height):
            for wi in range(width):
                if hi == 0:
                    self.points.append(PlotPoint(wi, hi, "_"))
                else:
                    if wi == 0:
                        self.points.append(PlotPoint(wi, hi, "|"))
                    if wi == width - 1:  
                        self.points.append(PlotPoint(wi, hi, "|"))
                    if hi == height - 1:
                        self.points.append(PlotPoint(wi, hi, "-"))

