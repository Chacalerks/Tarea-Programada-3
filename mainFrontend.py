#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

"""
Documentación IMPORTANTE:
+La interfaz del main no se cuentra una función y es por custiones de eficiencia y menos exigencia al procesador, ya que los frames no cambian solo el main 
    el top bar y el nav bar no cambia y volver a ejecutarlo en una función recursuva hace que se destruya y se vuelva a crear haciendo que el procesador 
    ejecute instrucciones inecesarias.
"""

from tkinter import PhotoImage
import tkinter as tk
from generarXML import *
from renovar import*
from crearPDF import*
from generarLicencias import*
from about import *
from general import*
from funciones import *
from archivo import *
from validaciones import *
from reportes import *

lista = []
lista = leerDatos('datos')




#Configuaricón de la ventana
root = tk.Tk()
root.title("Sistema de Licencias")
root.geometry("1400x900+150+50")

#Barra superior
topFrame = tk.Frame(root, bg=color["topbar"])
topFrame.pack(side="top", fill=tk.BOTH)

#Header
titulo = tk.Label(topFrame, text="SISTEMA DE LICENCIAS", font="Bahnschrift 15", bg=color["topbar"], fg="white", height=1, padx=20)
titulo.pack()

#Panel de navegación:
navFrame = tk.Frame(root, bg=color["sidebar"], width=300)
navFrame.pack(side="left",fill=tk.BOTH)

#Panel Principal
mainFrame = tk.Frame(root, bg=color["fondo"])
mainFrame.pack(fill=tk.BOTH, expand=1)

#Cargar el inicio
card_img = PhotoImage(file=".\iconos\card.png")

corazon_lb = tk.Label(mainFrame, image=card_img, bd=0,bg=color["fondo"])
corazon_lb.pack(side="top") 


#Botones de navegación:
#Crear XML
insertar_btn = tk.Button(navFrame, text="Crear XML",font="BahnschriftLight 12", bg=color["caja"],fg="black", activebackground="black",\
activeforeground="black", bd=0, padx=60, pady=5, command=crearXML_ES)
insertar_btn.place(x=50, y=80, width=200)

#Generar Licencias
generar_btn = tk.Button(navFrame, text="Generar licencias",font="BahnschriftLight 12", bg=color["caja"],fg="black", activebackground="black",\
activeforeground="black", bd=0, padx=60, pady=5,command=lambda:generarLicenciasES(mainFrame, card_img,leerXML(),lista))
generar_btn.place(x=50, y=160, width=200)

#Renovar Licencias
actualizar_btn = tk.Button(navFrame, text="Renovar",font="BahnschriftLight 12", bg=color["caja"],fg="black", activebackground="black",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:renovarLicenciaES(mainFrame, card_img, lista))
actualizar_btn.place(x=50, y=240, width=200)

#Generar PDF
eliminar_btn = tk.Button(navFrame, text="Generar PDF",font="BahnschriftLight 12", bg=color["caja"],fg="black", activebackground="black",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:crearPDF_ES(mainFrame, card_img, lista))
eliminar_btn.place(x=50, y=320, width=200)

#Reportes de Excel
provincia_btn = tk.Button(navFrame, text="Reportes de Excel",font="BahnschriftLight 12", bg=color["caja"],fg="black", activebackground="black",\
activeforeground="black", bd=0, padx=60, pady=5,  command=lambda:menuReportes(mainFrame, card_img, lista))
provincia_btn.place(x=50, y=400, width=200)

#Acerca de 
acerca_btn = tk.Button(navFrame, text="Acerca de",font="BahnschriftLight 12", bg=color["caja"],fg="black", activebackground="black",\
activeforeground="black", bd=0, padx=60, pady=5, command=lambda:about(mainFrame, card_img, lista))
acerca_btn.place(x=50, y=480,width=200)


#Salir
salir_btn = tk.Button(navFrame, text="Salir",font="BahnschriftLight 12", bg=color["caja"],fg="black", activebackground="black",\
activeforeground="black", bd=0, padx=60, pady=5, command=salir)
salir_btn.place(x=50, y=800,width=200)


#Cargar Ventana:
root.mainloop()