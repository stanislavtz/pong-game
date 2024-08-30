from turtle import Turtle

SHAPE = "circle"
COLOR = "white"


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape(SHAPE)
		self.color(COLOR)
		self.penup()

	def move(self):
		new_xcor = self.xcor() + 10
		new_ycor = self.ycor() + 10
		self.goto(new_xcor, new_ycor)