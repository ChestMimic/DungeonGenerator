#A Cell is a base unit of measurement to be used when making a dungeon's map. 
#Cell consists of it's own X and Y position, and NSEW directionality

class Cell:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
		self.joined = []


    #Determine equality by whether or not two cells occupy the same X-Y space
	def __eq__(self, other):
		return self.xPos == other.xPos and self.yPos == other.yPos
		
	#depreceated
	def isNorthOf(self, other):
		return self.yPos < other.yPos
		
	#depreceated
	def isSouthOf(self, other):
		return self.yPos > other.yPos
		
	#depreceated
	def isEastOf(self, other):
		return self.xPos < other.xPos
		
	#depreceated
	def isWestOf(self, other):
		return self.xPos > other.xPos
		

	def joinCell(self, CellB):
		if(CellB not in self.joined):
			self.joined.append(CellB)
			cellB.joinCell(self)

	#depreceated
	def isIsolated(self):
		if len(self.joined) == 0:
			return True
		return False

	def __str__(self):
		return "X"