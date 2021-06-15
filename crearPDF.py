#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización: 13/06/2021 10:10 p.m
#Última modificación: 
#Versión: 3.9.5
from generarXML import crearXML
from fpdf import FPDF
from datetime import datetime
import tkinter as tk
from tkinter import StringVar, ttk, messagebox
from tkinter.constants import E
from typing import Text
from general import *
from validaciones import *
from funciones import *
from archivo import* 
    

def crearPDF_ES(mainFrame,corazon_img,lista):
    """
    Funcionamiento: Se encarga de ES
    Entradas: Datos: mainframe: frame donde se va a cargar, corazon: imagen incio, lista: base deatos
    Salidas: Archivo pdf
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    cedula = StringVar()
    
    tk.Label(grupo, text="Crear PDF",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=50).grid(row=0, column=0, columnspan=2,padx=10,sticky=E)
    #Cédula
    tk.Label(grupo, text="Cédula: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10,sticky=E)
    cedula_txt = ttk.Entry(grupo,textvariable=cedula, width=80)
    cedula_txt.grid(row=1, column=1, pady=10,padx=10, columnspan=2)

    buscar_btn = ttk.Button(grupo, text="Crear PDF",width=25,padding=10, command=lambda:crearPDFValidacion(lista,cedula))
    buscar_btn.grid(row=4, column=1,padx=5, pady=80)
    
    limpiar_btn = ttk.Button(grupo, text="Limpiar",width=25,padding=10, command=lambda:limpiarCampos([cedula]))
    limpiar_btn.grid(row=4, column=2,padx=5, pady=80)
    
    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=3, columnspan=2, pady=10,padx=300,  sticky=E)
    
    
def crearPDFValidacion(lista,cedula):
    """
    Funcionamiento: Se encarga de las validaciones E/S del pdf
    Entradas: lista: base de datos, Cedula, a buscar
    Salidas: Archivo pdf
    """
    cedula=cedula.get()
    if not validarExistente(cedula,lista):
        messagebox.showwarning(title=tittle, message="No se ha encontrado la licencia ligada a esta cédula")
    else:
        crearPDf(lista[obtenerPosicion(cedula,lista)].mostrarDatos())
        

def crearPDf(datos):
    """
    Funcionamiento: Se encarga de crear el pdf de la licenca
    Entradas: Datos: una tupla con los datos
    Salidas: Archivo pdf
    """
    pdf = FPDF('P', 'mm',(150,90))
    pdf.add_page()
    pdf.add_font('sysfont', '', r"D:\TEC\I SEMESTRE\Intro-Taller (Laura)\Taller\Tareas\Tarea Programada 3\Tarea-Programada-3\arial\arial.ttf", uni=True)
    pdf.set_font('arial', '', 16)

    # El titulo de COSTA RICA
    pdf.set_text_color(0, 195, 246)
    pdf.cell(0, 5, 'REPUBLICA DE COSTA RICA', 0,1)

    # Titulo de Licencia
    pdf.set_font('arial', '', 14)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(0, 5, 'Licencia de Conducir', 0,1)

    # Cédula de identificación
    pdf.set_font('arial', 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(8, 5, 'N°: ')
    # EL número de la base de datos
    pdf.set_font('arial', 'B', 14)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(8, 5, 'CI-'+datos[0],0,1)

    # Fecha de Expedición
    pdf.set_font('arial', 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(30, 5, 'Expedición: ')
    # la Fecha de la base de datos
    pdf.set_font('arial', '', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(8, 5, datos[3],0,1)

    # Fecha de Nacimiento
    pdf.set_font('arial', 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(30, 5, 'Nacimiento: ')
    # la Fecha de la base de datos
    pdf.set_font('arial', '', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(8, 5, datos[2],0,1)

    # Fecha de Vecimiento
    pdf.set_font('arial', 'B', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(31, 5, 'Vencimiento: ')
    # la Fecha de la base de datos
    pdf.set_font('arial', '', 14)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(8, 5, datos[4],0,1)

    # Tipo de licencia
    pdf.set_font('arial', '', 14)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(12, 6, 'Tipo: ')
    # la Fecha de la base de datos
    pdf.set_font('arial', '', 18)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(8, 6, datos[5],0,1)

    # Si es Donador
    if datos[7]:
        pdf.set_font('arial', '', 14)
        pdf.set_text_color(255, 0, 0)
        pdf.cell(5, 5, 'Donador',0,1)

    # Tipo de Sangre
    pdf.set_font('arial', '', 14)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(10, 5, 'T.S: ')
    # la Fecha de la base de datos
    pdf.set_font('arial', '', 14)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(8, 5, datos[6],0,1)

    # nombre de la persona
    pdf.set_font('arial', 'B', 18)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(8, 6, datos[1],0,1)

    # Hora Actual
    pdf.set_font('arial', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(10, 5, obtenerFechaActual()+" "+obtenerHoraActual()+ " No se que es esto")
    crearArchivo(pdf)

def crearArchivo(pdf):
    """
    Funcionamiento: Se encarga de validar que el archivo no esté abierto
    Entradas: pdf: objeto de pdf
    Salidas: Archivo pdf
    """
    try:
        pdf.output('licencia'+obtenerFechaActual()+'.pdf')
        messagebox.showinfo(title=tittle, message="Se ha creado el PDF!")
        abrirPage('licencia'+obtenerFechaActual()+'.pdf')
    except:
        messagebox.showwarning(title=tittle, message="No se puede crear el pdf, cierre el archivo abierto!")