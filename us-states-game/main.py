import turtle
import pandas

global answer_state

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)
turtle.penup()

pen = turtle.Turtle()
pen.ht()
pen.pencolor('black')
pen.penup()

scoreboard = turtle.Turtle()
scoreboard.ht()
scoreboard.pencolor('black')
scoreboard.penup()

states_data_frame = pandas.read_csv("50_states.csv")
all_states = states_data_frame.state.to_list()

completed_states = []


def update_score():
    scoreboard.clear()
    scoreboard.goto(240, 180)
    scoreboard.write(f'Score:{len(completed_states)}/50', align='center', font=('Arial', 32, 'normal'))


while len(completed_states) < 50:
    update_score()
    answer_state = screen.textinput(title="Guess the state", prompt="What is another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in completed_states]
        break
    match_state = states_data_frame[states_data_frame.state == answer_state]
    if not match_state.empty:
        completed_states.append(answer_state)
        x = match_state['x'].item()
        y = match_state['y'].item()
        pen.goto(x, y)
        pen.write(answer_state, align='center', font=('Arial', 8, 'normal'))

turtle.mainloop()
