# does the Florida map

import sys
sys.path.append('../')
from utils import *
from cmu_112_graphics import *


def map_appStarted(app):
    urlflorida = 'https://fvmstatic.s3.amazonaws.com/maps/m/US-FL-EPS-02-0001.png'
    app.imageflorida = loadImage(urlflorida)
    app.waterColor = "blue"

def map_keyPressed(app, event):
    if event.key == "Backspace":
        app.mode = 'introMode'

def map_mousePressed(app, event):
    x = event.x
    y = event.y
    if (x > app.width//5 and x < app.width//5 + 40 and y > app.height//5 and 
        y < app.height//5 + 40):
        app.color = "blue"
        app.mode = 'boat'
    if ((x > app.width*3//5-20 and x < app.width*3//5 + 40-20 and 
        y > app.height//2 and y < app.height//2 + 40)):
        app.color = "blue"
        app.mode = 'boat'
    if (app.width*8//10+20 and x < app.width*8//10 + 40+ 20 and 
        y > app.height*7//10 and y < app.height*7//10 + 40):
        app.color = "blue"
        app.mode = 'boat'
    if (x > app.width*7//10+10 and x < app.width*7//10 + 40 + 10 and 
        y > app.height//5 and y < app.height//5 + 40):
        app.color = "blue"
        app.mode = 'boat'
    if (x > app.width*8//10+5 and x < app.width*8//10 + 40+5 and 
        y > app.height//2 and y < app.height//2 + 40):
        app.color = "blue"
        app.mode = 'boat'

def map_redrawAll(app, canvas):
    canvas.create_image(400, 400, image=ImageTk.PhotoImage(
                        app.scaleImage(app.imageflorida, 3)))
    canvas.create_text(app.width//2, app.height//11, text = 'Pick a Port', 
                        font = 'Arial 50 bold')
    canvas.create_oval(app.width//5, app.height//5, app.width//5 + 40, 
                        app.height//5 + 40, fill = 'red')
    canvas.create_oval(app.width*3//5-20, app.height//2, app.width*3//5 + 40-20,
                       app.height//2 + 40, fill = 'red')
    canvas.create_oval(app.width*8//10+20, app.height*7//10, 
                       app.width*8//10 + 40+ 20, app.height*7//10 + 40, 
                       fill = 'red')
    canvas.create_oval(app.width*7//10+10, app.height//5, 
                       app.width*7//10 + 40 + 10, app.height//5 + 40, 
                       fill = 'red')
    canvas.create_oval(app.width*8//10+5, app.height//2, 
                       app.width*8//10 + 40+5, app.height//2 + 40, 
                       fill = 'red')
