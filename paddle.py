from turtle import Turtle

COLOR = "white"
SHAPE = "square"


class Paddle(Turtle):
	def __init__(self, position):
		super().__init__()
		self.color(COLOR)
		self.shape(SHAPE)
		self.penup()
		self.shapesize(stretch_wid=6, stretch_len=1)
		self.goto(position)

	def move_up(self):
		y_cor = self.ycor() + 20
		self.goto(self.xcor(), y_cor)

	def move_down(self):
		y_cor = self.ycor() - 20
		self.goto(self.xcor(), y_cor)