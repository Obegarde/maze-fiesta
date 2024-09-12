from graphics import Point, Line
class Cell:
    def __init__(self,
                 _x1,
                 _y1,
                 _size,
                 _win = None,
                 has_left_wall = True,
                 has_right_wall = True,
                 has_top_wall = True, 
                 has_bottom_wall = True,
                 ) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x = _x1 
        self.y = _y1
        self.size = _size
        self._win = _win
        
    def draw(self):
        top_color = "black"
        bottom_color = "black"
        left_color = "black"
        right_color = "black"
        if self._win == None:
            return

        leftwall = Line(Point(self.x, self.y),
                        Point(self.x, self.y + self.size),)
        
        rightwall = Line(Point(self.x + self.size, self.y),
                         Point(self.x + self.size, self.y + self.size))
       

        topwall = Line(Point(self.x, self.y),
                       Point(self.x + self.size,self.y))

        bottomwall = Line(Point(self.x, self.y + self.size),
                          Point(self.x + self.size, self.y + self.size))

        if self.has_top_wall == False:
            top_color = "white"
        if self.has_bottom_wall == False:
            bottom_color = "white"
        if self.has_left_wall == False:
            left_color = "white"
        if self.has_right_wall == False:
            right_color = "white"

        self._win.draw_line(leftwall, left_color)
        self._win.draw_line(rightwall,right_color) 
        self._win.draw_line(topwall, top_color)
        self._win.draw_line(bottomwall, bottom_color)




    def draw_move(self, to_cell, undo = False):
        if self._win == None:
            return
        move_line = Line(Point(self.x + self.size/2,
                               self.y + self.size/2),
                         Point(to_cell.x + to_cell.size/2,
                               to_cell.y + to_cell.size/2))
        if undo == False:
            self._win.draw_line(move_line,"red")
        else:
            self._win.draw_line(move_line,"grey")

