#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

from tkinter import BooleanVar, StringVar
import tkinter as tk
from tkinter import messagebox


color = {"fondo":"#FFFFFF", "sidebar":"#343A40", "topbar":"#000000", "caja": "#F9D71D" ,  "principal": "#343A40", "secundario": "#343A40","tercero":"#0E3D5E"}
tittle = "Sistema de Licencias"
#----------------------------------------------------------------------------
#                           Navegación
#----------------------------------------------------------------------------
def cargarInicio(mainFrame, card_img):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)

    card_lb = tk.Label(mainFrame, image=card_img, bd=0,bg=color["fondo"])
    card_lb.pack(side="top")
    #tk.Label(mainFrame, text="Donar sangre, es donar vida", font="Bahnschrift 16", bg=color["principal"], fg="white", height=1, padx=20,pady=25).pack(side="top")

def salir():
    """
    Funcionamiento: Se encarga de cerrar el programa
    Entradas: Na
    Salidas: NA
    """
    messagebox.showinfo(title=tittle, message="No olvides gestionar pronto tu licencia")
    exit()

def limpiarFrame(mainFrame):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    for elemento in mainFrame.winfo_children():
        elemento.destroy()

def limpiarCampos(datos):
    """
    Funcionamiento: Limpia los campos del formulario.
    Entradas: Las variables que esta enlazadas alformulario
    Salidas: NA
    """
    i = 0
    while i<len(datos):
        if i == 4:
            datos[i].set(True)
        else:
            datos[i].set("")
        i+=1
#----------------------------------------------------------------------------
#                           Entrada y Salida
#----------------------------------------------------------------------------
def establecerDatos(datosString):
    """
    Funcionamiento: Se encarga de estableces los datos de los campos.
    Entradas: -datosString: el array con las variables.
    Salidas: -Datos: Lista con los datos en string
    """
    datos = []
    i=0
    if len(datosString)==0:# Cuando no hay datos que leer []
        while True:
            if i == 4 :
                datos.append(BooleanVar())
                datos[i].set(True)
            else:
                datos.append(StringVar())
                datos[i].set("")            
                if i==7:
                    break
            i+=1
    else: # cuando se van a cargar datos en el formularios
        while True:
            if i == 4 :
                datos.append(BooleanVar())
                datos[i].set(datosString[i])
            else:
                datos.append(StringVar())
                datos[i].set(datosString[i])            
                if i==7:
                    break
            i+=1
    return datos
    
def obtenerDatos(datos):
    """
    Funcionamiento: Se encarga de obtener los datos de los campos.
    Entradas: -Datos: el array con las variables.
    Salidas: -DatosString: Lista con los datos en string
    """
    datosString = []
    i = 0
    while i<len(datos):
        datosString.append(datos[i].get())
        i+=1
    if datosString[5].isdigit():
        datosString[5]=int(datosString[5])
    return datosString

