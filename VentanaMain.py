# -*- coding: UTF-8 -*-
# @author JoseMariaRomeroARK visit my gitHub site at: https://github.com/JoseMariaRomeroARK
from tkinter import *
import Utilidades
import os, shutil, threading
from VentanAux import createNew
listaFormatos =[".mp3",".aac",".m4a",".mp4",".wma",".wav",".atrac",".m4p",".m3p",".flac",".midi",".oog"]

ruta = Utilidades.getRuta()

#
# Ventana principal
#
def createNewMain(lista):

    ventana = Tk()

    vrd = PhotoImage(file=(ruta+'verde.png'),format='png')
    rj = PhotoImage(file=(ruta+'rojo.png'),format='png')
    marco = Frame(ventana)
    marco.grid(column=0,row=0,padx=(60,60),pady=(15,15))
    #Copia un(o conjunto de) archivo(s)  a la carpeta de destino
    # e inserta su(s) nombre(s) en el Listbox de destino además de quitarlo del de origen
    def copiar(Marcador,ListboxOrig,ListboxDest,dirOrig,dirDest):
        try:
            for seleccionado in ListboxOrig.curselection()[::-1]:
                nombre = ListboxOrig.get(seleccionado)
                print("Copying: "+nombre)
                shutil.copyfile(dirOrig+"/"+nombre,dirDest+"/"+nombre)
                ListboxOrig.delete(seleccionado)
                ListboxDest.insert(END,nombre)
                print("Copied")
        except:
            print("File error, maybe you are tring to copy a folder.")
        finally:
            cambiar_a_verde()

    #Borra un(o conjunto de) archivo(s) de la carpeta de destino
    # e inserta su(s) nombre(s) en el Listbox de origen además de quitarlo del de destino
    def borrar(ListboxOrig,ListboxDest,dirOrig,dirDest):
        try:
            for seleccionado in ListboxDest.curselection()[::-1]:
                nombre = ListboxDest.get(seleccionado)
                print("Removeing: "+nombre)
                os.remove(dirDest+"/"+nombre)
                ListboxDest.delete(seleccionado)
                ListboxOrig.insert(END,nombre)
                print("Removed")
        except:
            print("File error")
        finally:
            cambiar_a_verde()

    #Cambia el color del indicador de estado a rojo (ocupado)
    def cambiar_a_rojo():
         Ocupado.set(True)
         imagenLB.config(image=rj)
         ventana.title("Movile Music Mananger (M3)")

    #Cambia el color del indicador de estado a verde (libre)
    def cambiar_a_verde():
        Ocupado.set(False)
        imagenLB.config(image=vrd)
        ventana.title("Movile Music Mananger (M3)")

    #Corre un Thread que copia el/los archivos seleccionados
    def ThreadCopiar(Marcador,ListboxOrig,ListboxDest,dirOrig,dirDest):
        if not Ocupado.get():
            cambiar_a_rojo()
            ventana.title("Movile Music Mananger (M3) - Copying...")
            threading.Thread(target=copiar,args=(Marcador,ListboxOrig,ListboxDest,dirOrig,dirDest,)).start()

    #Corre un Thread que borra el/los archivos seleccionados
    def ThreadBorrar(Marcador,ListboxOrig,ListboxDest,dirOrig,dirDest):
         if not Ocupado.get():
            cambiar_a_rojo()
            ventana.title("Movile Music Mananger (M3) - Removeing...")
            threading.Thread(target=borrar,args=(ListboxOrig,ListboxDest,dirOrig,dirDest,)).start()

    #comoponetes de la interfaz
    #Variables:
    Ocupado = BooleanVar(value=False)
    varOrigen = StringVar(value=lista[1])
    varDestino = StringVar(value=lista[2])

    #Fila 0:
    lblOrigen= Label(marco,text="Origin: ")
    imagenLB = Label(marco,image=vrd)
    lblDestino= Label(marco,text="Destination: ")



    #Fila 2:
    botonCambiarO = Button(marco,text="Change origin",command= lambda: cambioValores(Ocupado,ventana,varDestino.get(),varOrigen.get()))
    botonCambiarD = Button(marco,text="Change destination",command= lambda: cambioValores(Ocupado,ventana,varDestino.get(),varOrigen.get()))

    #Fila 3:
    marcoOrigen = Frame(marco)
    ScrollbarMarcoOrigen = Scrollbar(marcoOrigen,orient=VERTICAL)
    ListboxMarcoOrigen = Listbox(marcoOrigen,height=30,width=37,selectmode=EXTENDED,yscrollcommand=ScrollbarMarcoOrigen.set)
    ScrollbarMarcoOrigen.config(command=ListboxMarcoOrigen.yview)

    ScrollbarMarcoOrigen.pack(side=RIGHT,fill=Y)
    ListboxMarcoOrigen.pack(side=LEFT,fill=BOTH)

    marcoPasar = Frame(marco)
    BotonPasar = Button(marcoPasar,text="-->",command=lambda: ThreadCopiar(imagenLB,ListboxMarcoOrigen,ListboxMarcoDestino,varOrigen.get(),varDestino.get()))
    BotonQuitar = Button(marcoPasar,text="<--",command=lambda: ThreadBorrar(imagenLB,ListboxMarcoOrigen,ListboxMarcoDestino,varOrigen.get(),varDestino.get()))
    BotonPasar.grid(row=0,column=0)
    BotonQuitar.grid(row=1,column=0)

    marcoDestino = Frame(marco)
    ScrollbarMarcoDestino = Scrollbar(marcoDestino,orient=VERTICAL)
    ListboxMarcoDestino = Listbox(marcoDestino,height=30,width=37,selectmode=EXTENDED,yscrollcommand=ScrollbarMarcoDestino.set)
    ScrollbarMarcoDestino.config(command=ListboxMarcoDestino.yview)

    ScrollbarMarcoDestino.pack(side=RIGHT,fill=Y)
    ListboxMarcoDestino.pack(side=RIGHT,fill=BOTH)

    #Fila 4:
    lblOrigenCarpeta= Label(marco,text=varOrigen.get())
    lblDestinoCarpeta= Label(marco,text=varDestino.get())

    #distribución de la interfaz
    #row 0(Fila 1):
    lblOrigen.grid(row=0,column=0)
    imagenLB.grid(row=0,column=1)
    lblDestino.grid(row=0,column=2)
    #row 1(Fila 2):
    botonCambiarO.grid(row=1,column=0)
    botonCambiarD.grid(row=1,column=2)
    #row 2(Fila 3):
    marcoOrigen.grid(row=2,column=0)
    marcoPasar.grid(row=2,column=1)
    marcoDestino.grid(row=2,column=2)
    #row 3(Fila 4):
    lblOrigenCarpeta.grid(row=3,column=0)
    lblDestinoCarpeta.grid(row=3,column=2)

    #Damos valores:
    rellenar(ListboxMarcoOrigen,ListboxMarcoDestino,varOrigen.get(),varDestino.get())

    #Ajustamos la ventana
    Utilidades.setPref(ventana)

    #Arrancamos
    ventana.mainloop()

