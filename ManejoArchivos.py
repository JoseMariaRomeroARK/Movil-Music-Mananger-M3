# -*- coding: UTF-8 -*-

def buscarDirectorio():
    from tkinter import Tk, filedialog
    Tk().withdraw()
    direc = filedialog.askdirectory()
    return direc

def buscarArchivo():
    from tkinter import Tk, filedialog
    Tk().withdraw()
    filename = filedialog.askopenfile()
    return filename.name
