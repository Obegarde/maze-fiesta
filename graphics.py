from tkinter import Tk,BOTH,Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze")
        self.__canvas = Canvas(self.__root, bg ="white")
        self.__canvas.pack(fill = BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("window closed")

    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color = "black"):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_one,point_two):
        self.point_one = point_one
        self.point_two = point_two
    def draw(self,canvas, fill_color = "black"):
        canvas.create_line(
                self.point_one.x, 
                self.point_one.y,
                self.point_two.x,
                self.point_two.y,
                fill = fill_color,
                width=2)
    

class Cell:
    def __init__(self,
                 _x1,
                 _y1,
                 _size,
                 _win,
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
        if self.has_left_wall:
            leftwall = Line(Point(self.x, self.y),
                            Point(self.x, self.y + self.size))
            self._win.draw_line(leftwall)
        if self.has_right_wall:
            rightwall = Line(Point(self.x + self.size, self.y),
                             Point(self.x + self.size, self.y + self.size))
            self._win.draw_line(rightwall)
        if self.has_top_wall:
            topwall = Line(Point(self.x, self.y),
                           Point(self.x + self.size,self.y))
            self._win.draw_line(topwall)
        if self.has_bottom_wall:
            bottomwall = Line(Point(self.x, self.y + self.size),
                              Point(self.x + self.size, self.y + self.size))
            self._win.draw_line(bottomwall)
