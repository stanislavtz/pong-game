from turtle import Turtle

SHAPE = "circle"
COLOR = "white"


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape(SHAPE)
		self.color(COLOR)
		self.penup()
		self.x_step = 10
		self.y_step = 10

	def move(self):
		new_xcor = self.xcor() + self.x_step
		new_ycor = self.ycor() + self.y_step
		self.goto(new_xcor, new_ycor)

	def bounce_from_wall(self):
		self.y_step *= -1

	def bounce_from_paddle(self):
		self.x_step *= -1

	def reset(self):
		self.goto(0, 0)
		self.x_step *= -1