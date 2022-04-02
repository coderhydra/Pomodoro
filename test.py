from tkinter import *
import time

def nowdate():
    now = time.localtime()
    return now.tm_year,"/",now.tm_mon,"/",now.tm_mday
def nowtime():
    now = time.localtime()
    return now.tm_hour,":",now.tm_min,":",now.tm_sec

root = Tk()
label = Label(root, text=nowdate())
label.pack()
label = Label(root, text=nowtime())
label.pack()

root.mainloop()