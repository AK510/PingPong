from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setx(xcor)
        self.sety(ycor)
        self.color("white")
        self.setheading(90)

    # move paddle up by 20
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # move paddle down by 20
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
