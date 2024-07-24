from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, X, Y):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(X, Y)

    def up(self):
        if self.ycor() < 260:
            self.forward(10)

    def down(self):
        if self.ycor() > -260:
            self.back(10)

