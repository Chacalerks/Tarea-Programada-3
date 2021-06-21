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

"""
DOCUMENTACIÓN
+ En caso de que no existan licencias que cumplan los criterios de búsqueda de algún reporte, de igual forma se generará el reporte
vació ya que es importante notar que no hay licencias con esos parámetros de búsqueda
"""

def menuReportes(mainFrame,corazon_img,lista):
    """
    Funcionamiento: Carga el menú de los reportes.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - lista: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="Reportes ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)

    #Totalidad de Licencias
    provincia_btn = tk.Button(grupo, text="Totalidad de Licencias",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:reporteTotalidadES(lista))
    provincia_btn.grid(row=1, column=0,padx=15, pady=35)

    #Por tipo de licencia
    rango_btn = tk.Button(grupo, text="Por tipo de licencia",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20, command=lambda:porTipoLicencia(mainFrame,corazon_img,lista))
    rango_btn.grid(row=1, column=1,padx=15, pady=35)

    #Examen por sanción
    sangre_btn = tk.Button(grupo, text="Examen por sanción",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:reporteExamenPorSancionES(lista))
    sangre_btn.grid(row=2, column=0,padx=15, pady=35)

    #Los donantes de órganos
    completos_btn = tk.Button(grupo, text="Los donantes de órganos",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:reporteDonanteOrganosES(lista))
    completos_btn.grid(row=2, column=1,padx=15, pady=35)

    #Licencia anulada
    mujeres_btn = tk.Button(grupo, text="Licencia anulada",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:reporteLicenciaAnuladaES(lista))
    mujeres_btn.grid(row=3, column=0,padx=15, pady=35)

    #Licencias por sede
    donadores_btn = tk.Button(grupo, text="Licencias por sede",font="BahnschriftLight 12",bg=color["principal"],fg="white", activebackground="white",
    width=15,activeforeground="black", bd=0, padx=100, pady=20,command=lambda:porSede(mainFrame,corazon_img,lista))
    donadores_btn.grid(row=3, column=1,padx=15, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0, column=2, columnspan=2, pady=10, padx=150, sticky=E)

############################################## Por Tipo de Licencia
def porTipoLicencia(mainFrame,corazon_img,lista):
    """
    Funcionamiento: Es el mini formulario para que el usuario cree el reporte.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - lista: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="Reportes por tipo de Licencia",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)

    #Tipo de licencia
    tipoLicencia = StringVar()
    tk.Label(grupo, text="Tipo de Licencia: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=3, column=0, pady=10,padx=10, sticky=E)
    tipoLicencia_cbo = ttk.Combobox(grupo,textvariable=tipoLicencia, width=47, state="readonly")
    tipoLicencia_cbo['values']= ["A","B","C","D","E"]
    tipoLicencia_cbo.grid(row=3, column=1, pady=10,padx=10)

    generar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reporteTipoLicenciaES(tipoLicencia,lista))
    generar_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:menuReportes(mainFrame,corazon_img,lista))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

