# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:33:31 2022

@author: Xavier
"""

dato = "01.01.2000 00:00"

dividir = dato.split(" ")

fecha = dividir[0]
dia = int(fecha[0:2])
mes = int(fecha[3:5])
lmes = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "Octuber", "November", "December"]
anio = int(fecha[6:])

reloj = dividir[1]
hora = int(reloj[0:2])
minutos = int(reloj[3:])


print(lmes[mes])
print(str(hora) + " horas")
print(str(minutos) + " minutos")



