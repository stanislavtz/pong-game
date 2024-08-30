from turtle import Screen

COLOR = "black"

sc = Screen()
sc.setup(width=1200, height=800)
sc.bgcolor(COLOR)
sc.tracer(0)
sc.listen()

game_is_over = False


while not game_is_over:
	sc.update()

sc.exitonclick()
