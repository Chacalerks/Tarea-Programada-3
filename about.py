#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:05/06/2021 07:21 p.m
#Última modificación:21/06/2021 10:59  a.m
#Versión: 3.9.5
from tkinter import PhotoImage
from archivo import *
from funciones import *
import tkinter as tk
from tkinter.constants import LEFT
from general import *
from validaciones import *
from funciones import *
from archivo import*

def about(mainFrame,corazon_img,matriz):

    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=10)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="CREADORES ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)
    
    #Creador 1
    textom = "Maynor Erks Martínez Hernández \n\
+Programador y diseñador nicaragüense.  \n\
+CEO, dueño y fundador de Férks \n\
+Egresado del C.T.P de General Viejo. \n \
+Actualmente cuenta con 18 años de edad\n \
+Estudia en el TEC, Ing. Computación"
    creador1 = tk.Frame(grupo, bg=color["principal"])
    creador1.grid(row=1, column=0, padx=20)
    erks_img = PhotoImage(file=".\iconos\maynor.png")
    erks_lb = tk.Label(creador1, image=erks_img, bd=0)
    erks_lb.pack(side="top") 
    tk.Label(creador1,font="BahnschriftLight 15", text="Maynor Erks Martínez Hernández",justify=LEFT, bg=color["principal"],fg="white",pady=5, padx=20).pack()
    tk.Label(creador1,font="BahnschriftLight 12", text=textom, bg=color["principal"],fg="white", pady=10, padx=20).pack()
    

    #Creador 2
    textoc = "César Jiménez Salazar: \n\
+Graduado del Liceo Anastasio Alfaro \n\
+Estudiante de Ingeniería en Computación \n\
+Vecino de Heredia \n\
+Edad: 19 años \n \
"
    creador2 = tk.Frame(grupo, bg=color["principal"])
    creador2.grid(row=1, column=1, padx=20)
    cesar_img = PhotoImage(file = ".\iconos\cesar.png")
    cesar_lb = tk.Label(creador2, image=cesar_img, bd=0)
    cesar_lb.pack(side="top") 
    tk.Label(creador2,font="BahnschriftLight 15", text="César Johel Jiménez Salazar",justify=LEFT, bg=color["principal"],fg="white",pady=5,padx=20).pack()
    tk.Label(creador2,font="BahnschriftLight 12", text=textoc, bg=color["principal"],fg="white", pady=10, padx=20).pack()
    


    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0, column=3)

    tk.Label(grupo, text="Programa realizado para la III Tarea Programada \n\
del curso de Taller de Prgramación GR2\n\
del Tecnológico de Costa Rica.\n\nLa figura del ID Card fue creada por: Freepik y recuperada de: www.flaticon.com \n\nVersión 1.5.2",font="BahnschriftLight 10",justify=LEFT, bg=color["fondo"],fg="black", pady=50, padx=20).grid(row=3, column=0)
    
    tk.Label(grupo, text="",font="BahnschriftLight 15",justify=LEFT, bg=color["fondo"],fg="black", pady=50, padx=20).pack()
