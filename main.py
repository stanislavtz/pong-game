from turtle import Screen

import time

from paddle import Paddle
from ball import Ball

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

	# Define collision with paddle
	if ball.distance(left_paddle) < 30 or ball.distance(right_paddle) < 30:
		ball.bounce_from_paddle()
		speed *= 0.9

	# Define scoring and ball reset position
	if ball.xcor() < -600 or ball.xcor() > 600:
		ball.reset()
		speed = 0.075


sc.exitonclick()
