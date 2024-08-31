from tkinter import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
countdown = 1500
start = True


# ---------------------------- TIMER RESET ------------------------------- #

def click_reset():
    global start
    start = False
    do.config(text="Timer")
    canvas.itemconfig(timer, text="25:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
pomo = 3


def timing(count=1500):
    global pomo, start
    if start:
        if pomo % 2 == 1:
            do.config(text="Work")
        if pomo == 1:
            count = WORK_MIN * 60
            pomo = 3
        if count == 0:
            canvas.itemconfig(timer, text="0:00")
            messagebox.showinfo(title="", message="Time is up!")
            pomo += 1
            if pomo % 8 == 2:
                count = LONG_BREAK_MIN * 60
                do.config(text="Break")
            elif pomo % 2 == 1:
                count = WORK_MIN * 60
                do.config(text="Work")
            elif pomo % 2 == 0:
                count = SHORT_BREAK_MIN * 60
                do.config(text="Break")
        sec = count % 60
        minute = int((count - sec) / 60)
        if sec < 10:
            sec = f"0{sec}"
        if count > 0:
            canvas.itemconfig(timer, text=f"{minute}:{sec}")
            window.after(1000, timing, count - 1)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def click_start():
    global start
    start = True
    timing()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=400, height=400)
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

do = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
do.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 112, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=click_start, bg=GREEN)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", command=click_reset, bg=GREEN)
reset_button.grid(row=2, column=2)

window.mainloop()
