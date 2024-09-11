from tkinter import Tk,BOTH,Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze")
        self.canvas = Canvas()
        self.canvas.pack()
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close())


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running == True:
            self.redraw()

    def close(self):
        self.window_running = False


