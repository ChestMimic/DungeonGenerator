#A Map is a list of Cells, with metadata providing X and Y bounds
from Cell import Cell

class Map:
    def __init__(self, xBound, yBound):
        self.xBound = xBound
        self.yBound = yBound
        self.lst = []
        #create the list of all Cells
        for x in range(0, xBound-1):
            for y in range(0, yBound-1):
                self.lst.append(Cell(x, y))