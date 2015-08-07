#A Map is a list of Cells, with metadata providing X and Y bounds
from DungeonGenerator import Cell as DGCell

class Grid(object):
	def __init__(self, xBound, yBound):
		self.xBound = xBound
		self.yBound = yBound
		self.lst = []
		#create the list of all Cells
		for x in range(0, xBound):
			for y in range(0, yBound):
				self.lst.append(DGCell.Cell(x, y))

	#For testing only
	def printMap(self):
		lines = [] 
		#theoretically, Cells are in order of X
		#Future versions should confirm
		ch = "\r"
		flag = 0
		for c in self.lst:
			if c.xPos != flag:
				lines.append(ch)
				ch = "\r"
				flag += 1
			ch += str(c)
		lines.append(ch)	

		for l in lines:
			print(l)

if __name__ == "__main__":
	mp = Grid(5, 5)
	mp.printMap()