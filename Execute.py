# -*- coding: UTF-8 -*-
# @author JoseMariaRomeroARK visit my gitHub site at: https://github.com/JoseMariaRomeroARK


import Utilidades
from VentanaMain import createNewMain
from VentanAux import createNew


archivoCon = open(Utilidades.getRuta()+"DesOrg.txt","r")
lineas = list()
for linea in archivoCon:
    lineas.append(linea)
if len(lineas) != 3:
    createNew('','')
else:
    lista = [lineas[0][:-1],lineas[1][:-1],lineas[2]]
    createNewMain(lista)