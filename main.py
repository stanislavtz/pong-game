from turtle import Screen

import time

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

COLOR = "black"

sc = Screen()
sc.setup(width=1200, height=800)
sc.bgcolor(COLOR)
sc.tracer(0)
sc.listen()

game_is_over = False

left_paddle = Paddle((-560, 0))
right_paddle = Paddle((560, 0))

ball = Ball()

score_board = ScoreBoard()

sc.onkeypress(left_paddle.move_up, "w")
sc.onkeypress(left_paddle.move_down, "s")

sc.onkeypress(right_paddle.move_up, "Up")
sc.onkeypress(right_paddle.move_down, "Down")

speed = 0.075

while not game_is_over:
	sc.update()
	time.sleep(speed)
	ball.move()

	# Define collision with wall
	if ball.ycor() == 380 or ball.ycor() == -380:
		ball.bounce_from_wall()

	# Define collision with left paddle
	if ball.distance(left_paddle) < 30 or ball.distance(right_paddle) < 30:
		ball.bounce_from_paddle()
		speed *= 0.9

	# Define right paddle scoring and ball reset position
	if ball.xcor() < -600:
		ball.reset()
		score_board.increase_right_scores()
		speed = 0.075

	# Define left paddle scoring and ball reset position
	if ball.xcor() > 600:
		ball.reset()
		score_board.increase_left_scores()
		speed = 0.075

	# Define winner
	if score_board.winner():
		game_is_over = True


sc.exitonclick()
