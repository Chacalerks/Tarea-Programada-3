#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización: 13/06/2021 10:10 p.m
#Última modificación: 
#Versión: 3.9.5
"""
DOCUMENTACIÓN
+ Nos parace obsesivo documentar cada función por eso un comentario general que los separa ya que cada función se explica por sí misma
"""

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
###### Get general de los datos completos.
    def mostrarDatos(self):
        return self.cedula, self.nombre, self.fechaNac, self.fechaEx, self.fechaVenci, self.tipoLicencia, self.tipoSangre, self.donador, self.sede,  self.puntaje, self.correo
