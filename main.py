from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break =  LONG_BREAK_MIN*60
    if reps%8 == 0:
        timer_label.config(text="Long break", fg=RED)
        count_down(long_break)
    elif reps%2==0 :
        timer_label.config(text="Short break",  fg=YELLOW)
        count_down(short_break)
    else:
        timer_label.config(text="Work",  fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec= count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✓"
        checkmark_label.config(text=mark)
# ---------------------------- UI SETUP -------------------------------

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER RESET ------------------------------- #
window = Tk()
window.title("Promodoro")
tomato_image=PhotoImage(file='tomato.png')
window.config(pady=50, padx=100, bg=PINK)

timer_label = Label(text="Timer", fg=GREEN, bg= PINK, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=223, bg=PINK, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 122, text="00:00", fill="white", font=(FONT_NAME,25, 'bold'))

start_button = Button(text="Start", fg="black", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


checkmark_label = Label(text="", bg=PINK,  fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()