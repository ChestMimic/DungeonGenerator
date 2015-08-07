import random
import math

from DungeonGenerator import Grid as DGGrid
from DungeonGenerator import Room as DGRoom

class Cartographer:
	def __init__(self): #Default map
		self.mp = DGGrid.Grid(50, 50)
		self.roomPerc = 0.25	#Maximum width/height of Map that room can occupy
		self.roomAtt = 1000		#Maximum number of attempts to place rooms
		self.roomList = []

	def labyrinthStartup(self, xBound, yBound, roomMaxFreq, roomAttempts):
		pass
	
	def genRandomRoom(self):
			xLim = self.mp.xBound
			yLim = self.mp.yBound
			szLim = self.roomPerc
			
			xRm = random.randint(0, xLim)
			yRm = random.randint(0, yLim)
			xSz = random.randint(0, int(round(xLim*szLim)))
			ySz = random.randint(0, int(round(yLim*szLim)))
			return DGRoom.Room(xRm, yRm, xSz, ySz)
	
	def addRooms(self):
		attemptsRemaining = self.roomAtt

		while attemptsRemaining > 0:
			attemptsRemaining -= 1
			rm = self.genRandomRoom()
			if rm.isRoomValid():
				if self.roomList:
					flag = 0
					for r in self.roomList:
						if r.roomsOverlap(rm):
							flag += 1
					if flag == 0:
						self.roomList.append(rm)
				else:
					self.roomList.append(rm)
		

	

	def addMaze(self):
		pass
	



if __name__ == "__main__":
	lab = Cartographer()
	lab.mp.printMap()

	room1 = DGRoom.Room(0, 0, 10,10)
	room2 = DGRoom.Room(50, 50, 5, 5)
	if room1.roomsOverlap(room2):
		print("Rooms overlap")
	lab.addRooms()
	print("Added " + str(len(lab.roomList)) + " rooms")