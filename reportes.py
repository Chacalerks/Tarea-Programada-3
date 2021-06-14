#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

from tkinter import messagebox
from archivo import *
from funciones import *
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import E
from typing import Text
from general import *
from validaciones import *
from funciones import *
from archivo import*

def menuReportes(mainFrame,corazon_img,matriz):

    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="Reportes ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)

    #Por Provincia
    provincia_btn = tk.Button(grupo, text="Por Provincia",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:porProvincia(mainFrame,corazon_img,matriz))
    provincia_btn.grid(row=1, column=0,padx=15, pady=35)

    #Por Rango de edad
    rango_btn = tk.Button(grupo, text="Por Rango de Edad",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20, command=lambda:porEdad(mainFrame,corazon_img,matriz))
    rango_btn.grid(row=1, column=1,padx=15, pady=35)

    #Por tipo de sangre
    sangre_btn = tk.Button(grupo, text="Por Tipo de Sangre",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:porTipoSangre(mainFrame,corazon_img,matriz))
    sangre_btn.grid(row=2, column=0,padx=15, pady=35)

    #Lista completa de donadores
    completos_btn = tk.Button(grupo, text="Lista Completa de Donadores",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:reporteTotalES(matriz))
    completos_btn.grid(row=2, column=1,padx=15, pady=35)

    #Mujeresdonantes O-
    mujeres_btn = tk.Button(grupo, text="Mujeres Donantes O-",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:reporteMujeresONegativoES(matriz))
    mujeres_btn.grid(row=3, column=0,padx=15, pady=35)

    #¿A quién puede donar?
    donadores_btn = tk.Button(grupo, text="¿A quién puede donar?",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:porDonador(mainFrame,corazon_img,matriz))
    donadores_btn.grid(row=3, column=1,padx=15, pady=35)

    #¿De quién puede recibir?
    receptor_btn = tk.Button(grupo, text="¿De quién puede recibir?",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:porReceptor(mainFrame,corazon_img,matriz))
    receptor_btn.grid(row=4, column=0,padx=15, pady=35)

    #No activos
    receptor_btn = tk.Button(grupo, text="Donadores No activos",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:reporteNoActivosES(matriz))
    receptor_btn.grid(row=4, column=1, padx=15, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0, column=2, columnspan=2, pady=10, padx=150, sticky=E)

############################################## Por Provincia
def porProvincia(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Es el mini formulario para que el usuario cree el reporte.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - matriz: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="Por Provincia ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)
    #Provincias
    provincia = StringVar()
    provincia.set("San José")
    tk.Label(grupo, text="Provincia: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10, sticky=E)
    provincias_cbo = ttk.Combobox(grupo,textvariable=provincia, width=47, state="readonly")
    provincias_cbo['values']= ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón"]
    provincias_cbo.grid(row=1, column=1, pady=10,padx=10)

    generar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reporteProvinciaES(provincia,matriz))
    generar_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:menuReportes(mainFrame,corazon_img,matriz))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

############################################## Por EDAD
def porEdad(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Es el mini formulario para que el usuario cree el reporte.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - matriz: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    tk.Label(grupo, text="Reportes ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)
    #Edad Inicial
    edadIn = StringVar() 
    edadIn.set("")
    tk.Label(grupo, text="Edad Inicial: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=0, column=0, pady=10,padx=10,sticky=E)
    edadIn_txt = ttk.Entry(grupo,textvariable=edadIn, width=50)
    edadIn_txt.grid(row=0, column=1, pady=10,padx=10)

    #Edad Final
    edadFin = StringVar() 
    edadFin.set("")
    tk.Label(grupo, text="Edad Final: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10,sticky=E)
    edadFin_txt = ttk.Entry(grupo,textvariable=edadFin, width=50)
    edadFin_txt.grid(row=1, column=1, pady=10,padx=10)

    generar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reporteEdadES(edadIn,edadFin,matriz))
    generar_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:menuReportes(mainFrame,corazon_img,matriz))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

############################################## Por Tipo de sangre
def porTipoSangre(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Es el mini formulario para que el usuario cree el reporte.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - matriz: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="Reportes ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)

    #Tipo de Sangre
    tipoSangre = StringVar()
    tk.Label(grupo, text="Tipo de Sangre: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=3, column=0, pady=10,padx=10, sticky=E)
    tipoSangre_cbo = ttk.Combobox(grupo,textvariable=tipoSangre, width=47, state="readonly")
    tipoSangre_cbo['values']= ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    tipoSangre_cbo.grid(row=3, column=1, pady=10,padx=10)

    generar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reporteTipoSangreES(tipoSangre,matriz))
    generar_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:menuReportes(mainFrame,corazon_img,matriz))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

def porDonador(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Es el mini formulario para que el usuario cree el reporte.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - matriz: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="¿A quién puede donar?",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)

    #Tipo de Sangre
    tipoSangre = StringVar()
    tk.Label(grupo, text="Tipo de Sangre: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=3, column=0, pady=10,padx=10, sticky=E)
    tipoSangre_cbo = ttk.Combobox(grupo,textvariable=tipoSangre, width=47, state="readonly")
    tipoSangre_cbo['values']= ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    tipoSangre_cbo.grid(row=3, column=1, pady=10,padx=10)

    generar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reporteAquienPuedeDonarES(tipoSangre,matriz))
    generar_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:menuReportes(mainFrame,corazon_img,matriz))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

def porReceptor(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Es el mini formulario para que el usuario cree el reporte.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - matriz: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="¿De quién puede recibir?",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)

    #Tipo de Sangre
    tipoSangre = StringVar()
    tk.Label(grupo, text="Tipo de Sangre: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=3, column=0, pady=10,padx=10, sticky=E)
    tipoSangre_cbo = ttk.Combobox(grupo,textvariable=tipoSangre, width=47, state="readonly")
    tipoSangre_cbo['values']= ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    tipoSangre_cbo.grid(row=3, column=1, pady=10,padx=10)

    generar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reporteDeQuienPuedeRecibirES(tipoSangre,matriz))
    generar_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:menuReportes(mainFrame,corazon_img,matriz))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

