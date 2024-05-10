from turtle import Turtle
import random


MOVING_DIRECTION = [[20, 20], [20, -20], [-20, 20], [-20, -20]]



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.moving_path = random.choice(MOVING_DIRECTION)

    def hit_horizontal_boarder(self):
        if 300 - self.ycor() < 20 or self.ycor() + 300 < 20:
            return True
        return False

    def move(self):
        self.goto(self.xcor() + self.moving_path[0], self.ycor() + self.moving_path[1])
        if self.hit_horizontal_boarder():
            self.bounce_y()

    def bounce_y(self):
        self.moving_path[1] = 0 - self.moving_path[1]

    def bounce_x(self):
        self.moving_path[0] = 0 - self.moving_path[0]
