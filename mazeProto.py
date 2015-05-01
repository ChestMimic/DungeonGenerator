import sys
import random
import subprocess as sp

from DrawMap import *
from Cell import Cell


sp.call('cls',shell=True)

class Cursor:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos
		

def printMap():
	sp.call('cls',shell=True)
	for y in range(0, yDun-1):
		for x in range(0, xDun-1):
			sys.stdout.write(str(MapOfDun[x][y]))
		sys.stdout.write("\n")
	return
	
def visit(cell):
	unvisitedCells.remove(cell)
	return cell
	
def breakWall(cellA, cellB):
	if cellA.xPos == cellB.xPos: #same E/W result
		if cellA.isNorthOf(cellB):
			cellA.south = True
			cellB.north = True
		else:
			cellA.north = True
			cellB.south = True	
	else:
		if cellA.isWestOf(cellB):
			cellA.east = True
			cellB.west = True
			
		else:
			cellA.west = True
			cellB.east = True
			
	if finalList.count(cellA) > 0:
		finalList.remove(cellA)
	finalList.append(cellA)
	
	if finalList.count(cellB) > 0:
		finalList.remove(cellB)
	finalList.append(cellB)
	
	
def digMaze(xDun, yDun):
	xStart = random.randrange(0, xDun-1)
	yStart = random.randrange(0, yDun-1)
	cur = Cell(xStart, yStart)
	visit(cur)
	
	while(len(unvisitedCells) > 0):
		#print("Test")
		#get current cell's unvisited neighbors
		neighbors = []
		#check left
		if cur.xPos-1 >= 0:
			#check visitation
			if Cell(cur.xPos-1, cur.yPos) in unvisitedCells:
				neighbors.append(Cell(cur.xPos-1, cur.yPos))
		
		if cur.xPos+1 < xDun:
		
			if Cell(cur.xPos+1, cur.yPos) in unvisitedCells:
				neighbors.append(Cell(cur.xPos+1, cur.yPos))
			

		if cur.yPos-1 >= 0:
			#check visitation
			
			if Cell(cur.xPos, cur.yPos-1) in unvisitedCells:
				neighbors.append(Cell(cur.xPos, cur.yPos-1))
			
		
		
		if cur.yPos+1 < yDun:
			#check visitation
			if Cell(cur.xPos, cur.yPos+1) in unvisitedCells:
				neighbors.append(Cell(cur.xPos, cur.yPos+1))
			
				
		if(len(neighbors) > 0):
			#pick random neighbor and assign to nxt
			nxt = random.choice(neighbors)
			#push cur to cellStack[]
			cellStack.append(cur)
			#remove wall between cur and nxt
			breakWall(cur, nxt)
			#make nxt cur, and visit()
			cur = nxt
			visit(cur)
		elif len(cellStack) > 0:
			#pop cell
			#make current
			cur = cellStack.pop()
		else:
			#pick random univisited cell, make cur and visit
			cur = random.choice(unvisitedCells)
			visit(cur)
		#printMap()
	
	return

xDun = 40
yDun = 20
roomMaxPercent = .25
roomAttempts = 1000
cellStack = []
unvisitedCells = []
finalList = []

MapOfDun = [[Cell(x, y) for y in range(yDun)] for x in range(xDun)]

print("Cells made")
		

for x in range(0, xDun):
	for y in range(0, yDun):
		unvisitedCells.append(Cell(x, y))
		
print("Total cells: " + str(len(unvisitedCells)) + "\n")
digMaze(xDun, yDun)

#printMap()
drawMapGR(finalList, xDun, yDun)