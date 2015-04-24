import sys	#for newline free print
import random 	#pseudorng access
import math

class Room:
	#standard room object
	#box shaped
	def __init__(self, xPos, yPos, xSize, ySize):
		self.xPos = xPos
		self.yPos = yPos
		self.xSize = xSize
		self.ySize = ySize
	def __lt__(self, other):
		return ((self.xPos, self.yPos, self.xSize, self.ySize) <
			(other.xPos, other.yPos, other.xSize, other.ySize))
		
def printMap():
	for x in range(0, xDun):
		for y in range(0, yDun):
			sys.stdout.write(str(MapOfDun[x][y]))
		sys.stdout.write("\n")
	return
	
def erectRoom(roomVal='#'):
	# stuff a random room in the map
	xRoom = random.randrange(3, int(round(xDun*roomMaxPercent))) 
	yRoom = random.randrange(3, int(round(yDun*roomMaxPercent))) 
	xPos = random.randrange(0, xDun-xRoom-1)
	yPos = random.randrange(0, yDun-yRoom-1)
	
	for x in range(xPos, xPos+xRoom):
		for y in range(yPos, yPos+yRoom):
			if MapOfDun[x][y] != '*':
				return None
	
	for x in range(xPos, xPos+xRoom):
		for y in range(yPos, yPos+yRoom):
			newRoom = Room(xPos, yPos, xRoom, yRoom)
			if x != xPos and x != xPos+xRoom-1 and y != yPos and y != yPos+yRoom-1:
				continue
			MapOfDun[x][y] = roomVal
	return newRoom
	
	
def digRoom(roomVal="*"):
	# stuff a random room in the map
	xRoom = random.randrange(3, int(round(xDun*roomMaxPercent))) 
	yRoom = random.randrange(3, int(round(yDun*roomMaxPercent))) 
	xPos = random.randrange(0, xDun-xRoom-1)
	yPos = random.randrange(0, yDun-yRoom-1)

	#pre dig check, check all spaces in and adjacent to ensure empty
	
	for x in range(xPos-1, xPos+xRoom+1):
		for y in range(yPos-1, yPos+yRoom+1):
			if MapOfDun[x][y] != '#':
				return None
	
	for x in range(xPos, xPos+xRoom):
		for y in range(yPos, yPos+yRoom):
			newRoom = Room(xPos, yPos, xRoom, yRoom)
			MapOfDun[x][y] = roomVal
			
			
	return newRoom

#Generate maximum map size

xDun = 30
yDun = 50
roomMaxPercent = .25
roomAttempts = 1000

MapOfDun = [['*' for x in range(yDun)] for x in range(xDun)]
roomList = []

for x in range(0, roomAttempts):
	r = erectRoom()
	if r is None:
		#do nothing
		1
	else:
		roomList.append(r)

print("Total Rooms: " + str(len(roomList))  + " (Of a total " + str(roomAttempts) + " attempts).")

printMap()


