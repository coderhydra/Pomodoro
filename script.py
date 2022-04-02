from tkinter import Label, Tk
import time
import sound
# 창디자인
app_window = Tk()
app_window.title("My Digital Time")
app_window.geometry("350x150")
app_window.resizable(0,0)
# 라벨디자인
text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25
# 라벨
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
# 디지털 시계 기능
def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()