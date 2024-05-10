import random
from turtle import Turtle, Screen

screen = Screen()
screen_width = 500
screen_height = 400
screen.setup(width=screen_width, height=screen_height)


colors = ["black", "red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle(color):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    return turtle


def init_race(turtles, x, y, gap):
    for i in range(len(turtles)):
        if i % 2 == 1:
            y = gap * (i // 2 + 1)
        else:
            y = gap * i // -2
        turtles[i].goto(x=x, y=y)

turtles = []
for i in range(0, len(colors)):
    turtles.append(create_turtle(colors[i]))
init_race(turtles, -240, 0, int((screen_height - 100) / len(colors)))

is_race_on = False

brandon = screen.textinput(title="Make Brandon's bet", prompt="Which turtle win the race? Enter a color")
june = screen.textinput(title="Make June's bet", prompt="Which turtle win the race? Enter a color")
if brandon and june:
    is_race_on = True


def check_bet(brandon, june, winner):
    if brandon == winner:
        print(f"Brandon wins!")
    elif june == winner:
        print(f"June wins!")
    else:
        print("Both lose!")
    print(f"The winner is {winner} turtle.")


while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 240:
            is_race_on = False
            winner = turtle.color()[1]
            check_bet(brandon, june, winner)
            break


screen.exitonclick()
