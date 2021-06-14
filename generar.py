#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

import tkinter as tk
from tkinter import IntVar, ttk, messagebox
from tkinter.constants import E
from general import *
from validaciones import *
from funciones import *
from archivo import *

def generarDonadorES(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    cantidad = IntVar()
    cantidad.set(1)
    #Cantidad
    tk.Label(grupo, text="Cantidad: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=0, column=0, pady=10,padx=10,sticky=E)
    cantidad_spb = ttk.Spinbox(grupo,textvariable=cantidad,from_=1,to=4000000,width=50,state="readonly")
    cantidad_spb.grid(row=0, column=1, pady=10,padx=10)

    #Generar Bonotes
    generar_btn = ttk.Button(grupo, text="Generar Donadores",width=40,padding=20, command=lambda:generarDonadoresValidaciones(cantidad,matriz))
    generar_btn.grid(row=9, column=1,padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=450,  sticky=E)

def generarDonadoresValidaciones(cantidad,matriz):
    cantidad = cantidad.get()
    generarDonadores(cantidad,matriz)
    guardarDatos('datos',matriz)
    messagebox.showinfo(title=tittle, message="Se han generado "+str(cantidad)+" donadores correctamente")

"""
dicc = {'San Jose':['El banco nacional de sangre', 'Hospital Mexico', 'Hospital San Juan de Dios'],
           'Alajuela':['Hospiital San Rafael de Alajuela','Hospital de San Ramon','Hospital de Canton Norteno'],
           'Cartago':['Hospital Max Peralta'],
           'Heredia':['Hospital San Vicente de Paul'],
           'Guanacaste':['Hospital La Anexión de Nicoya','Hospital Enrique Baltodano de Liberia'],
           'Puntarenas':['Hospital Monseñor Sanabria'],
           'Limon':['Hospital Tony Facio','Hospital de Gupiles']}

guardarDatos('provincias',dicc)
"""