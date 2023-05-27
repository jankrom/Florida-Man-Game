# splash Screen

import sys
sys.path.append('../')
from utils import *
from cmu_112_graphics import *

def introMode_appStarted(app):
    app.playx0 = app.width//20
    app.playy0 = app.height*4//10
    app.playx1 = app.width//2
    app.playy1 = app.height*6//10
    urlSplashScreen = 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2020/09/931/524/fisherman-istock.jpg?ve=1&tl=1'
    app.imageSplashScreen = loadImage(urlSplashScreen)

def introMode_mousePressed(app, event):
    x = event.x
    y = event.y
    if x >= app.playx0 and x <= app.playx1 and y >= app.playy0 and y <= app.playy1:
        app.mode = 'map'
    if x >= app.width//20 and x <= app.width//2 and y >= app.height*7//10 and y <= app.height*9//10:
        app.mode = "eduIntroMode"

def introMode_redrawAll(app, canvas):
    canvas.create_image(app.width//6, app.height//2, image=ImageTk.PhotoImage(
                        scaleImage(app.imageSplashScreen, 1.5)))
    canvas.create_text(app.width//3, app.height//4, fill = "black", 
                        text = 'The Florida Man', font = 'Arial 50 bold')
    canvas.create_rectangle(app.playx0, app.playy0, app.playx1, app.playy1, 
                            fill = 'light blue')
    canvas.create_text((app.playx0+app.playx1)//2, (app.playy0+app.playy1)//2,
                        text = 'PLAY', fill = "black", font = 'Arial 50 bold')
    canvas.create_rectangle(app.width//20, app.height*7//10, app.width//2,
                            app.height*9//10, fill = 'light blue')
    canvas.create_text((app.width//20 + app.width//2)//2, 
                        (app.height*7//10 + app.height*9//10)//2, 
                        text = 'HELP', fill = 'black', font = 'Arial 50 bold')