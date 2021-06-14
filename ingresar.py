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

def insertarDonadorES(mainFrame,corazon_img,matriz,datos=[],categoria="I",dicc=""):
    """
    Funcionamiento: Se encarga de crear todos lo elementos del formulario insertar.
    Entradas: -mainFrame: mainFrameEl contenedor(frame)
    Salidas: NA
    """
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)

    datos = establecerDatos(datos)
    tk.Label(grupo, text="Eliminar Donador ",font="BahnschriftLight 15", bg=color["fondo"],fg="black", pady=20, padx=20).grid(row=0, column=0, columnspan=2,padx=10,sticky=E)
    #Cédula

    #Cédula
    tk.Label(grupo, text="Cédula: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=0, column=0, pady=10,padx=10,sticky=E)
    cedula_txt = ttk.Entry(grupo,textvariable=datos[0], width=50)
    cedula_txt.grid(row=0, column=1, pady=10,padx=10)

    #Nombre completo
    tk.Label(grupo, text="Nombre completo: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=1, column=0, pady=10,padx=10, sticky=E)
    nombreCompleto_txt = ttk.Entry(grupo,textvariable=datos[1],width=50)
    nombreCompleto_txt.grid(row=1, column=1, pady=10,padx=10)

    #Fecha de Nacimiento
    tk.Label(grupo, text="Fecha de Nacimiento: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=2, column=0, pady=10,padx=10, sticky=E)
    fechaNacimiento_txt = ttk.Entry(grupo,textvariable=datos[2],width=50)
    fechaNacimiento_txt.grid(row=2, column=1, pady=10,padx=10)

    #Tipo de Sangre
    tk.Label(grupo, text="Tipo de Sangre: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=3, column=0, pady=10,padx=10, sticky=E)
    tipoSangre_cbo = ttk.Combobox(grupo,textvariable=datos[3], width=47, state="readonly")
    tipoSangre_cbo['values']= ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    tipoSangre_cbo.grid(row=3, column=1, pady=10,padx=10)

    #Sexo    
    tk.Label(grupo, text="Sexo: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=4,rowspan=2,column=0, pady=10,padx=10, sticky=E)
    sexo_rb1 = ttk.Radiobutton(grupo,variable=datos[4], text="Masculino",value=True, width=45)
    sexo_rb2 = ttk.Radiobutton(grupo,variable=datos[4], text="Femenino",value=False, width=45)
    sexo_rb1.grid(row=4, column=1, pady=10,padx=10)
    sexo_rb2.grid(row=5, column=1, pady=10,padx=10)

    #Peso
    tk.Label(grupo, text="Peso en Kg: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=6, column=0, pady=10,padx=10, sticky=E)
    peso_txt = ttk.Entry(grupo,textvariable=datos[5], width=50)
    peso_txt.grid(row=6, column=1, pady=10,padx=10)

    #Teléfono
    tk.Label(grupo, text="Teléfono: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=7, column=0, pady=10,padx=10, sticky=E)
    telefono_txt = ttk.Entry(grupo,textvariable=datos[6], width=50)
    telefono_txt.grid(row=7, column=1, pady=10,padx=10)

    #Correo
    tk.Label(grupo, text="Correo: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=8, column=0, pady=10,padx=10, sticky=E)
    email_txt = ttk.Entry(grupo,textvariable=datos[7], width=50)
    email_txt.grid(row=8, column=1, pady=10,padx=10)

    ingresar_btn = ttk.Button(grupo, text="Registrar",width=40,padding=20, command=lambda:ingresarDatosValidaciones(mainFrame,corazon_img,datos,matriz,categoria,dicc))
    ingresar_btn.grid(row=9, column=0,padx=5, pady=35)

    limpiar_btn = ttk.Button(grupo, text="Limpiar",width=40,padding=20, command=lambda:limpiarCampos(datos))
    limpiar_btn.grid(row=9, column=1,padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0,command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=300,  sticky=E)
    
    if categoria !="I":
        ingresar_btn.configure(text="Actualizar")
        cedula_txt.configure(state="readonly")
        regresar_btn.configure(command=lambda:actulizarDonadorES(mainFrame, corazon_img, matriz))
        

def actulizarDonadorES(mainFrame,corazon_img,matriz):
    limpiarFrame(mainFrame)
    grupo = tk.Frame(mainFrame, bg=color["fondo"],padx= 30, pady=60)
    grupo.pack(fill=tk.BOTH,expand=1)
    cedula = StringVar()
    #Cédula
    tk.Label(grupo, text="Cédula: ",font="BahnschriftLight 12", bg=color["fondo"],fg="black").grid(row=0, column=0, pady=10,padx=10,sticky=E)
    cedula_txt = ttk.Entry(grupo,textvariable=cedula, width=50)
    cedula_txt.grid(row=0, column=1, pady=10,padx=10)

    buscar_btn = ttk.Button(grupo, text="Buscar",width=40,padding=20, command=lambda:buscarCedula(mainFrame,corazon_img,matriz,cedula))
    buscar_btn.grid(row=2, column=1,padx=5, pady=35)

    regresar_btn = tk.Button(grupo, text="< Regresar", font="Bahnschrift 15", fg="gray17",bd=0, command=lambda:cargarInicio(mainFrame,corazon_img))
    regresar_btn.grid(row=0,rowspan=2, column=2, columnspan=2, pady=10,padx=450,  sticky=E)

def buscarCedula(mainFrame,corazon_img,matriz,cedula):
    cedula=cedula.get()
    if validarExistente(cedula,matriz):
        print(obtenerDatosDonador(cedula,matriz))
        insertarDonadorES(mainFrame,corazon_img,matriz,obtenerDatosDonador(cedula,matriz),"asdf") # Crear la función que devuelve los datos buscados


    
def ingresarDatosValidaciones(mainFrame,corazon_img,datos,matriz,categoria,dicc):
    
    datosString=obtenerDatos(datos)
    print(datosString)    
    if not validarCedula(datosString[0]):
        messagebox.showwarning(title=tittle, message="Formato de cédula incorrecto")
    elif validarExistente(datosString[0],matriz) and categoria =="I":
        messagebox.showwarning(title=tittle, message="Ya se encuentra un donador registrado con esa cédula")
    elif not validarNombre(datosString[1]):
        messagebox.showwarning(title=tittle, message="Debe de ser el nombre completo")
    elif not validarFormatoFecha(datosString[2]):
        messagebox.showwarning(title=tittle, message="Fecha inválida")
    elif not validarEdad(datosString[2]):
         messagebox.showwarning(title=tittle, message="No tiene la edad adecuada para ser donante")
    elif not validarVacio(datosString[3]):
        messagebox.showwarning(title=tittle, message="Debe selecionar el tipo de sangre")
    elif not validarPeso(datosString[5]):
        messagebox.showwarning(title=tittle, message="Peso no apto para un donador")
    elif not validarTelefono(datosString[6]):
        messagebox.showwarning(title=tittle, message="Formato incorrecto de número de celular")
    elif not validarCorreo(datosString[7]):
        messagebox.showwarning(title=tittle, message="Formato de correo inválido")
    elif categoria != "I": #Actualizaci[on]
        if messagebox.askquestion(title=tittle, message="¿Desea actualizar los datos?") =="yes":
            completarDatosActualizar(mainFrame,corazon_img,datosString,matriz)
        else:
            messagebox.showinfo(title=tittle, message="No se han actualizado los datos")
    else:
       insertarDonador(datosString, matriz)
       guardarDatos('datos',matriz)
       messagebox.showinfo(title=tittle, message="Se ha registrado correctamente")
       informacionInicial(datosString[3],datosString[0],dicc)
       

def completarDatosActualizar(mainFrame,corazon_img,datosString,matriz):
    
    datosObtenidos =  obtenerDatosDonador(datosString[0],matriz)
    i = 1
    while True:
        datosObtenidos[i]=datosString[i]
        if i==7:
            break
        i+=1
    actulizarDonador(datosObtenidos,matriz)
    guardarDatos('datos',matriz)
    messagebox.showinfo(title=tittle, message="Datos actualizados correctamente")
    cargarInicio(mainFrame,corazon_img)


def informacionInicial(sangre,cedula,dicc):

    info = "Información \n\n+Su sangre es de tipo "+sangre+" ,por esto "+datosSangre(sangre) + "\n\n+" +datosLugares(cedula,dicc)       
    messagebox.showinfo(title="IMPORTANTE", message=info)
    
