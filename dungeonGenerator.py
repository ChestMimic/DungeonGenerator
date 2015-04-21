import sys	#for newline free print
import random 	#pseudorng access
import math

def printMap():
	for x in range(0, xDun):
		for y in range(0, yDun):
			sys.stdout.write(str(MapOfDun[x][y]))
		sys.stdout.write("\n")
	return
	
def digRoom(roomVal="*"):
	# stuff a random room in the map
	xRoom = random.randrange(2, int(round(xDun*roomMaxPercent))) 
	yRoom = random.randrange(2, int(round(yDun*roomMaxPercent))) 
	xPos = random.randrange(0, xDun-xRoom-1)
	yPos = random.randrange(0, yDun-yRoom-1)

	#pre dig check, check all spaces in and adjacent to ensure empty
	
	for x in range(xPos-1, xPos+xRoom+1):
		for y in range(yPos-1, yPos+yRoom+1):
			if MapOfDun[x][y] != '#':
				return
	
	for x in range(xPos, xPos+xRoom):
		for y in range(yPos, yPos+yRoom):
			MapOfDun[x][y] = roomVal
	return

#Generate maximum map size

xDun = 30
yDun = 50
roomMaxPercent = .25
roomAttempts = 100

MapOfDun = [['#' for x in range(yDun)] for x in range(xDun)]

for x in range(0, roomAttempts):
	digRoom()


printMap()


