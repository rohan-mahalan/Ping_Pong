from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# to increase the speed of the ball with every score
Ball_speed = 0.1

screen = Screen()
screen.tracer(0)
screen.title('Ping Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')

Score = ScoreBoard()
left_paddle = Paddle(-380, 0)
right_paddle = Paddle(370, 0)
BALL = Ball()

game_is_on = True

screen.listen()
screen.onkeypress(key='w', fun=left_paddle.up)
screen.onkeypress(key='s', fun=left_paddle.down)
screen.onkeypress(key='Up', fun=right_paddle.up)
screen.onkeypress(key='Down', fun=right_paddle.down)

while game_is_on:
    time.sleep(Ball_speed)
    screen.update()
    BALL.move()
    # bouncing back from top wall
    if BALL.ycor() > 280:
        BALL.y *= -1

    if BALL.distance(right_paddle) < 50 and BALL.xcor() > 340:
        BALL.x *= -1
    # bouncing from bottom wall
    if BALL.ycor() < -270:
        BALL.y *= -1

    if BALL.distance(left_paddle) < 50 and BALL.xcor() < -350:
        BALL.x *= -1

    if BALL.xcor() < -410:
        BALL.reset_position()
        Score.right_score()
        Ball_speed *= 0.9

    if BALL.xcor() > 410:
        BALL.reset_position()
        Score.left_score()
        Ball_speed *= 0.9


screen.exitonclick()
