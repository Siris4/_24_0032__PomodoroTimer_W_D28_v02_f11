from tkinter import *
import math

#Dr. Toma, the tomato:

# ---------------------------- CONSTANTS ------------------------------- #
#Colors (in Hex code):
#in layered order from outer-most to inner-most color layers: window background > canvas background >
PINK = "#ED7B7B"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#EBE76C"
ORANGE = "#F0B86E"
PURPLE = "#836096"

#Fonts:
FONT_NAME = "Courier"

#Integers (variable numbers):
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
work_timer_set_to_in_seconds = 11   # 3000 = 50 min, as default
reps = 0


#Strings:
checkmark_string = "✔"    #checkmark string version obtained from wikipedia:  https://en.wikipedia.org/wiki/Check_mark

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer_button():    # this function is responsible for calling that function 'timer_count_down', and we drop the 'start_timer_button' part behind the command= of the Start button code block
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        work_timer_count_down(work_timer_set_to_in_seconds)

    elif reps == 2 or reps == 4 or reps == 6 or reps == 8:
        (work_timer_count_down(work_timer_set_to_in_seconds * 2))

    # if it is the 2nd, 4th, 6th, and 8th rep:
    #you get a 20 min break


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  #either get ahold of the tkinter Module, then the Tk() Class, OR if using a lot of Classes (which we will be doing in this program), then we will just use the .Tk() Class from importing tkinter
#set the title of the window:
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)   #this ACTUALLY ADDS to the original width and height of the original 421x518 window. It won't take AWAY, or keep it the same size, it ADDS to the x and y lengths. So (padx=40, pady=40) would be a total window size of 461x558 pixels.  # https://colorhunt.co/palette/ebe76cf0b86eed7b7b836096 for bg=background_color_of_choice (without using "", because )

fg=GREEN #foreground

canvas = Canvas(width=430, height=496, bg=YELLOW, highlightthickness=0)  #variable canvas is created from the Canvas Widget  # width and height ar in pixel. # bg=background_color_for_canvas (not using "", since YELLOW is a variable name.  # highlightthickness=0 will get rid of the white line.

#Grid layout will be 3 columns wide and 5 rows down:

# Timer label:
label = Label(text="This is old text", fg=GREEN, bg=YELLOW, font=("Arial", 36, 'bold')) #color=GREEN
label.config(text="Timer")
label.grid(column=1, row=0)

#############

tomato_img = PhotoImage(file="tomato4.png") #Also add the image=(PhotoImage datatype Class of tkinter), in order to read through a file and get ahold of a photo at a certain location.  (use Absolute File path, if in another dir). #Also will need to provide a variable name to store this image to (not the Class, but a different variable name of choice, like 'tomato_img'.), then place it after the 'image=' part of the next line:
canvas.create_image(215, 248, image=tomato_img)  #add my image to it, x and y (which are implied, inside) is needed in the (). Because we want the image to be placed right in the center of the window, we divide the dimensions in half, for both, and place those numbers in the paren(). #Also add the image=(PhotoImage datatype Class of tkinter), in order to read through a file and get ahold of a photo at a certain location. Also add the variable after the 'image=' part.
timer_text = canvas.create_text(214, 305, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))   #this code line needs to be placed before/above we .pack() it. # the implied x and y value are the *args; text="text_here" is the keyword arguments (**kwargs)   #timer_text is the variable that we link once we get the function 'count_down' fixed
canvas.grid(column=1, row=1)   #to actually put it on the screen. Pack is okay for now, til we have to add more components. (changed to grid() )

#############

# Start Button:
button = Button(text="Start", font=20, highlightthickness=0, command=start_timer_button) #command=miles_to_kilometers #ONCE the button is actually pressed, then you run the calculation from the miles and it rewrites over the km quantity converted amount and places it OVER the 0 that was written at the col=1, row=1 that was at the original spot for the km_result_label
button.grid(column=0, row=2)   #the fix was to reduce the col from 2 to 1, and row from 3 to 2.

#############

# Reset Button:
button = Button(text="Reset", font=20, highlightthickness=0) #command=miles_to_kilometers #ONCE the button is actually pressed, then you run the calculation from the miles and it rewrites over the km quantity converted amount and places it OVER the 0 that was written at the col=1, row=1 that was at the original spot for the km_result_label
button.grid(column=2, row=2)   #the fix was to reduce the col from 2 to 1, and row from 3 to 2.

#############

# Timer label:
label = Label(text="This is old text", fg=GREEN, bg=YELLOW, font=("Arial", 24, 'bold')) #color=GREEN   #label is a kwarg (see all key-value pairs on this line)
label.config(text=checkmark_string)
label.grid(column=1, row=3)




# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def work_timer_count_down(count):
    # count = 5    # no need to put this var here, because we will be passing 5 as the argument later into the function call.
    countdown_in_mins = math.floor(count / 60)   #rounds down to whole number
    countdown_in_secs = count % 60   #remaining seconds after we cleanly divide it by 60
    if countdown_in_secs < 10:
        countdown_in_secs = f"0{countdown_in_secs}"

    canvas.itemconfig(timer_text, text=f"{countdown_in_mins}:{countdown_in_secs}")
    if count > 0:
        window.after(1000, work_timer_count_down, count - 1)   # count_down should NOT be count_down() here.




window.mainloop()
