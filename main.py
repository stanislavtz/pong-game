import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
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

while not game_is_over:
	sc.update()
	time.sleep(ball.move_speed)
	ball.move()

	# Define collision with wall
	if ball.ycor() == 380 or ball.ycor() == -380:
		ball.bounce_from_wall()

	# Define collision with paddles
	if ((ball.distance(left_paddle) < 60 and ball.xcor() < -530) or (
			ball.distance(right_paddle) < 60 and ball.xcor() > 530)):
		ball.bounce_from_paddle()

	# Define right paddle scoring and ball reset position
	if ball.xcor() < -560:
		ball.reset()
		score_board.increase_right_score()

	# Define left paddle scoring and ball reset position
	if ball.xcor() > 560:
		ball.reset()
		score_board.increase_left_score()

	# Define winner
	if score_board.winner():
		game_is_over = True

sc.exitonclick()
