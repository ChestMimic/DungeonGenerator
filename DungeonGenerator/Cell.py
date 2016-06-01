#A Cell is a base unit of measurement to be used when making a dungeon's map. 
#Cell consists of it's own X and Y position, and NSEW directionality

class Cell:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
		self.north = None
		self.south = None
		self.east = None
		self.west = None


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
		

	def canGoNorth(self):
		if self.north == None
			return False
		return True
		
	def canGoSouth(self):
		if self.south == None
			return False
		return True
		
	def canGoEast(self):
		if self.east == None
			return False
		return True
		
	def canGoWest(self):
		if self.west == None
			return False
		return True

	#depreceated
	def isClean(self):
		return self.canGoEast() == False and self.canGoNorth() == False and self.canGoSouth() == False and self.canGoWest() == False

	def __str__(self):
		return "X"