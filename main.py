

from score import ScoreBoard
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
p1 = Paddle(350, 0)
p2 = Paddle(-360, 0)
b = Ball()
sc = ScoreBoard()
screen.listen()
# to move up right paddle press UP arrow key
# to move down right paddle press down arrow key
# to move up left paddle press W arrow key
# to move down left paddle press S arrow key
screen.onkey(fun=p1.move_up, key="Up")
screen.onkey(fun=p1.move_down, key="Down")
screen.onkey(fun=p2.move_up, key="w")
screen.onkey(fun=p2.move_down, key="s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    b.move()

    # bounce at boundary
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()

    # bounce at horizontal boundary
    if b.distance(p1) < 30 and b.xcor() > 320 or b.distance(p2) < 30 and b.xcor() < -320:
        b.bounce_x()

    # reset ball after passing vertical boundary
    if b.xcor() > 380:
        b.reset_position()
        sc.update_score1()

    # reset ball after passing vertical boundary
    if b.xcor() < -380:
        b.reset_position()
        sc.update_score2()

screen.exitonclick()
