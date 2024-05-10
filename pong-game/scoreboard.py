from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 32, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        self.score_left = 0
        self.score_right = 0
        super().__init__()
        self.penup()
        self.color("white")
        self.sety(250)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_left}     {self.score_right}", align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
