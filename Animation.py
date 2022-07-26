from ctypes import resize
from email.mime import image
from tkinter import *
import time

Width = 900
Height = 900
xVelocity =4
yVelocity = 4
window = Tk()

canvas =Canvas(window,width=Width,height=Height)
canvas.pack()


photo=PhotoImage(file='me118.png')
my_image =canvas.create_image(0,0,image=photo,anchor=NW)

image_width = photo.width()
image_height = photo.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(Width-image_width) or coordinates[0]<0):
        xVelocity= -xVelocity
    if(coordinates[1]>=(Height-image_height) or coordinates[1]<0):
        yVelocity= -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()