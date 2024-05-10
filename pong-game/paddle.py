from turtle import Turtle

LEFT_STARTING_POSITION = [(-490, 20), (-490, 0), (-490, -20)]
RIGHT_STARTING_POSITION = [(482, 20), (482, 0), (482, -20)]


class Paddle:

    def __init__(self, pos):
        self.paddle = []
        self.create_paddle(pos)
        self.head = self.paddle[0]
        self.tail = self.paddle[2]

    def create_paddle(self, pos):
        if pos == "left":
            for position in LEFT_STARTING_POSITION:
                block = Turtle(shape="square")
                block.penup()
                block.color("white")
                block.goto(position)
                self.paddle.append(block)
        elif pos == "right":
            for position in RIGHT_STARTING_POSITION:
                block = Turtle(shape="square")
                block.penup()
                block.color("white")
                block.goto(position)
                self.paddle.append(block)

    def up(self):
        if 300 - self.head.ycor() > 20:
            for i in range(len(self.paddle) - 1, -1, -1):
                self.paddle[i].sety(self.paddle[i].ycor() + 20)

    def down(self):
        if 300 + self.tail.ycor() > 20:
            for i in range(len(self.paddle) - 1, -1, -1):
                self.paddle[i].sety(self.paddle[i].ycor() - 20)
