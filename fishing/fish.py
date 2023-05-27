import sys

sys.path.append('../')

from cmu_112_graphics import *
from dataclasses import make_dataclass
import random

Fish = make_dataclass('Fish', ['x', 'y', 'dir', 'speed', 'type', 'hooked'])
Gator = make_dataclass('Gator', ['x', 'y', 'dir','hooked'])

def fish_appStarted(app):
    app.xHook = app.width/2
    app.yHook = app.height * 0.23
    # grey yellow : 1, orange, brown: -2, green: 3
    app.types = ['green', 'brown', 'orange', 'yellow', 'grey']
    app.fishes = []
    app.gators = []
    app.timerCount = 0
    app.hookFull = False
    app.score = 0
    app.timerDelay = 50
    app.waterColor = 'dark blue'
    app.gameOver = False
    app.gameOverCounter = 0

def fish_keyPressed(app, event):
    if event.key == 'r':
        fish_appStarted(app)
        app.mode = "boat"
    if event.key == "h":
        app.mode = "helpMode"
    if not app.gameOver:
        if event.key == 'Up':
            if app.yHook >= app.height * 0.23:
                app.yHook -= 20
        elif event.key == 'Down':
            if app.yHook < app.height:
                app.yHook += 20
        if app.hookFull != False:
            if app.yHook < app.height * 0.35:
                if app.hookFull == 'grey' or app.hookFull == 'yellow':                    
                    app.score += 1
                elif app.hookFull == 'orange' or app.hookFull == 'brown':
                    app.score -= 2
                elif app.hookFull == 'green':
                    app.score += 3
                app.hookFull = False


def drawHook(app, canvas):
    x1 = app.xHook
    y1 = app.yHook
    y2 = app.yHook + app.height/35
    x2 = app.xHook - app.width/100
    canvas.create_line(app.width/2, app.height * 0.23, x1, y1)
    canvas.create_line(x1,y1,x1, y2, fill = 'gray', width = 3)
    canvas.create_line(x2, y2, x1, y2, fill = 'gray', width = 3)
    if app.hookFull != False:
        canvas.create_oval(x1 - app.height/40, y2, x1, y2 + app.height/20, fill = app.hookFull)
        canvas.create_polygon(x1 - app.height/80, y2 + app.height/100, 
                    x1 - app.height/40, y2 + app.height/20 + app.height/60, x1, y2 + app.height/20 + app.height/60, fill = app.hookFull )

def draw_background(app,canvas):
    canvas.create_rectangle(0, 0, app.width, app.height * .35, 
                            fill = 'light blue')
    canvas.create_rectangle(0, app.height * .35, 
                            app.width, app.height, fill = app.waterColor)
    canvas.create_oval(10, 10, 100, 100, fill = 'yellow')
    # boat
    canvas.create_rectangle(app.width/1.7, app.height * 0.3,
     app.width/2 + app.width*0.25, app.height * 0.35, fill = 'brown')
     # rod
    canvas.create_line(app.width/2, app.height * 0.23, 
                            app.width/ 1.6, app.height * 0.3, width = 6)

def spawnFish(app):
    speed = random.choice([3, 5, 7])
    dir = random.choice([1, -1])
    if dir == 1:
        x = 0
    else:
        x = app.width
    y = random.choice([app.width * .65,app.width * .5 ,
                                app.width * .6, app.width * .7, app.width * .8])
    type = random.choice(app.types)
    app.fishes.append(Fish(x, y, dir, speed, type, False))

def spawnGator(app):
    dir = random.choice([1, -1])
    if dir == 1:
        x = 0
    else:
        x = app.width
    y = random.choice([app.width * .3,app.width * .4 ,app.width * .5 ,
            app.width * .45 ,app.width * .6, app.width * .5, app.width * .35])
    app.gators.append(Gator(x, y, dir, False))

def fish_timerFired(app):
    if not app.gameOver:
        app.timerCount += 1
        if app.timerCount % 10 == 0:
            app.timerCount = 0
            gator = random.choice([0,0,0,1,1])
            if gator == 1:
                spawnGator(app)
            else:
                spawnFish(app)
        for fish in app.fishes:
            fish.x += fish.speed * fish.dir
            if not app.hookFull and hookedFish(app, fish):
                app.hookFull = fish.type
        for gator in app.gators:
            speed = random.choice([20, 15, 10])
            gator.x += speed * gator.dir
            isGatorHooked(app, gator)
    else:
        app.gameOverCounter +=1
        #if app.gameOverCounter > 20:
        #   app.mode = 'final'



def drawGator(app, canvas, gator):
    #body
    x1 = gator.x
    y1 = gator.y
    x2 = gator.x - gator.dir * app.width/7
    y2 = gator.y + app.height/25
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'dark green')
    #snout
    x1 = gator.x
    y1 = gator.y + app.height/40
    x2 = x1 + gator.dir * app.width/25
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'dark green')
    #tail
    x1 = gator.x - gator.dir * app.width/7
    y1 = gator.y + app.height/35
    x2 = x1 - gator.dir * app.width/10
    y2 = gator.y + app.height/45
    canvas.create_rectangle(x1, y1, x2, y2, fill = 'dark green')

    

def drawFish(app, canvas, fish):
    x1 = fish.x
    y1 = fish.y
    x2 = fish.x - fish.dir * app.width/20
    y2 = fish.y + app.height/40
    canvas.create_oval(x1, y1, x2, y2, fill = fish.type)
    canvas.create_polygon(x2 + fish.dir * app.width/100, (y1+y2)/2, x2 - fish.dir * app.width/60, y2,
                                         x2 - fish.dir * app.width/60, y1, fill = fish.type)