def reporteProvinciaES(provincia,matriz):
    provincia = provincia.get()
    provincia = obtenerIndexLugar(provincia)
    crearArchivo("provincia.html",reportePlantillaCorta(sacarDonantesProvincia(provincia,sacarDonantesActivos(matriz)),"provincia"))
    abrirPage("provincia.html")

def reporteEdadES(edadIn,edadFin,matriz):
    edadIn = edadIn.get()
    edadFin = edadFin.get()
    if not validarEntero(edadFin) or not validarEntero(edadIn):
        messagebox.showwarning(title=tittle, message="El texto no corresponde a una edad válida")
    elif not validarRangoEdad(edadIn) or not validarRangoEdad(edadFin):
        messagebox.showwarning(title=tittle, message="Las edades no están en un rango válido para un donador")
    elif not validarEdades(edadIn,edadFin):
        messagebox.showwarning(title=tittle, message="Hay un conflicto en las edades")
    else:
        edadIn
        print(edadIn,edadFin,matriz[2][2])
        crearArchivo("rango.html",reportePlantillaCorta(sacarDonantesRangoEdad(int(edadIn), int(edadFin), sacarDonantesActivos(matriz)),"rango de edad"))
        abrirPage("rango.html")

def reporteTipoSangreES(tipoSangre,matriz):
    tipoSangre = tipoSangre.get()
    if not validarVacio(tipoSangre):
        messagebox.showwarning(title=tittle, message="Debe seleccionar una opción.")
    else:
        crearArchivo("sangre.html",reportePlantillaCorta(sacarDonantesTipoSangre(tipoSangre,sacarDonantesActivos(matriz)),"tipo de sangre"))
        abrirPage("sangre.html")

def reporteTotalES(matriz):
    crearArchivo("total.html",reporteTotal(sacarDonantesActivos(matriz)))
    abrirPage("total.html")

def reporteMujeresONegativoES(matriz):
    crearArchivo("total.html",reportePlantillaCorta(sacarMujeresONegativo(sacarDonantesActivos(matriz)),"mujeres donantes O-"))
    abrirPage("total.html")


def reporteAquienPuedeDonarES(tipoSangre,matriz):
    tipoSangre = tipoSangre.get()
    if not validarVacio(tipoSangre):
        messagebox.showwarning(title=tittle, message="Debe seleccionar una opción.")
    else:
        crearArchivo("aquienDonar.html",reporteSangre(sacarAquienPuedeDonar(tipoSangre,sacarDonantesActivos(matriz)),"a quien puedo donar"))
        abrirPage("aquienDonar.html")

def reporteDeQuienPuedeRecibirES(tipoSangre,matriz):
    tipoSangre = tipoSangre.get()
    if not validarVacio(tipoSangre):
        messagebox.showwarning(title=tittle, message="Debe seleccionar una opción.")
    else:
        crearArchivo("dequienRecibir.html",reporteSangre(sacarDeQuienPuedeRecibir(tipoSangre,sacarDonantesActivos(matriz)),"de quien puedo recibir"))
        abrirPage("dequienRecibir.html")

def reporteNoActivosES(matriz):
    crearArchivo("noActivos.html",reporteNoActivos(sacarNoActivos(matriz)))
    abrirPage("noActivos.html")
