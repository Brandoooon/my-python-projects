import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.is_dead():
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
    if snake.head.distance(food) <= 20:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

screen.exitonclick()
