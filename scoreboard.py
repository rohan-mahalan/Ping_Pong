from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score()

    def score(self):
        self.goto(-200, 220)
        self.write(self.l_score, align='left', font=('Arial', 25, 'normal'))
        self.goto(200, 220)
        self.write(self.r_score, align='left', font=('Arial', 25, 'normal'))

    def left_score(self):
        self.clear()
        self.l_score += 1
        self.score()

    def right_score(self):
        self.clear()
        self.r_score += 1
        self.score()