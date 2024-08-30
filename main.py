from turtle import Screen

from paddle import Paddle

COLOR = "black"

sc = Screen()
sc.setup(width=1200, height=800)
sc.bgcolor(COLOR)
sc.tracer(0)
sc.listen()

game_is_over = False

left_paddle = Paddle((-560, 0))
right_paddle = Paddle((560, 0))

sc.onkeypress(left_paddle.move_up, "w")
sc.onkeypress(left_paddle.move_down, "s")

sc.onkeypress(right_paddle.move_up, "Up")
sc.onkeypress(right_paddle.move_down, "Down")

while not game_is_over:
	sc.update()

sc.exitonclick()
