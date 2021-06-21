#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización: 13/06/2021 10:10 p.m
#Última modificación: 
#Versión: 3.9.5

import xml.etree.cElementTree as ET
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
from general import *
from funciones import *
from tkinter import messagebox

#obtiene el html de la web page
url = "https://practicatest.cr/blog/licencias/tipos-licencia-conducir-costa-rica"
page = requests.get(url)
contenido = page.content
soup = BeautifulSoup(contenido, "html.parser")

# Declaración de variables Globales para almacenar el XML
tipos = []
subtipos = []
comentarios = []
requisistos = []

def limpiarVariables():
    """
    Funcionamiento: Se encarga de limpiar la variables para volver a crear un XML
    Entradas: NA
    Salidas: Variables reiniciadas
    """
    for i in range(0,len(tipos)):
        tipos.pop(0)
    for i in range(0,len(subtipos)):
        subtipos.pop(0)
    for i in range(0,len(comentarios)):
        comentarios.pop(0)
    for i in range(0,len(requisistos)):
        requisistos.pop(0)

def obtenerTiposLicencias(): 
    """
    Funcionamiento: Se encarga de obtener los h2 de la pagina web
    Entradas: NA
    Salidas: Lista de tipos de licencias
    """
    for i in soup.findAll('h2'): 
        print(i)
        if i.text != "":
            tipos.append(i.text)

def obtenerSubTipo():
    """
    Funcionamiento: Se encarga de obtener los h3 y los comentarios de la pagina web
    Entradas: NA
    Salidas: Lista de subtipos y el comentario de esta
    """
    filaTipos = []
    filaComentario = []
    caracter = "A"
    for i in soup.findAll('h3'):
        print(i)
        if "Licencia" in i.text and i.text != "":
            if i.text[9:][:2][0] != caracter:
                subtipos.append(filaTipos)
                comentarios.append(filaComentario)
                filaTipos = []
                filaComentario = []       
            if i.text[-1] == "\n":
                filaTipos.append(i.text[:-1])
            else:
                filaTipos.append(i.text)
            # Este if comienza a guardar los comentarios de cada subtipo
            if i.next_sibling.text[-1] == "\n":
                filaComentario.append(i.next_sibling.text[:-1])
            else:
                filaComentario.append(i.next_sibling.text)
            caracter = i.text[9:][:2][0]
    subtipos.append(filaTipos)
    comentarios.append(filaComentario) 

def obtenerRequisitos():
    """
    Funcionamiento: Se encarga de obtener los requesitos comentarios de la pagina web
    Entradas: NA
    Salidas: Lista de requsitos
    """
    temp = 0
    cont = 0
    filaRequisitos = [] 
    for i in soup.findAll('ul'):
        print(i)
        if cont ==3 or cont == 7 or cont == 9 or cont == 10 or cont==12:
            requisistos.append(filaRequisitos)
            filaRequisitos = [] 
        if temp >= 8:
            if i.text[-1] == "\n":
                filaRequisitos.append(i.text[:-1])
                cont +=1
            else:
                filaRequisitos.append(i.text)
                cont +=1    
        temp+=1
    requisistos.append(filaRequisitos)

def crearXML():
    """
    Funcionamiento: Se encarga de crear el XMl
    Entradas: NA
    Salidas: XMl de las licencias
    """
    root = ET.Element("ArchivoLicencias")
    cont = 0
    print(len(tipos),len(subtipos), len(requisistos))
    for i in tipos:
        tipoLicenciaET = ET.SubElement(root, "TipoLicencia")
        NombreTipo = ET.SubElement(tipoLicenciaET, "Nombre")
        NombreTipo.text = i
        print(i)
        for j in subtipos[cont]:
            #nombre del Subtipo
            print(j)
            subTipoET = ET.SubElement(tipoLicenciaET, "SubTipoLicencia")
            NombreSubTipo = ET.SubElement(subTipoET, "NombreSubTipo")
            NombreSubTipo.text = j

            # Comentario
            comentarioET = ET.SubElement(subTipoET, "Comentario")
            comentarioET.text = comentarios[cont][subtipos[cont].index(j)]

            # Requisitos
            requesitosET = ET.SubElement(subTipoET, "Requisitos")
            if cont == 3: 
                for i in requisistos[cont][0].split("\n"):   
                    requisitoET = ET.SubElement(requesitosET, "Requisito")        
                    requisitoET.text = i
            else:
                for i in requisistos[cont][subtipos[cont].index(j)].split("\n"):   
                    requisitoET = ET.SubElement(requesitosET, "Requisito")        
                    requisitoET.text = i
        cont +=1
    arbol = ET.ElementTree(root)
    arbol.write("licencia.xml")

def crearXML_ES():
    """
    Funcionamiento: Se encarga de la E/S, que llama a todas las funciones de XML
    Entradas: NA
    Salidas: Archivo XML
    """
    limpiarVariables()
    obtenerTiposLicencias()
    obtenerSubTipo()
    obtenerRequisitos()
    crearXML()
    messagebox.showinfo(title=tittle, message="Se creó correctamente el archivo")
    abrirPage("licencia.xml")

def leerXML():
    """
    Funcionamiento: Lee el archivo XMl y obtiene el tipo de lincencia
    Entradas: NA
    Salidas: Lista de licencia
    """
    try:
        lista = []
        with open('licencia.xml', 'r') as f:
            data = f.read()
        Bs_data = BeautifulSoup(data, "xml")
        NombreSubTipo = Bs_data.find_all('NombreSubTipo')
        for i in NombreSubTipo:
            lista.append(i.text[9:][:2])
        return lista
    except:
        messagebox.showwarning(title=tittle, message="No hay ningún archivo .XML para leer.")