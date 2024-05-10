from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


def init_net():
    net = Turtle()
    net.ht()
    net.speed("fastest")
    net.goto(0, 300)
    net.setheading(270)
    net.pencolor("white")
    while net.ycor() > -300:
        net.forward(10)
        net.penup()
        net.forward(10)
        net.pendown()


init_net()
ball = Ball()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')


def hit_left(ball, left_paddle):
    for block in left_paddle.paddle:
        if ball.distance(block) < 15:
            return True
    return False

def hit_right(ball, right_paddle):
    for block in right_paddle.paddle:
        if ball.distance(block) < 15:
            return True
    return False


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if hit_left(ball, left_paddle):
        scoreboard.increase_score_left()
        ball.bounce_x()
    elif hit_right(ball, right_paddle):
        scoreboard.increase_score_right()
        ball.bounce_x()

    if abs(ball.xcor()) > 520:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
