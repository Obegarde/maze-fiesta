from graphics import Line, Window, Point,Cell


def main():
    win = Window(800, 600)
    cell1 = Cell(10,10,100,win)
    cell1.draw()
    win.wait_for_close()

    


main()
