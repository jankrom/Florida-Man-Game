# Vihan Karnala 11/6/21

import math
from utils import *
import random


def boat_redrawAll(self, canvas):
    drawHorizon(self, canvas)
    drawWaves(self, canvas)
    createBoat(self, canvas)
    drawSky(self, canvas)
    drawMiniMap(self, canvas)

def drawMiniMap(self, canvas):
    rad = self.miniMapRad
    center = self.height//8, self.width-(self.width//8)
    canvas.create_oval(center[0]-rad, center[1]-rad, center[0]+rad, center[1]+rad, width=0, fill=rgb(5,2,89))
    canvas.create_line(center[0], center[1]-rad, center[0], center[1]+rad)
    canvas.create_line(center[0]-rad, center[1], center[0]+rad, center[1])
    point = []
    point.append(center[0] + self.boatPos[0]//20)
    point.append(center[1] + self.boatPos[1]//20)
    length = 20
    dir = math.pi*(self.boatHeading/180)
    point0 = point[0]+ math.cos(dir)*length, point[1] + math.sin(dir)*length
    dir1 = dir+((140/180)*math.pi)
    point1 = point[0] + math.cos(dir1)*length, point[1] + math.sin(dir1)*length
    dir2 = dir-((140/180)*math.pi)
    point2 = point[0] + math.cos(dir2)*length, point[1] + math.sin(dir2)*length
    canvas.create_polygon(point0[0], point0[1], point1[0], point1[1], point2[0], point2[1], fill='brown4')
    canvas.create_text(100, 600, text='Press a to drop the anchor!', fill='white', font='18')

def drawSky(self, canvas):
    canvas.create_oval(self.sunPos[0]-self.sunR, self.sunPos[1]-self.sunR, 
                            self.sunPos[0]+self.sunR, self.sunPos[1]+self.sunR, 
                            fill=rgb(252, 244, 76), width=0)
    cloudOffSet = [400,80]
    canvas.create_image((self.sunPos[0] + cloudOffSet[0])%self.width, self.sunPos[1] + cloudOffSet[1], image=ImageTk.PhotoImage(self.cloudImg))

def boat_started(self):
    self.waveLocs = []
    self.moving = 0
    self.sunPos = [20,90]
    self.sunR = 50
    (self.midX, self.midY) = (self.width/2, self.height/2)
    self.look = 0
    self.waveR = 70
    self.boatPos = [0,0]
    self.boatHeading = 90
    self.miniMapRad = 60
    self.waveTimer = 0
    self.boatView = 0
    imgUrl = self.path + '/boat/boat.png'
    self.boatImg = loadImage(imgUrl)
    imgUrl = self.path + '/boat/cloud.png'
    self.cloudImg = loadImage(imgUrl)

def boat_keyPressed(self, event):
    if event.key == 'Up':
        self.waveTimer = 0
        self.moving -= 1
        self.boatPos[0]+=4*(math.cos(math.pi*(self.boatHeading)/180))
        self.boatPos[1]+=4*(math.sin(math.pi*(self.boatHeading)/180))
        if self.miniMapRad*15 < ((self.boatPos[0])**2 + (self.boatPos[1])**2)**0.5:
            self.boatPos = [0,0]
        if len(self.waveLocs) < 15 and self.moving <= 0:
            self.waveLocs.append([random.randint(0,self.width), self.midY+self.look-20])
            self.moving = 10

        i = 0
        while i < len(self.waveLocs):
            self.waveLocs[i][1] += 10
            if self.waveLocs[i][1] > self.height:
                self.waveLocs.pop(i)
            i+=1

    elif event.key == 'Left':
        self.sunPos[0]+=10
        self.sunPos[0]%=self.width
        self.boatHeading-=3
        self.waveTimer = 0
        self.moving -= 1

        if len(self.waveLocs) < 15 and self.moving <= 0:
            self.waveLocs.append([0, random.randint(self.midY+ self.look, self.height-40)])
            self.moving = 10

        i = 0
        while i < len(self.waveLocs):
            self.waveLocs[i][0] += 10
            if self.waveLocs[i][0] > self.width:
                self.waveLocs.pop(i)
            i+=1

    elif event.key == 'Right':
        self.sunPos[0]-=10
        self.boatHeading+=3
        if self.sunPos[0] < 0:
            self.sunPos[0]%=self.width

        self.moving -= 1
        if len(self.waveLocs) < 15 and self.moving <= 0:
            self.waveLocs.append([self.width, random.randint(self.midY+ self.look, self.height-40)])
            self.moving = 10

        self.waveTimer = 0
        i = 0
        while i < len(self.waveLocs):
            self.waveLocs[i][0] -= 10
            if self.waveLocs[i][0] < 0:
                self.waveLocs.pop(i)
            i+=1

    elif event.key == 'w':
        if self.look < 200:
            self.look+=5
            self.sunPos[1]+=5

        i = 0
        while i < len(self.waveLocs):
            if self.waveLocs[i][1] < self.midY+self.look:
                self.waveLocs.pop(i)
            i+=1

    elif event.key == 's':
        if self.look > -30:
            self.look-=5
            self.sunPos[1]-=5
    
    elif event.key == 'a':
        self.mode = 'fish'

    elif event.key == 'Backspace':
        self.mode = 'map'


def boat_timerFired(self):
    self.waveTimer +=1
    if self.waveTimer > 5 and len(self.waveLocs) > 0:
        self.waveTimer-=6
        self.waveLocs.pop(0)
        
def drawWaves(self, canvas):
    for point in self.waveLocs:
        canvas.create_arc(point[0]-self.waveR, point[1]-self.waveR, 
                            point[0]+self.waveR, point[1]+self.waveR, 
                            start=270, extent=60, fill='blue', style='arc', width=5)
        canvas.create_arc(point[0]+self.waveR-self.waveR//4, point[1]-self.waveR, 
                            point[0]+2*self.waveR-self.waveR//4, point[1]+self.waveR, 
                            start=210, extent=80, fill='blue', style='arc', width=5)    

def drawHorizon(self, canvas):
        sky, darkWater = rgb(189,236,252), rgb(31,91,222)
        canvas.create_rectangle(0,0,self.width,self.midY+self.look, #sky
                                     fill = sky,width = 0)
        canvas.create_rectangle(0,self.midY+self.look,self.width, #ground
                            self.height, fill= darkWater,width = 0)

def createBoat(self, canvas):
    canvas.create_image(self.midX + self.boatView, self.midY+self.height//6 + self.look,
                             image=ImageTk.PhotoImage(self.boatImg))
    '''point0 = (self.midX + self.boatView, self.midY + self.height//6 + self.look)
    point1 = (self.midX - self.width//6 + self.boatView, self.height+ 100 + self.look)
    point2 = (self.midX + self.width//6 + self.boatView, self.height+ 100 + self.look)
    canvas.create_polygon(point0[0], point0[1], point1[0], point1[1], 
                                point2[0], point2[1], fill='brown4')
    canvas.create_polygon(point0[0], point0[1]+30, point1[0]+20, point1[1], 
                                point2[0]-20, point2[1], fill='tan4')
    '''