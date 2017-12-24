#!/usr/bin/python
from Tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 800
r = random.uniform(0.5,1.5)
x = random.randint(0,800)
y = random.randint(-200,200)


tk = Tk() #Create the window
tk.title("rain") #Title
canvas = Canvas(tk, width = WIDTH, height =HEIGHT, bg ='white') #Create the window with the background
canvas.pack() #DUNNOW



class drop: #Class def
    def __init__ (self):        #Define object
        x = random.randint(0,800)
        y = random.randint(-200,200)
        r = random.uniform(0.5,2.0)

        self.shape = canvas.create_rectangle(x-r, y-3*r, x+r, y+3*r, outline='purple', fill='purple') #create canvasn rectangle
        self.yspeed = random.randint(20,60)          #speed x
        self.xspeed = random.randint(-50,50)        #speed y

    def move(self):     #Define moving function
        canvas.move(self.shape,0,self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[1] >= HEIGHT:    #If drops reach the bottom of the screen create new particle at the top
            x = random.randint(0,800)
            y = random.randint(-200,200)
            r = random.uniform(0.5,2.0)
            self.shape = canvas.create_rectangle(x-r, y-3*r, x+r, y+3*r, outline='purple', fill='purple') #Shouldn't have to write this agains


drops = [] #Empty list of drops
for i in range(300):
    drops.append(drop()) #Add drops in the drop list


while True:
    for drop in drops:
        drop.move() #Print 
    tk.update() #Refresh the window
    time.sleep(0.05) # 20images per second

tk.mainloop()