def hookedFish(app, fish):
    x1 = int(app.xHook)
    y1 = int(app.yHook) - 20
    y2 = int(app.yHook + app.height/35) + 20
    x2 = int(app.xHook - app.width/100)
    x = fish.x
    y = fish.y
    if x in range(x2, x1) and y in range(y1, y2):
        app.hookFull = fish.type
        app.fishes.remove(fish)
        return True
    return False

def isGatorHooked(app, gator):
    #body 
    x1 = int(gator.x)
    y1 = int(gator.y)
    x2 = int(gator.x - gator.dir * app.width/7)
    y2 = int(gator.y + app.height/25)
    xHook = int(app.xHook - app.width/100)
    yHook = int(app.yHook + app.height/35)
    if gator.dir > 0:
        if xHook in range(x2, x1) and yHook in range(y1, y2):
            app.gameOver = True
    else:
        if xHook in range(x1, x2) and yHook in range(y1, y2):
            app.gameOver = True 
    # snout
    x1 = int(gator.x)
    y1 = int(gator.y + app.height/40)
    x2 = int(x1 + gator.dir * app.width/25)
    if gator.dir > 0:
        if xHook in range(x2, x1) and yHook in range(y1, y2):
            app.gameOver = True
    else:
        if xHook in range(x1, x2) and yHook in range(y1, y2):
            app.gameOver = True 
    #tail 
    x1 = int(gator.x - gator.dir * app.width/7)
    y1 = int(gator.y + app.height/35)
    x2 = int(x1 - gator.dir * app.width/10)
    y2 = int(gator.y + app.height/45)
    if gator.dir > 0:
        if xHook in range(x2, x1) and yHook in range(y1, y2):
            app.gameOver = True
    else:
        if xHook in range(x1, x2) and yHook in range(y1, y2):
            app.gameOver = True 
    
def drawKey(app, canvas):
    canvas.create_rectangle(app.width * .8, app.height * .02, 
                            app.width* 0.98, app.height * 0.25, fill = 'white')
    x1 = app.width * .88
    y1 = app.height*.05
    x2 = x1 - app.width/20
    y2 = y1 + app.height/40
    canvas.create_oval(x1, y1, x2, y2, fill = 'green')
    canvas.create_polygon(x2 +app.width/100, (y1+y2)/2, x2 - app.width/60, y2,
                                        x2 - app.width/60, y1, fill = 'green')
    canvas.create_text(app.width *.93, (y1+y2)/2, text = 'Arapaima')

    x1 = app.width * .88
    y1 = app.height*.09
    x2 = x1 - app.width/20
    y2 = y1 + app.height/40
    canvas.create_oval(x1, y1, x2, y2, fill = 'grey')
    canvas.create_polygon(x2 +app.width/100, (y1+y2)/2, x2 - app.width/60, y2,
                                        x2 - app.width/60, y1, fill = 'grey')
    canvas.create_text(app.width *.93, (y1+y2)/2, text = 'Tarpon')

    x1 = app.width * .88
    y1 = app.height*.13
    x2 = x1 - app.width/20
    y2 = y1 + app.height/40
    canvas.create_polygon(x2 +app.width/100, (y1+y2)/2, x2 - app.width/60, y2,
                                        x2 - app.width/60, y1, fill = 'yellow', width = 1, outline = 'black')
    canvas.create_oval(x1, y1, x2, y2, fill = 'yellow')
    canvas.create_text(app.width *.93, (y1+y2)/2, text = 'Trout')

    x1 = app.width * .88
    y1 = app.height*.17
    x2 = x1 - app.width/20
    y2 = y1 + app.height/40
    canvas.create_polygon(x2 +app.width/100, (y1+y2)/2, x2 - app.width/60, y2,
                                        x2 - app.width/60, y1, fill = 'orange', width = 1, outline = 'black')
    canvas.create_oval(x1, y1, x2, y2, fill = 'orange')
    canvas.create_text(app.width *.93, (y1+y2)/2, text = 'Red Snapper')

    x1 = app.width * .88
    y1 = app.height*.21
    x2 = x1 - app.width/20
    y2 = y1 + app.height/40
    canvas.create_polygon(x2 +app.width/100, (y1+y2)/2, x2 - app.width/60, y2,
                                        x2 - app.width/60, y1, fill = 'brown', width = 1, outline = 'black')
    canvas.create_oval(x1, y1, x2, y2, fill = 'brown')
    canvas.create_text(app.width *.93, (y1+y2)/2, text = 'Grouper')

def fish_redrawAll(app, canvas):
    draw_background(app, canvas)
    for fish in app.fishes:
        if not fish.hooked:
            drawFish(app, canvas, fish)
    for gator in app.gators:
        drawGator(app, canvas, gator)
    drawHook(app, canvas)
    canvas.create_text(app.width/2, 50, text = f'Score: {app.score}', 
                                            font = 'Arial 25')
    drawKey(app, canvas)
    if app.gameOver:
        canvas.create_text(app.width/2, app.height/2,
        text = 'You snagged an alligator.\n Not a true Florida jit :/', font = "Arial 50")
        canvas.create_text(app.width/2, app.height/2 + 200,
                                     text = 'Press \'r\' to restart', font = 'Arial 25')
    
