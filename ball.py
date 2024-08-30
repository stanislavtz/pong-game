from turtle import Turtle

SHAPE = "circle"
COLOR = "white"


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape(SHAPE)
		self.color(COLOR)
		self.penup()