#Usamos este metodo para combiar los valores de Destino de datos y Origen de datos
def cambioValores(Ocupado,ventana,valDestino,valOrigen):
    if not Ocupado.get():
        ventana.destroy()
        createNew(valDestino,valOrigen)

#Recopilamos los items de cada conjunto
def rellenar(ListboxOrig,ListboxDest,dirOrig,dirDest):
    try:
        #Lo que hay en el origen de datos (A)
        ListaObjetosOrigenFiltrados = list()
        ListaCarpetas = list()
        ListaObjetosOrigen = os.listdir(dirOrig)
        for item in ListaObjetosOrigen:
            if '.' in item:
                for formato in listaFormatos:
                    if formato in item:
                        ListaObjetosOrigenFiltrados.append(item)
                        break
            else:
                ListaCarpetas.append("Folder: "+item)

        #Lo que hay en el destino de datos (B)
        ListaObjetosDestinoFiltrados = list()
        ListaObjetosDestino = os.listdir(dirDest)
        for item in ListaObjetosDestino:
            if '.' in item:
                for formato in listaFormatos:
                    if formato in item:
                        ListaObjetosDestinoFiltrados.append(item)
                        break
        #Lo que debe mostrarse en el ListBoxDestino = [AUB](c)
        conjuntoD = list()
        for cancionD in ListaObjetosOrigenFiltrados:
            for cancion in ListaObjetosDestinoFiltrados:
                if cancion == cancionD:
                    conjuntoD.append(cancionD)
                    ListboxDest.insert(END,cancionD)
                    break

        #Lo que debe mostrarse en el ListBoxOrigen = A-C (D)
        #(añadimos las carpetas para mejorara la experiencia del usuario)
        for carpeta in ListaCarpetas:
            ListboxOrig.insert(END,carpeta)
        #reelemanos con canciones

        for cancion in ListaObjetosOrigenFiltrados:
            coincidencias = 0
            for cancionD in conjuntoD:
                if cancion == cancionD:
                    coincidencias += 1
            if coincidencias == 0:
                ListboxOrig.insert(END,cancion)

    except:
        print("Error\nOrigin directory: "+dirOrig+"\nDestination directory: "+dirDest)