# -*- coding: UTF-8 -*-
# @author JoseMariaRomeroARK visit my gitHub site at: https://github.com/JoseMariaRomeroARK

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
