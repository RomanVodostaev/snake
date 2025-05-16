from plot_point import PlotPoint

class ScreenRenderer:
    def render(self, points: list[PlotPoint]):
        
        max_x = 0
        max_y = 0
        
        points_dict = {}
        
        for p in points:
            if p.x > max_x: 
                max_x = p.x
            if p.y > max_y: 
                max_y = p.y
                
            points_dict[(p.x, p.y)] = p
        
        for plot_x in range(max_x + 1):
            for plot_y in range(max_y + 1):
                plot_key = (plot_x, plot_y)
                if plot_key in points_dict:
                    print(points_dict[plot_key].character, end="")
                else:
                    print(" ", end="")

            print()