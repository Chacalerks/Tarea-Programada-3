#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

import tkinter as tk
from tkinter import IntVar, StringVar, ttk, messagebox
from tkinter.constants import E, LEFT
from general import *
from validaciones import *
from funciones import *
from archivo import*

def eliminarES(mainFrame,corazon_img,matriz):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario eliminar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame) -corazon_img: imagen para volver al menu -Matriz: base de datos
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    cedula = StringVar()
    
    tk.Label(grupo, text="Eliminar Donador ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2,padx=10,sticky=E)
    #Cédula
    tk.Label(grupo, text="Cédula: ",width=10,font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10,sticky=E)
    cedula_txt = ttk.Entry(grupo,textvariable=cedula, width=50)
    cedula_txt.grid(row=1, column=1, pady=10,padx=10)

    justificacion = IntVar()
    justificacion.set(0)
    justificaciones ="\n\
    1.Su peso bajó a menos de 50 kgms\n\n\
    2.No se puede donar sangre si la persona ha sido trasplantada,\n\
    es decir, ha recibido un trasplante de órgano.\n\n\
    3.Enfermedades como: tuberculosis, cáncer o cualquier enfermedad coronaria.\n\n\
    4.Si el donante esadicto a ningún tipo de droga.\n\n\
    5.Padecióhepatitis B o C. \n\n\
    6.Si has padecido de mal de Chagas no puedes donar."
    #Justificacion
    tk.Label(grupo, text="Justificación: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black", width=10).grid(row=3, column=0, pady=10,padx=10,sticky=E)
    justificacion_cbo = ttk.Combobox(grupo,textvariable=justificacion, width=47, state="readonly")
    justificacion_cbo['values']= [1,2,3,4,5,6]
    justificacion_cbo.grid(row=3, column=1, pady=10,padx=10)
    
    #Label justificaciones
    tk.Label(grupo, text=justificaciones,font="BahnschriftLight 12",justify=LEFT, bg=color["fondo"],fg="black").grid(row=4, column=0, columnspan=2, pady=10,padx=10,sticky=E)
    
    buscar_btn = ttk.Button(grupo, text="Eliminar",width=40,padding=20, command=lambda:eliminarDonador(justificacion,matriz,cedula))
    buscar_btn.grid(row=5, column=1,padx=5, pady=35)   

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)

def eliminarDonador(justificacion,matriz,cedula):
    """
    Funcionamiento: Se encarga de validar los datos.
    Entradas: -justificacion: La justificacion -cedula: id de la persona -Matriz: base de datos
    Salidas: -messagebox con respuestas o confirmaciones
    """
    cedula=cedula.get()
    justificacion=justificacion.get()
    datos = obtenerDatosDonador(cedula,matriz)
    if not validarExistente(cedula,matriz):
        messagebox.showwarning(title=tittle, message="No se ha encontrado la cédula")
    elif not enteroMayorCero(justificacion):
        messagebox.showwarning(title=tittle, message="Debe escoger una opción válida")
    elif messagebox.askquestion(title=tittle, message="¿Desea continuar?") == "yes":
        datos[8] = 0
        datos[9] = justificacion
        actulizarDonador(datos,matriz) # Crear la función que devuelve los datos buscados
        guardarDatos('datos',matriz)
        messagebox.showinfo(title=tittle, message="Cambios realizados correctamente")
