def draw_square(length):
	import turtle
	my_turtle = turtle.Turtle()
	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(90)
	
	return None

draw_square(100)
