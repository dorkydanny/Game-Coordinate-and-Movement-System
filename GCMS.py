#imports
#----------------------------------------------------------------
import tkinter as tk # tkinter modules
from tkinter import *
#code 
#----------------------------------------------------------------
win = tk.Tk()
canv = Canvas(win,height=200,width=200,bg="#fff")
canv.grid()

def upx():
    canv.move('square', 1, 0)
def upy():
    canv.move('square', 0, -1)   
def downx():
    canv.move('square', -1, 0)   
def downy():
    canv.move('square', 0, 1)

btn = tk.Button(win,text = '>', command = upx)
btn2 = tk.Button(win,text = '<', command = downx)
btn3 = tk.Button(win,text = '^', command = upy)
btn4 = tk.Button(win,text = 'v', command = downy)

btn.place(x=30,y=30)
btn2.place(x=10,y=30)
btn3.place(x=20,y=3)
btn4.place(x=20,y=57)

canv.create_rectangle(60, 60, 120, 120, tags=('square'))

win.mainloop()




    
    
  
