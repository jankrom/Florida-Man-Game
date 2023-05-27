# random stuff from cmu_112_graphics that we would like to keep

from tkinter import Canvas, messagebox, simpledialog, filedialog
from io import BytesIO
import os

def failedImport(importName, installName=None):
    installName = installName or importName
    print('**********************************************************')
    print(f'** Cannot import {importName} -- it seems you need to install {installName}')
    print(f'** This may result in limited functionality or even a runtime error.')
    print('**********************************************************')
    print()

try: from PIL import Image, ImageTk, ImageDraw, ImageFont
except ModuleNotFoundError: failedImport('PIL', 'pillow')
try: import requests
except ModuleNotFoundError: failedImport('requests')

def rgb(red, green, blue):return "#%02x%02x%02x" % (red, green, blue)

def loadImage(path=None):
        if (path is None):
            path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select file: ',filetypes = (('Image files','*.png *.gif *.jpg'),('all files','*.*')))
            if (not path): return None
        if (path.startswith('http')):
            response = requests.request('GET', path) # path is a URL!
            img = Image.open(BytesIO(response.content))
            img = img.convert("RGBA")
        else:
            img = Image.open(path)

        return img

def scaleImage(image, scale, antialias=False):
        # antialiasing is higher-quality but slower
        resample = Image.ANTIALIAS if antialias else Image.NEAREST
        return image.resize((round(image.width*scale), round(image.height*scale)), resample=resample)