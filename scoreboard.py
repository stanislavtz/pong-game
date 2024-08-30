from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
SCORES_FONT = ("Courier", 56, "bold")
WINNER_FONT = ("Courier", 36, "bold")

WINNING_SCORES = 3


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.left_scores = 0
		self.right_scores = 0

		self.color(COLOR)
		self.penup()
		self.goto(0, 300)
		self.hideturtle()
		self.display_result()

	def display_result(self):
		self.clear()
		self.write(f"{self.left_scores} : {self.right_scores}", align=ALIGNMENT, font=SCORES_FONT)

	def increase_right_scores(self):
		self.right_scores += 1
		self.display_result()

	def increase_left_scores(self):
		self.left_scores += 1
		self.display_result()

	def display_winner(self, player):
		self.goto(0, 0)
		self.write(f"The WINNER is {player}", align=ALIGNMENT, font=WINNER_FONT)

	def winner(self):
		if self.left_scores == WINNING_SCORES:
			self.display_winner("LEFT PLAYER")
		elif self.right_scores == WINNING_SCORES:
			self.display_winner("RIGHT PLAYER")
		else:
			return False
		return True
