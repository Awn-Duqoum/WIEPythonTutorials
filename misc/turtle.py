import turtle
#turtle.pen()

x=50

color = ("red","blue","green", "teal","orange","hot pink")

turtle.width(4)
turtle.speed(10)

for counter in range(100):
	turtle.color(color[counter%len(color)])
	turtle.forward(x)
	turtle.right(80)
	
	x = x+5