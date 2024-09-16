from cell import Cell
import time
import random
class Maze: 
    def __init__(self,
                 x,
                 y,  
                 num_cols,
                 num_rows,
                 cell_size,
                 win = None,
                 seed = None,
                 ) -> None:
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._win = win
        self._cells = []
        self.seed = random.seed(seed)
        self._create_cells()
        self.entrance_cell = self._cells[0][0] 
        self.exit_cell =  self._cells[self._num_rows - 1][self._num_cols - 1]
        self._break_entrance_and_exit()
        self._add_neighbour_links()
        self._cells[0][0]._break_walls_r()
        self._reset_cells_visited()
    def _create_cells(self):
        for i in range(self._num_rows):
            column = []
            for j in range(self._num_cols):
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
        

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.entrance_cell.has_top_wall = False
        self.exit_cell.has_bottom_wall = False
        self._draw_cell(self.entrance_cell)
        self._draw_cell(self.exit_cell)
    
    def _add_neighbour_links(self):               
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                if j > 0:
                    self._cells[i][j].left_neighbour = self._cells[i][j - 1]
             
                if i > 0:
                    self._cells[i][j].top_neighbour = self._cells[i - 1][j]
              
                if j + 1< self._num_cols:
                    self._cells[i][j].right_neighbour = self._cells[i][j + 1]
               
                if i + 1 < self._num_rows:
                    self._cells[i][j].bottom_neighbour = self._cells[i + 1][j]
           
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False


    def solve(self):
        return self._cells[0][0]._solve_r(self)
