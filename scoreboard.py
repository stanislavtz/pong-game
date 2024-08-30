from turtle import Turtle

COLOR = "white"
ALIGNMENT = "center"
SCORES_FONT = ("Courier", 56, "bold")
WINNER_FONT = ("Courier", 30, "bold")
WINNING_SCORES = 10


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.left_score = 0
		self.right_score = 0

		self.color(COLOR)
		self.penup()
		self.goto(0, 300)
		self.hideturtle()
		self.display_result()

	def display_result(self):
		self.clear()
		self.write(f"{self.left_score} : {self.right_score}", align=ALIGNMENT, font=SCORES_FONT)

	def increase_right_score(self):
		self.right_score += 1
		self.display_result()

	def increase_left_score(self):
		self.left_score += 1
		self.display_result()

	def display_winner(self, player):
		self.goto(0, 0)
		self.write(f"The WINNER is: {player}", align=ALIGNMENT, font=WINNER_FONT)

	def winner(self):
		if self.left_score == WINNING_SCORES:
			self.display_winner("LEFT PLAYER")
		elif self.right_score == WINNING_SCORES:
			self.display_winner("RIGHT PLAYER")
		else:
			return False
		return True
