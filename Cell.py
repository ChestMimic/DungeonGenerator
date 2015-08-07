#A Cell is a base unit of measurement to be used when making a dungeon's map. 
#Cell consists of it's own X and Y position, and NSEW directionality

class Cell:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
		self.north = False
		self.south = False
		self.east = False
		self.west = False
			
    #Determine equality by whether or not two cells occupy the same X-Y space
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
		
	def canGoNorth(self):
		return self.north
		
	def canGoSouth(self):
		return self.south
		
	def canGoEast(self):
		return self.east
		
	def canGoWest(self):
		return self.west