# -*- coding: UTF-8 -*-
#Proyecto Python:
#Bajo la galeria de entorno grafico "Tkynter"
# @author Jose Maria Romero

""" Galería de metedos útiles y de uso recurrente """

def getRuta():
    #Obtiene la ruta donde se aloja el proyecto. Es necesario para cargar las imagenes
    import inspect, os
    return  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/"

def center(win):
    #"Centra la pantalla"
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 4)
    y = (win.winfo_screenheight() // 4)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def setIcono(win):
    #Aloja como icono de la applicacion la imagen especificada
    ruta = getRuta()
    win.iconbitmap((ruta+'music.ico'))

def setPref(win):
    #Ver center(win) y setIcon(win)
    center(win)
    setIcono(win)
    win.title("Movile Music Mananger (M3)")

"""
    Recibe una variable de tipo cadena qe sabemos que representa una fecha
    Los tipos de configuracion aceptados (tanto de salida como de entrada) son:
        -EU: dd/mm/yyyy
        -US: mm/dd/yyyy
        -JP: yyyy/mm/dd
    El caracter @param spaceChar hace referencia al separador
"""
def formatFecha(fecha,enterType="JP",exitType="EU",spaceChar="-"):
    fecalista=fecha.split(spaceChar)
    if enterType=="US":
        dia=fecalista[1]
        mes=fecalista[0]
        anio=fecalista[2]

    elif enterType=="JP":
        dia=fecalista[2]
        mes=fecalista[1]
        anio=fecalista[0]

    else:
        dia=fecalista[0]
        mes=fecalista[1]
        anio=fecalista[2]

    if exitType=="US":
        return str(mes+spaceChar+dia+spaceChar+anio)
    elif exitType=="JP":
        return str(anio+spaceChar+mes+spaceChar+dia)
    else:
        return str(dia+spaceChar+mes+spaceChar+anio)

def secToMin(segundos):
    #Convierte los segundos en minutos
    mins = segundos//60
    sec = segundos - (mins*60)
    minisandsec = "{0}:{1}".format(str(mins),str(sec))
    return minisandsec

def minToSec(minutos):
    #Convierte los minutos en segundos
    split = minutos.split(":")
    segundos = (int(split[0])*60)+(int(split[1]))
    return segundos

