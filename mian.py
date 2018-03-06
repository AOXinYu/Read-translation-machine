#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  Tkinter as tk
import  readCopy
import  testtestGoogletrans
old_text = ''
new_text = 'hi'
engine = readCopy.speakInit()
def update_timeText():
    global  old_text
    global  new_text
    new_text = readCopy.getCopyText()
    print (new_text+ '+')
    print  (old_text+'-')
    if (new_text != old_text):
        try:
            words = new_text
            result = testtestGoogletrans.translate(words)
            Label2.configure(text=result)
            Label2.pack
            old_text =new_text
            window.after(1000, update_timeText)
            return   read_text()
        except:
            window.after(1000, update_timeText)
    else:
        window.after(1000, update_timeText)

def read_text():
    global  engine
    engine.say(new_text)
    engine.runAndWait()
def init():
    window = tk.Tk()
    Button1=tk.Button(window, text='再次朗读',  command=lambda:read_text())
    Button1.place(x=350,y=20)
    window.title('daydayup点读机')
    window.geometry('400x200')
    Label1=tk.Label(window,text='结果')
    Label1.place(x=10,y=10)
    Label2=tk.Label(window,text='*******', font = ("Arial, 14"),wraplength=300)
    Label2.place(x=20,y=40)
    return  Label2 ,window
if __name__ == "__main__":
    Label2,window=init()
    engine = readCopy.speakInit()
    new_text =  readCopy.getCopyText()
    try:
        words = new_text
        result=testtestGoogletrans.translate(words)
        Label2.configure(text=result)
        Label2.place(x=20, y=40)
        Label2.pack()
        update_timeText()
        window.wm_attributes('-topmost', 1)
        window.mainloop()
    except:
        pass

