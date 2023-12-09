# from tkinter import *
import tkinter as tk
import ttkbootstrap as tb

win = tb.Window(themename="darkly")
win.title("Artin Text To Voice")
win.minsize(700,450)

def click():
    red_color, green_color, blue_color = red["amountused"], green["amountused"], blue["amountused"]
    rgb = (red_color, green_color, blue_color)
    
    color_frm.configure(bg="#%02x%02x%02x" % rgb )

frm = tb.Frame(win,)
frm.pack(pady=(40,0))
red = tb.Meter(frm, bootstyle="info", subtext="red", interactive=True, metersize=140, amounttotal=255)
red.grid(row=0, column=0, padx=10)
green = tb.Meter(frm, bootstyle="info", subtext="green", interactive=True, metersize=140, amounttotal=255,)
green.grid(row=0, column=1, padx=10)
blue = tb.Meter(frm, bootstyle="info", subtext="blue", interactive=True, metersize=140, amounttotal=255,)
blue.grid(row=0, column=2, padx=10)

btn = tb.Button(win,text="set color", bootstyle="success-outline", width=10, command=click)
btn.pack(pady=(30,0))

color_frm = tk.Frame(win, width=300, height=100, bg="white",)
color_frm.pack(pady=(30,0))


win.mainloop()