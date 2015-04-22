import sys
import random

class Cursor:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
		
class Wall:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
	
	
def printMap():
	for x in range(0, xDun):
		for y in range(0, yDun):
			sys.stdout.write(str(MapOfDun[x][y]))
		sys.stdout.write("\n")
	return
	
def digMaze(xDun, yDun):
	xStart = 0
	yStart = 0
	listOfWalls = []	
	while True:
		xStart = random.randrange(0, xDun-1)
		yStart = random.randrange(0, yDun-1)
		if MapOfDun[xStart][yStart] == '*':
			break
	
	crsr = Cursor(xStart, yStart)
	
	#Wall in map
	for x in range(0, xDun):
		for y in range(0, yDun):
			if x != 0 and x != xDun-1 and y != 0 and y != yDun-1:
				continue
			MapOfDun[x][y] = '#'
	
		

xDun = 30
yDun = 50
roomMaxPercent = .25
roomAttempts = 1000

MapOfDun = [['*' for x in range(yDun)] for x in range(xDun)]

		

digMaze(xDun, yDun)
printMap()