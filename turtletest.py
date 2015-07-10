import turtle

def HelloWorld():	
	turtle.title("Hello World")
	turtle.setup(1000, 1000, 0, 0)
	turtle.penup()
	turtle.goto(0,0)
	
	turtle.color('navy')
	
	turtle.write("Hello World!", font = ('Times New Roman', 36, 'bold'))
	
	turtle.hideturtle()
	
	turtle.done()#Persist screen
	
def drawSquare(ttl, x, y, side):
	ttl.penup()
	ttl.goto(x, y)
	ttl.setheading(0)
	ttl.pendown()
	for iter in range(4):
		ttl.forward(side)
		ttl.right(90)
	ttl.penup()
	
def drawGrid(ttl):
	x = -400
	while(x < 400):
		drawSquare(ttl, x, 400, 50)
		x += 50
	
def main():
	turtle.title("Squares")
	
	turtle.setup(800, 800, 0, 0)
	
	ttl = turtle.Turtle()
	ttl.speed(0)
	
	
	ttl.color('red')
	drawGrid(ttl)
	
	#drawSquare(ttl, -50, -50, 50)
	#drawSquare(ttl, 0, 0, 50)
	#drawSquare(ttl, 50, 50, 50)
	#drawSquare(ttl, -50, 50, 150)
	
	#ttl.fillcolor('purple')
	#ttl.begin_fill()
	#drawSquare(ttl, 0, 0, 50)
	#ttl.end_fill()
	turtle.done()
	
main()