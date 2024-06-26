from tkinter import *
import calendar
from datetime import datetime

win = Tk()
win.title("GUI Calendar")

def show_calendar():
    year_str = year_spinbox.get()
    month_str = month_spinbox.get()
    
    year_int = int(year_str)
    month_int = int(month_str)
    
    cal = calendar.month(year_int, month_int)
    
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)

today = datetime.now()
default_year = today.year
default_month = today.month

Label(win, text="Year").grid(row=0, column=0)
Label(win, text="Month").grid(row=0, column=1)

year_spinbox = Spinbox(win, from_=1947, to=2150, width=24)
year_spinbox.grid(row=1, column=0, padx=16)
year_spinbox.delete(0, END)
year_spinbox.insert(0, default_year)

month_spinbox = Spinbox(win, from_=1, to=12, width=3)
month_spinbox.grid(row=1, column=1)
month_spinbox.delete(0, END)
month_spinbox.insert(0, default_month)

Button(win, text="GO", command=show_calendar).grid(row=1, column=2)

textfield = Text(win, height=10, width=30, foreground='brown')
textfield.grid(row=3, columnspan=3)

win.mainloop()