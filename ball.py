from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(x=self.xcor() + self.x, y=self.ycor() + self.y)

    def reset_position(self):
        self.goto(0, 0)
        self.x *= -1
        self.move()



