from Tkinter import *
import random
import numpy as np
widthf=800
highf=400
global yspeed
y = 10


def drop():
    x = random.randint(20,800)
    y = 10
    r = 5
    cav.create_rectangle(x-r, y-r, x+r, y+r, outline='blue', fill='blue')

def fall():
    y = y + yspeed


fenetre= Tk()
fenetre.title ("goutte")

cav=Canvas(fenetre, width= widthf,height=highf, background='white')
cav.pack()

BoutonGo = Button(fenetre, text ='Go', command = drop)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)




fenetre.mainloop()
