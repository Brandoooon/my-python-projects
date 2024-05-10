from turtle import Turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
TURNING_ANGLE = 90
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def create_snake(self):
        for position in STARTING_POSITION:
            block = Turtle(shape="square")
            block.penup()
            block.color("white")
            block.goto(position)
            self.snake.append(block)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def is_dead(self):
        is_dead = False
        if abs(self.head.xcor()) >= 310 or abs(self.head.ycor()) >= 310:
            is_dead = True
        for block in self.snake[1:]:
            if self.head.distance(block) < 15:
                is_dead = True
        return is_dead

    def grow(self):
        new_tail = Turtle(shape="square")
        new_tail.penup()
        new_tail.color("white")
        new_tail.goto(self.tail.position())
        self.snake.append(new_tail)

    def reset(self):
        for block in self.snake:
            block.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]