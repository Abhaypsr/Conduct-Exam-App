#import time
#
#print(time.localtime()[0])
#print(time.localtime()[1])
#print(time.localtime()[2])

#import pygame
#
#
from tkinter import *
win=Tk()
win.geometry("1300x700")
def action(n):
    print(n)
f=Frame(win,width=800,height=500)
f.place(x=300,y=100)
f.pack_propagate(False)
s=Scrollbar(f)
s.pack(side=RIGHT,fill=Y)
listbox = Listbox(f)
for i in range(100):
#    listbox.insert(END,"      ")
    listbox.insert(i,b1)
#    listbox.insert(END,"      ")
listbox.pack(side=LEFT)
listbox.pack_propagate(False)
#s.config(command=listbox.yview)
#n=10
#Button(win,text="click",command= lambda: action(10)).pack()
win.mainloop()
