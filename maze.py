from cell import Cell
import time
class Maze: 
    def __init__(self,
                 x,
                 y,  
                 num_rows,
                 num_cols,
                 cell_size,
                 win = None,
                 ) -> None:
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._x + self._cell_size * j ,self._y + self._cell_size * i,self._cell_size,self._win))
            self._cells.append(column)
        self.force_draw_all_cells() 


    def force_draw_all_cells(self):
        for col in self._cells:
            for cell in col:
                self._draw_cell(cell)
        

    def _draw_cell(self,cell):
        if self._win is None:
            return
        cell.draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0] 
        exit_cell =  self._cells[self._num_cols - 1][self._num_rows - 1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        self._draw_cell(entrance_cell)
        self._draw_cell(exit_cell)
