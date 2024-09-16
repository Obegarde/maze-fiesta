from random import choice, random, randrange
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
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x = _x1 
        self.y = _y1
        self.size = _size
        self._win = _win
        self.visited = False
        self.left_neighbour = None
        self.right_neighbour = None
        self.bottom_neighbour = None
        self.top_neighbour = None 
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
    
    def _break_walls_r(self):
        neighbours = [self.left_neighbour,self.right_neighbour,self.bottom_neighbour,self.top_neighbour] 
        self.visited = True
        while True:
            possible_directions = []
            for n in neighbours:
                if n != None and n.visited == False:
                    possible_directions.append(n)
            if len(possible_directions) == 0:
                self.draw()
                return
            else:
                selection = choice(possible_directions) 
                if selection == self.left_neighbour:
                    self.has_left_wall = False
                    selection.has_right_wall = False
                if selection == self.right_neighbour:
                    self.has_right_wall = False
                    selection.has_left_wall = False
                if selection == self.top_neighbour:
                    self.has_top_wall = False
                    selection.has_bottom_wall = False
                if selection == self.bottom_neighbour:
                    self.has_bottom_wall = False
                    selection.has_top_wall = False
                selection._break_walls_r()

    def _solve_r(self,maze): 
        maze._animate()
        self.visited = True
        if self == maze.exit_cell:
            return True
        if self.left_neighbour != None and self.left_neighbour.visited != True and self.has_left_wall != True and self.left_neighbour.has_right_wall != True:
            self.draw_move(self.left_neighbour)
            if self.left_neighbour._solve_r(maze) == True:
                return True
            else:
                self.draw_move(self.left_neighbour,True)
                            
        if self.right_neighbour != None and self.right_neighbour.visited != True and self.has_right_wall != True and self.right_neighbour.has_left_wall != True:
            self.draw_move(self.right_neighbour)
            if self.right_neighbour._solve_r(maze) == True:
                return True
            else:
                self.draw_move(self.right_neighbour,True)
         
        if self.top_neighbour != None and self.top_neighbour.visited != True and self.has_top_wall != True and self.top_neighbour.has_bottom_wall != True:
            self.draw_move(self.top_neighbour)
            if self.top_neighbour._solve_r(maze) == True:
                return True
            else:
                self.draw_move(self.top_neighbour,True)
        
        if self.bottom_neighbour != None and self.bottom_neighbour.visited != True and self.has_bottom_wall != True and self.bottom_neighbour.has_top_wall != True:
            self.draw_move(self.bottom_neighbour)
            if self.bottom_neighbour._solve_r(maze) == True:
                return True
            else:
                self.draw_move(self.bottom_neighbour,True)
        return False
