from graphics import *


def drawMapGR(CellList, xCount, yCount):
	scale = 15
	win = GraphWin("Maze", (yCount)*scale, (xCount)*scale) #Y then X
	
		
	for x in CellList:
		print("X/Y: " + str(x.xPos) + " " + str(x.yPos))
		
		tl = Point(x.yPos*scale, x.xPos*scale)
		br = Point(x.yPos*scale+scale, x.xPos*scale+scale )
		rect = Rectangle(tl, br)
		rect.setFill("white")
		rect.setOutline("white")
		rect.draw(win)
		
	for x in CellList:
		if not x.north:
			l = Point(x.yPos*scale, x.xPos*scale)
			r = Point(x.yPos*scale, x.xPos*scale+scale)
			ln = Line(l, r)
			ln.setOutline("red")
			ln.draw(win)
			
		if not x.south:
			l = Point(x.yPos*scale+scale, x.xPos*scale)
			r = Point(x.yPos*scale+scale, x.xPos*scale+scale)
			ln = Line(l, r)
			ln.setOutline("red")
			ln.draw(win)
		
		if not x.east:
			l = Point(x.yPos*scale, x.xPos*scale)
			r = Point(x.yPos*scale+scale, x.xPos*scale)
			ln = Line(l, r)
			ln.setOutline("red")
			ln.draw(win)
			
		if not x.west:
			l = Point(x.yPos*scale, x.xPos*scale+scale)
			r = Point(x.yPos*scale+scale, x.xPos*scale+scale)
			ln = Line(l, r)
			ln.setOutline("red")
			ln.draw(win)
		
	win.getMouse()
	win.close()
	

	

	
if __name__ == "__main__":
	drawMapGR(None, 500, 300)