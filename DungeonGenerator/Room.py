class Room():
	def __init__(self, xPos, yPos, xSize, ySize):
		self.xPos = xPos
		self.yPos = yPos
		self.xSize = xSize
		self.ySize = ySize

	def isRoomValid(self):
		if self.xPos >= 0 and self.yPos >= 0:
			if self.xSize > 0 or self.ySize > 0:
				return True
		return False

	def roomsOverlap(self, room2):
		xAlpha = range(self.xPos, self.xPos + self.xSize)
		xBravo = range(room2.xPos, room2.xPos +room2.xSize)
		xaSet = set(xAlpha)
		xInter = xaSet.intersection(xBravo)

		if xInter:
			yAlpha = range(self.yPos, self.yPos + self.ySize)
			yBravo = range(room2.yPos, room2.yPos +room2.ySize)
			yaSet = set(yAlpha)
			yInter = yaSet.intersection(yBravo)
			if yInter:
				return True
		return False