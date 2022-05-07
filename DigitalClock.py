from tkinter import *
import time

root = Tk()
root.title('Digital Clock')
root.geometry('410x115')

def myTime():
    Clock = time.strftime("%I:%M:%S %p")
    Day = time.strftime("%A")
    myClock.config(text = Clock)
    myDay.config(text = Day)
    myClock.after(1000, myTime)

myClock = Label(root, text = '', font = ('Arial', 72), fg = 'white', bg = 'black')
myClock.pack()
myDay = Label(root, text = "", font = ('Arial', 24))
myDay.pack()

myTime()

root.mainloop()