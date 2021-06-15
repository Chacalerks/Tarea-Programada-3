#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización: 13/06/2021 10:10 p.m
#Última modificación: 
#Versión: 3.9.5
"""
DOCUMENTACIÓN
+ Nos parace obsesivo documentar cada función por eso un comentario genral que los sepra ya que cada función se explica por sí misma
"""
from datetime import datetime
import time
import random

class Licencia():
####### Inicialización de la Clase
    def __init__(self,cedula, nombre, fechaNac, fechaEx, fechaVenci, tipoLicencia, tipoSangre, donador, sede, puntaje, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.fechaNac = fechaNac
        self.fechaEx = fechaEx
        self.fechaVenci = fechaVenci
        self.tipoLicencia = tipoLicencia
        self.tipoSangre = tipoSangre
        self.donador = donador
        self.sede = sede
        self.puntaje = puntaje
        self.correo = correo

####### Los métodos Setters para cada atributo  
    def setCedula(self,cedula): 
            self.cedula = cedula
    def setNombre(self,nombre):
            self.nombre = nombre
    def setFechaNac(self,fechaNac):
            self.fechaNac = fechaNac
    def setFechaEx(self,fechaEx):
            self.fechaEx = fechaEx
    def setFechaVenci(self,fechaVenci):
            self.fechaVenci = fechaVenci
    def setTipoLicencia(self,tipoLicencia):
            self.tipoLicencia = tipoLicencia
    def setTipoSangre(self,tipoSangre):
            self.tipoSangre = tipoSangre
    def setDonador(self,donador):
            self.donador = donador
    def setSede(self,sede):
            self.sede = sede
    def setPuntaje(self,puntaje):
            self.puntaje = puntaje
    def setCorreo(self,correo):
            self.correo = correo
####### Los métodos Getters para cada atributo        
    def getCedula(self): 
        return self.cedula
    def getNombre(self):
            return self.nombre
    def getFechaNac(self):
            return self.fechaNac
    def getFechaEx(self):
            return self.fechaEx
    def getFechaVenci(self):
            return self.fechaVenci
    def getTipoLicencia(self):
            return self.tipoLicencia
    def getTipoSangre(self):
            return self.tipoSangre
    def getDonador(self):
            return self.donador
    def getSede(self):
            return self.sede
    def getPuntaje(self):
            return self.puntaje
    def getCorreo(self):
            return self.correo

###### Get genral de los datos completos.
    def mostrarDatos(self):
        return self.cedula, self.nombre, self.fechaNac, self.fechaEx, self.fechaVenci, self.tipoLicencia, self.tipoSangre, self.donador, self.sede,  self.puntaje, self.correo

def generarFechaExp():
    """
    funcionamiento: genera la fecha de hoy
    entradas: N/A
    salidas: la fecha de hoy en string
    """
    return time.strftime('%d/%m/%Y', time.localtime())

def convertirFechaAnnos(fecha):
    annos = int(generarFechaExp()[6:]) - int(fecha[6:])
    return annos

#print(convertirFechaAnnos("06/10/2002"))

def generarFechaVenc(edad):
    if edad >= 18 and edad <= 25:
        edadVen = generarFechaExp()[0:6] + str(int(generarFechaExp()[6:])+3)
    else:
        edadVen = generarFechaExp()[0:6] + str(int(generarFechaExp()[6:])+5)
    return edadVen

#print(generarFechaVenc(33))

def generarTipoLicencia(tiposLicencias):
    return random.choice(tiposLicencias)

#print(generarTipoLicencia(['A1', 'B1', 'B2', 'B3', 'C3']))

def generarTipoSangre():
    return random.choice(["O", "A", "B", "AB"])+random.choice("-+")\
            
#print(generarTipoSangre())

def traducirLugar(lugar):
    """
    funcionamiento: Traduce el lugar según corresponsa con tilde  no 
    entradas: lugar: lugar a traducir
    salidas: Traduccion
    """
    lugares = ['San José, San Sebastián','Montecillos Alajuela','Tránsito Cartago','Barva de Heredia','Tránsito San Ramón','Guapiles, Ruta 32',
               'Barrio Sandoval de Moín','Carretera al Aeropuerto Daniel Oduber','Aeropuerto de Nicoya','Chacarita, Calle 138','Pérez Zeledón',
               'Río Claro de Golfito','San Carlos']
    if lugar.isdigit():
        return lugares[int(lugar)]
    else:
        return str(lugares.index(lugar))

#print(traducirLugar('Río Claro de Golfito'))