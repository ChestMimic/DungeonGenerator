class Cell:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
		self.north = False
		self.south = False
		self.east = False
		self.west = False
			
	def __eq__(self, other):
		return self.xPos == other.xPos and self.yPos == other.yPos
		
	def isNorthOf(self, other):
		return self.yPos < other.yPos
		
	def isSouthOf(self, other):
		return self.yPos > other.yPos
		
	def isEastOf(self, other):
		return self.xPos < other.xPos
		
	def isWestOf(self, other):
		return self.xPos > other.xPos