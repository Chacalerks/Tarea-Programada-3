#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización: 13/06/2021 10:10 p.m
#Última modificación: 
#Versión: 3.9.5



import xml.etree.cElementTree as ET

from xml.dom import minidom
import requests
from bs4 import BeautifulSoup

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

def obtenerTiposLicencias(): 
    #Obtiene los tipos de lincencias
    for i in soup.findAll('h2'): 
        if i.text != "":
            tipos.append(i.text)
        #print(i.text)

def obtenerSubTipo():
    #Obtiene un array de los subtipos de licencias y los comentarios de esta
    filaTipos = []
    filaComentario = []
    caracter = "A"
    for i in soup.findAll('h3'):
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
    #Obtiene un array de los requisitos de las licencias
    temp = 0
    cont = 0
    filaRequisitos = [] 
    for i in soup.findAll('ul'):
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
    #Esta función crea el archivo de XML a partir de la variables globales de arriba
    root = ET.Element("ArchivoLicencias")
    cont = 0
    for i in tipos:
        tipoLicenciaET = ET.SubElement(root, "TipoLicencia")
        NombreTipo = ET.SubElement(tipoLicenciaET, "Nombre")
        NombreTipo.text = i
        for j in subtipos[cont]:
            #nombre del Subtipo
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


    print(len(tipos), len(subtipos), len(comentarios), len(requisistos))
    ET.SubElement(tipoLicenciaET, "nodo2", atributo="algo").text = "texto 2"
    arbol = ET.ElementTree(root)
    arbol.write("./licencia.xml")

obtenerTiposLicencias()
obtenerSubTipo()
obtenerRequisitos()
crearXML()


def leerXML():
    lista = []
    with open('licencia.xml', 'r') as f:
        data = f.read()
    Bs_data = BeautifulSoup(data, "xml")
    NombreSubTipo = Bs_data.find_all('NombreSubTipo')
    for i in NombreSubTipo:
        lista.append(i.text[9:][:2])
    return lista

lista = leerXML()
print(lista)