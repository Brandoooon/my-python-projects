import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    if reps < 8:
        reps += 1
        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            title_label.config(text="Break", fg=RED)
        elif reps % 2 == 1:
            title_label.config(text="Work", fg=GREEN)
            count_down(WORK_MIN * 60)
        else:
            count_down(SHORT_BREAK_MIN * 60)
            title_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    check_mark = "✔"
    minute = "{:02}".format(count // 60)
    second = "{:02}".format(count % 60)
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(5, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += check_mark
        check_mark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
title_label = Label(text="Timer", font=(FONT_NAME, 48), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)
start_btn = Button(text="Start", relief=FLAT, command=start_timer)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", relief=FLAT, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark_label = Label(text="", font=(FONT_NAME, 16), fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

window.mainloop()
