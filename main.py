from cmu_112_graphics import *
from boat.boating import *
from education.edu import *
from intro.intro import *
from map.map import *
from fishing.fish import *
from utils import *
import os


def appStarted(self):
    self.path = os.path.abspath(os.getcwd())
    self.mode = 'introMode'
    # education, fishing, introMode, map
    introMode_appStarted(self)
    map_appStarted(self)
    boat_started(self)
    fish_appStarted(self)
    edu_appStarted(self)
    # images for education and fish
    urlFL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/USA_Florida_location_map.svg/1132px-USA_Florida_location_map.svg.png'
    self.imageFL = loadImage(urlFL)
    self.floridaBackground = scaleImage(self.imageFL, .75)
    urlRS = 'https://image.shutterstock.com/image-vector/vector-red-snapper-marine-fish-260nw-1230329710.jpg'
    self.imageRS = loadImage(urlRS)
    self.redSnapper = scaleImage(self.imageRS, .4)
    urlGr = 'https://thumbs.dreamstime.com/b/grouper-fish-vector-illustration-55422248.jpg'
    self.imageGr = loadImage(urlGr)
    self.grouper = scaleImage(self.imageGr, .2)
    urlTar = 'https://thumbs.dreamstime.com/b/salwater-fish-tarpon-178294866.jpg'
    self.imageTar = loadImage(urlTar)
    self.tarpon = scaleImage(self.imageTar, .3)
    urlTrout = 'https://thumbs.dreamstime.com/b/brown-trout-17280687.jpg'
    self.imageTrout = loadImage(urlTrout)
    self.trout = scaleImage(self.imageTrout, .15)
    urlAra = 'https://image.shutterstock.com/image-vector/arapaima-260nw-421192516.jpg'
    self.imageAra = loadImage(urlAra)
    self.arapaima = scaleImage(self.imageAra, .33)
    urlOverFishing = "https://image.shutterstock.com/image-vector/arapaima-260nw-421192516.jpg"
    self.imageOF = loadImage(urlOverFishing)
    self.overfishing = scaleImage(self.imageOF, .32)
    urlOFmap = "https://moldychum.com/wp-content/uploads/2017/08/Overfished_US_stocks_2015-1024x740.png"
    self.imageMap = loadImage(urlOFmap)
    self.OFmap = scaleImage(self.imageMap, .37)
    urlImg = 'https://img.buzzfeed.com/buzzfeed-static/static/2020-05/6/21/asset/77c5e80509de/sub-buzz-602-1588799315-2.png'
    self.meme = loadImage(urlImg)


def redrawAll(self):
    if(self.pause == False):
        if(self.mode == "boat"): boat_redrawAll(self, self.canvas)
        elif(self.mode== 'introMode'): introMode_redrawAll(self, self.canvas)
        elif(self.mode == "helpMode"): helpMode_redrawAll(self, self.canvas)
        elif(self.mode == "map"): map_redrawAll(self, self.canvas)
        elif(self.mode == 'eduIntroMode'): eduIntroMode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg1Mode'): eduPg1Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg2Mode'): eduPg2Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg3Mode'): eduPg3Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg4Mode'): eduPg4Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg6Mode'): eduPg6Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg6_2Mode'): eduPg6_2Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg6_3Mode'): eduPg6_3Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'eduPg7Mode'): eduPg7Mode_redrawAll(self, self.canvas)
        elif(self.mode == 'fish'): fish_redrawAll(self, self.canvas)
        elif(self.mode == 'final'): endScreen_redrawAll(self, self.canvas)


def onTimerFired(self):
    if self.mode =='fish': fish_timerFired(self)
    elif self.mode == 'boat': boat_timerFired(self)
    
def onKeyPressed(self, event):
    if(self.mode == 'boat'): boat_keyPressed(self, event)
    elif(self.mode == 'helpMode'): helpMode_keyPressed(self, event)
    elif(self.mode == 'map'): map_keyPressed(self, event)
    elif(self.mode == 'eduIntroMode'): eduIntroMode_keyPressed(self, event)
    elif(self.mode == 'eduPg1Mode'): eduPg1Mode_keyPressed(self, event)
    elif(self.mode == 'eduPg2Mode'): eduPg2Mode_keyPressed(self, event)
    elif(self.mode == 'eduPg3Mode'): eduPg3Mode_keyPressed(self, event)
    elif(self.mode == 'eduPg4Mode'): eduPg4Mode_keyPressed(self, event)
    elif(self.mode == 'eduPg6Mode'): eduPg6Mode_keyPressed(self, event)
    elif(self.mode == 'eduPg6_2Mode'): eduPg6_2Mode_keyPressed(self, event)
    elif(self.mode == 'eduPg6_3Mode'): eduPg6_3Mode_keyPressed(self, event)
    elif(self.mode == 'eduPg7Mode'): eduPg7Mode_keyPressed(self, event)
    elif(self.mode == 'fish'): fish_keyPressed(self, event)
    

def mousePressed(self, event):
    if(self.mode == 'introMode'): introMode_mousePressed(self, event)
    elif(self.mode == 'map'): map_mousePressed(self, event)

def endScreen_redrawAll(app, canvas):
    canvas.create_rectangle(200,400,300,800)
    canvas.create_text(400, 200, text=f'Your score is {app.score}')
    canvas.create_image(400, 400, image=ImageTk.PhotoImage(app.meme))

runApp(width = 800, height = 800)