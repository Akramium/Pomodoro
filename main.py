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


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(20)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# title
title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title.grid(row=0, column=1)

# tomato + timer photo
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# button start
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(row=2, column=0)

# button reset
reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(row=2, column=2)

# checkmarks
checkmarks = Label(text="✔", fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)

window.mainloop()
