#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:05/06/2021 07:21 p.m
#Última modificación:21/06/2021 10:59  a.m
#Versión: 3.9.5
import tkinter as tk
from tkinter import IntVar, ttk, messagebox
from tkinter.constants import E
from general import *
from validaciones import *
from funciones import *
from archivo import *

def generarLicenciasES(mainFrame,corazon_img,tipos,lista):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario generar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    cantidad = IntVar()
    cantidad.set(1)
    tk.Label(grupo, text="      Generar Licencias ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)
    #Cantidad
    tk.Label(grupo, text="Cantidad: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=2, column=0, pady=10,padx=10,sticky=E)
    cantidad_spb = ttk.Spinbox(grupo,textvariable=cantidad,from_=1,to=250,width=50,state="readonly")
    cantidad_spb.grid(row=2, column=1, pady=10,padx=10)

    #Generar Bonotes
    generar_btn = ttk.Button(grupo, text="Generar Licencias",width=40,padding=20, command=lambda:generarLicenciasValidaciones(cantidad,tipos,lista))
    generar_btn.grid(row=9, column=1,padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=450,  sticky=E)

def generarLicenciasValidaciones(cantidad,tipos,lista):
    """
    Funcionamiento: Se encarga de crear la licencias
    Entradas: -mainFrame: mainFrameEl contenedor(frame), -lista: la base de datos
    Salidas: NA
    """
    cantidad = cantidad.get()
    generarLicencias(cantidad,tipos,lista)
    guardarDatos('datos',lista)
    messagebox.showinfo(title=tittle, message="Se han generado "+str(cantidad)+" licencias correctamente")