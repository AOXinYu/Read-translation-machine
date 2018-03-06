#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk
import time
import time
from googletrans import Translator
import  readCopy
import  testtestGoogletrans

def update_timeText():
#Get the current time, note you can change the format as you wish

    current = time.strftime("%H:%M:%S")
    print ('1')

# Update the timeText Label box with the current time
    timeText.configure(text=current)

# Call the update_timeText() function after 1 second
    window.after(1000, update_timeText)



window = tk.Tk()

window.wm_title("Simple Clock Example")


# Create a timeText Label (a text box)
timeText = tk.Label(window, text="", font=("Helvetica", 150))
timeText.pack()
update_timeText()
window.mainloop()