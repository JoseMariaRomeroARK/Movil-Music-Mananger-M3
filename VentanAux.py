# -*- coding: UTF-8 -*-
# @author JoseMariaRomeroARK visit my gitHub site at: https://github.com/JoseMariaRomeroARK

from tkinter import *
import Utilidades, ManejoArchivos
from VentanaMain import createNewMain

Constante_WARNING = "Please use these wisely do not touch if you do not understand it."
Constante_FILL = "Choose a directory..."

def createNew(valDestino,valOrigen):
    def rellenarEntry(var):
        var.set(ManejoArchivos.buscarDirectorio())

    def guardarYpasar():
        orText = OrigenTexto.get()
        deText = DestinoTexto.get()
        if  orText !=Constante_FILL and deText != Constante_FILL:
            if  orText != "" and deText != "":
                archivo = open(Utilidades.getRuta()+"DesOrg.txt","w")
                archivo.write(Constante_WARNING)
                archivo.write("\n"+OrigenTexto.get())
                archivo.write("\n"+DestinoTexto.get())
                archivo.close()
                ventana.destroy()
                lista = ["",orText,deText]
                createNewMain(lista)
            else:
                print("Error")
        else:
            print("Error")

    ventana = Tk()
    if  valDestino == '' or valOrigen == '':
        varOrigen = StringVar(ventana,value=Constante_FILL)
        varDestino = StringVar(ventana,value=Constante_FILL)
    else:
        varOrigen = StringVar(ventana,value=valOrigen)
        varDestino = StringVar(ventana,value=valDestino)

    marco = Frame(ventana)
    marco.grid(column=0,row=0,padx=(50,50),pady=(10,10))

    OrigenDir = Label(marco,text="Origin directory: ")
    OrigenDir.grid(row=0,column=0,sticky=W)
    OrigenTexto = Entry(marco,width=25,textvariable=varOrigen)
    OrigenTexto.grid(row=0,column=1,sticky=W)
    BotonOrigen = Button(marco,text="Browser",command=lambda: rellenarEntry(varOrigen))
    BotonOrigen.grid(row=0,column=2,sticky=W)

    DestinoDir = Label(marco,text="Destination directory: ")
    DestinoDir.grid(row=1,column=0,sticky=W)
    DestinoTexto = Entry(marco,width=25,textvariable=varDestino)
    DestinoTexto.grid(row=1,column=1,sticky=W)
    BotonDestino = Button(marco,text="Browser",command=lambda: rellenarEntry(varDestino))
    BotonDestino.grid(row=1,column=2,sticky=W)

    BotonDone = Button(marco,text="Finish",command=guardarYpasar)
    BotonDone.grid(row=2,column=1)

    Utilidades.setPref(ventana)
    ventana.mainloop()