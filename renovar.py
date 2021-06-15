#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

import tkinter as tk
from tkinter import StringVar, ttk, messagebox
from tkinter.constants import E
from typing import Text
from general import *
from validaciones import *
from funciones import *
from archivo import*        

def RevonvarLicenciaES(mainFrame,corazon_img,lista):
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    cedula = StringVar()
    
    tk.Label(grupo, text="Renovar Licencia",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=50).grid(row=0, column=0, columnspan=2,padx=10,sticky=E)
    #Cédula
    tk.Label(grupo, text="Cédula: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10,sticky=E)
    cedula_txt = ttk.Entry(grupo,textvariable=cedula, width=80)
    cedula_txt.grid(row=1, column=1, pady=10,padx=10, columnspan=2)

    buscar_btn = ttk.Button(grupo, text="Buscar",width=25,padding=10, command=lambda:renovarCedula(lista,cedula))
    buscar_btn.grid(row=4, column=1,padx=5, pady=80)
    
    limpiar_btn = ttk.Button(grupo, text="Limpiar",width=25,padding=10, command=lambda:limpiarCampos([cedula]))
    limpiar_btn.grid(row=4, column=2,padx=5, pady=80)
    
    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=3, columnspan=2, pady=10,padx=300,  sticky=E)
    
    
def renovarCedula(lista,cedula):
    cedula=cedula.get()
    if not validarExistente(cedula,lista):
        messagebox.showwarning(title=tittle, message="No se ha encontrado la licencia ligada a esta cédula")
    elif validarPuntaje(obtenerPosicion(cedula,lista),lista) == 'a':
        messagebox.showwarning(title=tittle, message="No puede renovar su licencia hasta que vuelva a hacer el examen teórico")
    elif validarPuntaje(obtenerPosicion(cedula,lista),lista) == False:
        messagebox.showwarning(title=tittle, message="Su puntaje es de 0, y por ende no podrá renovar su licencia")
    else:
        if messagebox.askquestion(title=tittle, message="¿Desea renovar su licencia?") =="yes":
            renovarLicencia(obtenerPosicion(cedula,lista),lista)
            guardarDatos('datos',lista)
            messagebox.showwarning(title=tittle, message="Se ha renovado su licencia!!")
        else:
            messagebox.showinfo(title=tittle, message="No se ha renovado su licencia")
    
