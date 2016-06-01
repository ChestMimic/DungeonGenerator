#A Map is a list of Cells, with metadata providing X and Y bounds
from DungeonGenerator import Cell

class Grid(object):
	def __init__(self, boundA, boundB):
		self.xBound = boundA
		self.yBound = boundB
		self.lst = []
		#create the list of all Cells
		for x in range(0, xBound):
			for y in range(0, yBound):
				self.lst.append(Cell(x, y))

if __name__ == "__main__":
	mp = Grid(5, 5)
	mp.printMap()