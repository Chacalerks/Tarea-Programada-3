#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

import re
from datetime import datetime
"""
DOCUMENTACIÓN
+ Solo se decidó validar el formata de la fecha, ya que en las instrucciones no especifica ¿qué? exactamente

"""
#----------------------------------------------------------------------------
#                      Validaciones de Ingresar y Actualizar
#----------------------------------------------------------------------------

def validarEntero(num):
    """
    Funcionamiento: Determina si el número es connveritble a  un entero
    Entradas:
    -num(string): Una cadena de texto con la posibilidad de ser entero
    Salidas: 
    -True si el número sí es entero
    -'a' si el número no fuese entero. 
    """
    try:
        num = int(num)
        if num > 0:
            return True
    except ValueError:
        return False
        
def validarVacio(texto):
    """
    Funcionamiento: Determina si la valiarble es vacía
    Entradas: texto(string): la varaiable a validar 
    Salidas: True/False de la condición dada (texto vacío)
    """
    if texto!="":
        return True
    else:
        return False

def enteroMayorCero(num):
    """
    Funcionamiento: Determina si el número mayor a cero
    Entradas: num(int): el número a válidar
    Salidas: True/Fase de la condición dada (mayor a cero)
    """
    if num >0:
        return True
    else:
        return False

def validarNombre(nombre):
    """
    funcionamiento: Se encarga de validar que el nombre ingresado por el usuario sea válido
    entradas: nombre: elnombre del donador a validar
    salidas: true/false según la condición dada (nombre válido)
    """
    if re.match("^[a-zA-Z]+\ [a-zA-Z]+\ (([a-zA-Z]+\ [a-zA-Z]+)|[a-zA-Z]+)$", nombre):
        return True
    else:
        return False
    
def validarCedula(id):
    """
    funcionamiento: Se encarga de validar que el numero de cedula ingresado por el usuario sea válido
    entradas: id: la cedula del donador a validar
    salidas: True: si la cédula SÍ es válida 
    False: si la cédula NO es válida
    """
    if re.match("^[1-9]\d{8}$",id):
        return True
    else:
        return False

def validarFormatoFecha(dob):
    """
    funcionamiento: Se encarga de validar que la fecha de nacimiento del donante sea válida
    entradas: dob: la fecha de nacimiento del donante
    salidas: True: si la fecha SÍ es válida 
    False: si la fecha NO es válida
    """
    if re.match("^(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](19[0-9][0-9]|20[0-9][0-9])$", dob):
        try:
            datetime.strptime(dob, '%d-%m-%Y')
            return True
        except ValueError:
            return False
    else:
        return False

def validarPuntajeFormato(puntaje):
    """
    funcionamiento: se encarga de validar que el puntaje sea entre 12 y 0
    salidas:true/false de la condición dada (puntaje entre 12 y 0)
    """
    if re.match("^[0-9]$|^(1[0-2])$",str(puntaje)):
        return True
    else:
        return False


def validarCorreo(nombre, correo):
    """
    funcionamiento: Se encarga de validar que la el correo electronico del donador sea valido
    entradas: correo: el correo electronico del donador
    salidas: True: si el correo SÍ es válida 
    False: si el correo NO es válida
    """
    partes = nombre.split()

    if re.match("^("+(partes[1]+partes[2][0]+partes[0][0]).lower()+"@gmail.com)$",correo):
        return True
    else:
        return False


def validarExistente(id, matriz):
    """
    funcionamiento: Se encarga de validar que el donador no haya sido ingresado ya
    entradas: id: numero de cedula del donador
    salidas: True: si el donador SI se encuentra ya en la base de datos
    False: si el donador NO se encuentra en la base de datos
    """
    for i in matriz:
        if id == i.getCedula():
            return True
    return False

def validarPuntaje(posicion, lista):
    """
    funcionamiento: analiza el puntaje del conductor y devuelve distintas salidas dependiendo del puntaje
    entradas: posicion: la posicion de la licencia a analizar
    salidas: True: si la licencia si puede ser renovada
    a: si la licencia no puede ser renovada, pero debe hacer el examen teorico de nuevo
    False: si la licencia no puede volver a ser renovada nunca
    """
    if lista[posicion].getPuntaje() > 6:
        return True
    elif lista[posicion].getPuntaje() > 0 and lista[posicion].getPuntaje() <= 6:
        return 'a'
    else:
        return False