def porSede(mainFrame,corazon_img,lista):
    """
    Funcionamiento: Es el mini formulario para que el usuario cree el reporte.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) - lista: La base de datos para buscar el reporte
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    tk.Label(grupo, text="Sedes",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2)

    sede = StringVar()
    tk.Label(grupo, text="Sede: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=3, column=0, pady=10,padx=10, sticky=E)
    sede_cbo = ttk.Combobox(grupo,textvariable=sede, width=47, state="readonly")
    sede_cbo['values']= ['San José, San Sebastián','Montecillos Alajuela','Tránsito Cartago','Barva de Heredia','Tránsito San Ramón','Guapiles, Ruta 32',
               'Barrio Sandoval de Moín','Carretera al Aeropuerto Daniel Oduber','Aeropuerto de Nicoya','Chacarita, Calle 138','Pérez Zeledón',
               'Río Claro de Golfito','San Carlos']
    sede_cbo.grid(row=3, column=1, pady=10,padx=10)
    
    generar_btn = ttk.Button(grupo, text="Crear Reporte",width=40,padding=20, command=lambda:reportePorSedeES(sede,lista))
    generar_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:menuReportes(mainFrame,corazon_img,lista))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)


###Backend

def reporteTotalidadES(lista):
    """
    Funcionamiento: se encarga de crear el reporte de la totalidad de licencias y abrir el mismo
    Entradas: lista: la lista de objetos con todas las licencias
    Salidas: NA
    """
    try:
        reporteFichaLarga("reporte_total_"+generarFechaExp()+".xlsx",lista, "Totalidad de licencias")
        messagebox.showinfo(title=tittle, message="Se ha creado el reporte")
        abrirFile("reporte_total_"+generarFechaExp()+".xlsx", "ReportesExcel")
    except:
        messagebox.showwarning(title=tittle, message="No se puede crear el reporte, cierre el archivo abierto!")

def reporteTipoLicenciaES(tipoLicencia,lista):
    """
    Funcionamiento: se encarga de crear el reporte de cierto tipo de licencias y abrir el mismo
    Entradas: lista: la lista de objetos con todas las licencias
    tipoLicencia: el tipo de licencia del que se hará el reporte
    Salidas: NA
    """
    tipoLicencia = tipoLicencia.get()
    try:
        if not validarVacio(tipoLicencia):
            messagebox.showwarning(title=tittle, message="Debe seleccionar una opción.")
        else:
            reporteFichaCorta("reporte_licencia_tipo"+tipoLicencia+"_"+generarFechaExp()+".xlsx",sacarTipoLicencia(tipoLicencia,lista),"Por tipo de licencia ")
            messagebox.showinfo(title=tittle, message="Se ha creado el reporte")
            abrirFile("reporte_licencia_tipo"+tipoLicencia+"_"+generarFechaExp()+".xlsx", "ReportesExcel")
    except:
        messagebox.showwarning(title=tittle, message="No se puede crear el reporte, cierre el archivo abierto!")
        
def reporteExamenPorSancionES(lista):
    """
    Funcionamiento: se encarga de crear el reporte de los que necesitan repetir el examen y abrir el mismo
    Entradas: lista: la lista de objetos con todas las licencias
    Salidas: NA
    """
    try:
        reporteFichaDeCuatro("reporte_examen_sancion_"+generarFechaExp()+".xlsx",sacarExamenPorSancion(lista), "Examen por sanción ")
        messagebox.showinfo(title=tittle, message="Se ha creado el reporte")
        abrirFile("reporte_examen_sancion_"+generarFechaExp()+".xlsx", "ReportesExcel")
        
    except:
        messagebox.showwarning(title=tittle, message="No se puede crear el reporte, cierre el archivo abierto!")

def reporteDonanteOrganosES(lista):
    """
    Funcionamiento: se encarga de crear el reporte de las personas donantes de organos y abrir el mismo
    Entradas: lista: la lista de objetos con todas las licencias
    Salidas: NA
    """
    try:
        reporteFichaCorta("reporte_donante_organo_"+generarFechaExp()+".xlsx",sacarDonatesOrganos(lista),"Los donantes de órganos")
        messagebox.showinfo(title=tittle, message="Se ha creado el reporte")
        abrirFile("reporte_donante_organo_"+generarFechaExp()+".xlsx", "ReportesExcel")
        
    except:
        messagebox.showwarning(title=tittle, message="No se puede crear el reporte, cierre el archivo abierto!")

def reporteLicenciaAnuladaES(lista):
    """
    Funcionamiento: se encarga de crear el reporte de las personas con licencia anulada y abrir el mismo
    Entradas: lista: la lista de objetos con todas las licencias
    Salidas: NA
    """
    try:
        reporteFichaPuntaje("reporte_licencias_anuladas"+generarFechaExp()+".xlsx",sacarLicenciasAnuladas(lista), "Licencia anulada")
        messagebox.showinfo(title=tittle, message="Se ha creado el reporte")
        abrirFile("reporte_licencias_anuladas"+generarFechaExp()+".xlsx", "ReportesExcel")
        
    except:
        messagebox.showwarning(title=tittle, message="No se puede crear el reporte, cierre el archivo abierto!")

def reportePorSedeES(sede,lista):
    """
    Funcionamiento: se encarga de crear el reporte por sede
    Entradas: lista: la lista de objetos con todas las licencias
    Salidas: NA
    """
    sede = sede.get()
    try:
        if not validarVacio(sede):
            messagebox.showwarning(title=tittle, message="Debe seleccionar una opción.")
        else:
            reporteFichaLarga("reporte_por_sede"+generarFechaExp()+".xlsx",sacarPorSede(lista, traducirSede(sede)), "Licencias por sede ")
            messagebox.showinfo(title=tittle, message="Se ha creado el reporte")
            abrirFile("reporte_por_sede"+generarFechaExp()+".xlsx", "ReportesExcel")
    except:
        messagebox.showwarning(title=tittle, message="No se puede crear el reporte, cierre el archivo abierto!")