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

def generarDonadorES(mainFrame,corazon_img,lista):
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
    cantidad_spb = ttk.Spinbox(grupo,textvariable=cantidad,from_=1,to=250,width=50,state="readonly")
    cantidad_spb.grid(row=0, column=1, pady=10,padx=10)

    #Generar Bonotes
    generar_btn = ttk.Button(grupo, text="Generar Licencias",width=40,padding=20, command=lambda:generarLicenciasValidaciones(cantidad,lista))
    generar_btn.grid(row=9, column=1,padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=450,  sticky=E)

def generarLicenciasValidaciones(cantidad,lista):
    cantidad = cantidad.get()
    generarLicencias(cantidad,['A1','A2','A3','B1','B2','B3','B4','C1','C2','D1','D2','D3','E1','E2'],lista)
    guardarDatos('datos',lista)
    messagebox.showinfo(title=tittle, message="Se han generado "+str(cantidad)+" licencias correctamente")