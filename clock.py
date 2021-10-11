from tkinter import Tk
from tkinter import Label
import time


root =Tk()
root.title("Clock")

def present_time():
    display_time = time.strftime("time in 24 hours\n%H:%M:%S %P")
    #display_time2 = time.strftime("%I:%M:%S %P")
    digi_clock.config(text=display_time)
    digi_clock.after(200,present_time)

digi_clock = Label(root, font=("arial",50),bg="black",fg="green")
digi_clock.pack()

present_time()
root.mainloop()