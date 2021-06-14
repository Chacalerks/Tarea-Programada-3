#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

import re
from datetime import datetime
#----------------------------------------------------------------------------
#                      Validaciones de Ingresar y Actualizar
#----------------------------------------------------------------------------
"""
Documentación IMPORTANTE:
+En las intrucciones no decía especificamente el rango de edades para donar, solo referenciaba a un artículo y en este decía que solo en los que los donante no esta 
    en buenas condiciones de salud no pueden continuar donando con más de 60 años, por lo que decidimos limitarlo a 65 años.
"""
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
    if re.match("^\d\-\d{4}\-\d{4}$",id):
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
    year = dob[-4:]
    moth = dob[3:6]
    day = dob[:3]
#^(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19[0-9][0-9]|20[0-9][0-9])$"

    if re.match("^(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[/](19[0-9][0-9]|20[0-9][0-9])$", dob):
        try:
            datetime.strptime(dob, '%d/%m/%Y')
            return True
        except ValueError:
            return False
    else:
        return False

print(validarFormatoFecha("12/08/2030"))
def validarEdad(dob):
    """
    funcionamiento: se encarga de validar que el donante sea mayor a 18 años
    entradas: la fecha del donante
    salidas: true: si el donante es mayor de edad
    False: si el donante NO es mayor de edad
    """
    fecha = datetime.strptime(dob, '%d/%m/%Y')
    resta = datetime.now() - fecha
    resta = resta.days
    if resta >= 6575 and resta < 23725+16:
        return True
    else:
        return False


def validarCorreo(correo):
    """
    funcionamiento: Se encarga de validar que la el correo electronico del donador sea valido
    entradas: correo: el correo electronico del donador
    salidas: True: si el correo SÍ es válida 
    False: si el correo NO es válida
    """
    if re.match("^[a-z0-9]+[\.'\-a-z0-9_]*[a-z0-9]+@(gmail.com|costarricense.cr|racsa.go.cr|ccss.sa.cr)$",correo.lower()):
        return True
    else:
        return False

def validarTelefono(telefono):
    """
    funcionamiento: Se encarga de validar que el numero de telefono del donador sea valido
    entradas: correo: el numero de telefono del donador
    salidas: True: si el numero de telefono SÍ es válida 
    False: si el numero de telefono NO es válida
    """
    if re.match("^\d{4}\-\d{4}$",telefono):
        return True
    else:
        return False
        
def validarPeso(peso):
    """
    funcionamiento: Se encarga de validar que el peso del donador sea valido
    entradas: correo: el peso del donador
    salidas: True: si el peso SÍ es válida 
    False: si el peso NO es válida
    """
    try:
        if peso > 50 and peso < 120:
            return True
        else:
            return False   
    except:
        return False

def validarExistente(id, matriz):
    """
    funcionamiento: Se encarga de validar que el donador no haya sido ingresado ya
    entradas: id: numero de cedula del donador
    salidas: True: si el donador SI se encuentra ya en la base de datos
    False: si el donador NO se encuentra en la base de datos
    """
    for i in matriz:
        if id == i[0]:
            return True
    return False

def validarRangoEdad(edad):
    """
    funcionamiento: Se encarga de validar la edad que el usuario ingrese de un donante en los reportes
    entradas: edad: la edad que haya ingresado
    salidas: True: si la edad SI es igual o mayor a 18 y menor o igual a 60
    False: si la edad NO es mayor a 18 o si la edad es mayor a 60
    """
    try:
        if int(edad) >= 18 and int(edad) < 65:
            return True
        else:
            return False
    except:
        return False
    
def validarEdades(edad1,edad2):
    """
    funcionamiento: Se encarga de validar la edad que el usuario ingrese de un donante en los reportes
    entradas: edad: la edad que haya ingresado
    salidas: True: si la edad SI es igual o mayor a 18 y menor o igual a 60
    False: si la edad NO es mayor a 18 o si la edad es mayor a 60
    """
    try:
        if int(edad1) <= int(edad2):
            return True
        else:
            return False
    except:
        return False