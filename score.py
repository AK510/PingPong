from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.goto(0, 230)
        self.color("white")
        self.write(f"{self.score1} {self.score2}", False, align="center", font=("Arial", 50, "normal"))

    # update score
    def update_score1(self):
        self.clear()
        self.score1 += 1
        self.write(f"{self.score1} {self.score2}", False, align="center", font=("Arial", 50, "normal"))

    # update score
    def update_score2(self):
        self.clear()
        self.score2 += 1
        self.write(f"{self.score1} {self.score2}", False, align="center", font=("Arial", 50, "normal"))
