#A Map is a list of Cells, with metadata providing X and Y bounds
from Cell import Cell

class Map:
    def __init__(self, xBound, yBound):
        self.xBound = xBound
        self.yBound = yBound
        self.lst = []
        #create the list of all Cells
        for x in range(0, xBound):
            for y in range(0, yBound):
                self.lst.append(Cell(x, y))

if __name__ == "__main__":
    mp = Map(5, 5)
    for c in mp.lst:
        print(c)