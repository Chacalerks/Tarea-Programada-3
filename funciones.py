#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:06/05/2021 07:21 p.m
#Última modificación:24/05/2021 1:20  a.m
#Versión: 3.9.5

from validaciones import *
import names
import random
from datetime import datetime
import string
from dateutil.relativedelta import relativedelta
import time
from dominate.tags import *
from archivo import *
from clase import *
import webbrowser

def determinarPar(num):
    """
    Funcionamiento: Determina si el número es par
    Entradas:
    -num(int): número a válidar
    Salidas: 
    -True: si es par
    -False: si no es par
    """
    if num % 2 ==0:
        return True
    else:
        return False

def obtenerHoraActual():
    """
    funcionamiento: Se encarga de obtner la hora actual
    entradas: Na
    salidas: Hora Actual
    """
    return datetime.now().time().strftime('%H:%M:%S')

def convertirFechaAnnos(fecha):
    """
    funcionamiento: convierte una fecha de nacimiento a los annos que debe tener esa persona
    entradas: fecha: la fecha de nacimiento
    salidas: los annos que debe tener la persona que nacio en esa fecha
    """
    annos = int(generarFechaExp()[6:]) - int(fecha[6:])
    return annos

def randomEmail(y):
       email = ''.join(random.choice(string.ascii_lowercase) for x in range(y))
       return email + random.choice(["@gmail.com","@costarricense.cr","@racsa.go.cr","@ccss.sa.cr"])

def str_time_prop(start, end, time_format, prop):
    """
    funcionamiento: genera una fecha aleatoria entre dos fechas dadas
    entradas: start: la fecha inicial
    end: la fecha futura
    time_format: el formato de la fecha
    prop: numero aleatorio para sacar la fecha
    salidas: la fecha aleatoria
    """
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def randomDate(start, end, prop):
    return str_time_prop(start, end, '%d-%m-%Y', prop)

def generarRangoFecha():
    fechaMin = (datetime.today() + relativedelta(years=-18)).strftime('%d-%m-%Y')
    fechaMax = (datetime.today() + relativedelta(years=-50)).strftime('%d-%m-%Y')
    return [fechaMax,fechaMin]
    

def generarLicencias(cant, tiposLicencias, lista):
    cant = int(cant)
    while cant != 0:
        insertarLicencia(randomLicencia(tiposLicencias),lista)
        cant-=1
    
def randomLicencia(tiposLicencias):
    """
    funcionamiento: genera una licencia con informacion aleatoria
    entradas: tiposLicencias: los subtipos de licencias
    salidas: el objeto licencia con los datos
    """
    licencia = [generarCedula(), generarNombre(), generarFechaNacimiento(), generarFechaExp()]
    licencia.append(generarFechaVenc(convertirFechaAnnos(licencia[2])))
    licencia.append(generarTipoLicencia(tiposLicencias))
    licencia.append(generarTipoSangre())
    licencia.append(generarDonador())
    licencia.append(generarSede(licencia[0][0]))
    licencia.append(generarPuntaje())
    licencia.append(generarCorreo(licencia[1]))
    licencia1 = Licencia(licencia[0],licencia[1],licencia[2],licencia[3],licencia[4],licencia[5],licencia[6],licencia[7],licencia[8],
                         licencia[9], licencia[10])
    return licencia1
    
def generarCedula():
    """
    funcionamiento: genera un numero de cedula aleatorio
    entradas: N/A
    salidas: un numero de cedula aleatorio
    """
    cedula = str(random.randint(1,9))+str(random.randint(1000,9999))+str(random.randint(1000,9999))
    return cedula

def generarNombre():
    """
    funcionamiento: genera un nombre aleatorio 
    entradas: N/A
    salidas: un nombre aleatorio
    """
    nombre = names.get_full_name()+" "+names.get_last_name()
    return nombre

def generarFechaNacimiento():
    """
    funcionamiento: genera una fecha de nacimiento aleatoria
    entradas: N/A
    salidas: un nombre aleatorio
    """
    dob = randomDate(generarRangoFecha()[0], generarRangoFecha()[1], random.random())
    return dob

def generarFechaExp():
    """
    funcionamiento: genera la fecha de hoy
    entradas: N/A
    salidas: la fecha de hoy en string
    """
    return time.strftime('%d-%m-%Y', time.localtime())

def generarFechaVenc(edad):
    """
    funcionamiento: genera la fecha de vencimiento de la licencia dependiendo de su edad
    entradas: la edad de la persona aplicando para la licencia
    salidas: la fecha de vencimiento
    """
    if edad >= 18 and edad <= 25:
        edadVen = generarFechaExp()[0:6] + str(int(generarFechaExp()[6:])+3)
    else:
        edadVen = generarFechaExp()[0:6] + str(int(generarFechaExp()[6:])+5)
    return edadVen

def generarTipoLicencia(tiposLicencias):
    """
    funcionamiento: retorna un tipo de licencia aleatorio
    entradas: la lista con los tipos de licencias
    salidas: el tipo escogido de manera aleatoria
    """
    return random.choice(tiposLicencias)

def generarTipoSangre():
    """
    funcionamiento: retorna un tipo de sangre aleatorio
    entradas: N/A
    salidas: el tipo escogido de manera aleatoria
    """
    return random.choice(["O", "A", "B", "AB"])+random.choice("-+")

def generarDonador():
    """
    funcionamiento: retorna un valor booleano aleatorio
    entradas: N/A
    salidas: el tipo escogido de manera aleatoria
    """
    return random.choice([True, False])

def traducirSede(sede):
    """
    funcionamiento: Traduce el sede según corresponda
    entradas: sede: sede a traducir
    salidas: Traduccion del sede
    """
    sedes = ['San José, San Sebastián','Montecillos Alajuela','Tránsito Cartago','Barva de Heredia','Tránsito San Ramón','Guapiles, Ruta 32',
               'Barrio Sandoval de Moín','Carretera al Aeropuerto Daniel Oduber','Aeropuerto de Nicoya','Chacarita, Calle 138','Pérez Zeledón',
               'Río Claro de Golfito','San Carlos']
    try:
        if sede.isdigit():
            return sedes[int(sede)]
        else:
            return str(sedes.index(sede))
    except:
        return sede

def traducirSedeReporte(lista):
    """
    funcionamiento: itera sobre una lista ejecutando la función que traduce las sedes y devuelve un string con las sedes traducidas
    entradas: lista: la lista con las sedes
    salidas: el string con las sedes
    """
    salida = ""
    for i in lista:
        salida+= traducirSede(i) +"|"
    return salida
    
def generarSede(id):
    """
    funcionamiento: retorna una sede aleatoria con respecto a la cedula
    entradas: N/A
    salidas: la sede escogida
    """
    if id in ['1','8','9']:
        return ['0','10']
    elif id == '2':
        return ['1','4','12']
    elif id == '3':
        return ['2']
    elif id == '4':
        return ['3']
    elif id == '5':
        return ['7','8']
    elif id == '6':
        return ['9','11']
    else:
        return ['5','6']

def generarPuntaje():
    """
    funcionamiento: genera un numero entre 0 y 12, que representa el puntaje
    entradas: N/A
    salidas: el puntaje
    """
    return random.randint(0,12)

def generarCorreo(nombre):
    """
    funcionamiento: genera un correo electrónico basado en el nombre de la persona
    entradas: nombre: el nombre de la persona
    salidas: el correo
    """
    partes = nombre.split()
    return (partes[1]+partes[2][0]+partes[0][0]).lower() + "@gmail.com"

def obtenerPosicion(cedula, lista):
    """
    funcionamiento: retorna la posicion del objeto en la lista con la cedula especificada
    entradas: cedula: la cedula a buscar
    salidas: la posicion del objeto en la lista con la cedula especificada 
    """
    for i in lista:
        if cedula == i.getCedula():
            return lista.index(i)
    return False

def traducirDonador(donador):
    """
    funcionamiento: dependiendo del valor booleano, retorna si o no para donador
    entradas: donador: el valor booelano
    salidas: Si: en caso de que donador sea True
    No: en caso de que el valor booleano sea False
    """
    if donador == True:
        return 'Si'
    else:
        return 'No'
    
def abrirPage(nombreFile):
    webbrowser.open_new_tab(nombreFile)
#----------------------------------------------------------------------------#
#                           Base de datos                                    #
#----------------------------------------------------------------------------#
def insertarLicencia(objeto,lista):
    """
    funcionamiento: inserta el objeto generado a la lista
    entradas: objeto: el objeto de la clase Licencia
    lista: la lista con los objetos
    salidas: el objeto licencia con los datos
    """
    lista.append(objeto)
    return lista

def renovarLicencia(posicion, lista):
    """
    Funcionamiento: Se encarga actuallizar a un donador.
    Entradas: -datos: datos del donador matriz: matriz en el que se va a guardar
    Salidas: NA
    """
    fecha = lista[posicion].getFechaVenci()
    annos = convertirFechaAnnos(lista[posicion].getFechaNac())
    if annos >= 18 and annos <= 25:
        fecha = fecha[0:6] + str(int(fecha[6:])+3)
    else:
        fecha = fecha[0:6] + str(int(fecha[6:])+5)
    lista[posicion].setFechaVenci(fecha)
    

#----------------------------------------------------------------------------#
#                           Provincias                                       #
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
#                           Reportes                                         #
#----------------------------------------------------------------------------#

#Procesamiento
def reporteFichaLarga(nombreArch,lista):
    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Cédula'
    sheet['B1'] = 'Nombre'
    sheet['C1'] = 'FechaNac'
    sheet['D1'] = 'FechaExp'
    sheet['E1'] = 'FechaVenc'
    sheet['F1'] = 'TipoLicen'
    sheet['G1'] = 'TipoSangre'
    sheet['H1'] = 'Donador'
    sheet['I1'] = 'Sede'
    sheet['J1'] = 'Puntaje'
    cont = 2
    for i in lista:
        sheet['A'+str(cont)] = i.getCedula()
        sheet['B'+str(cont)] = i.getNombre()
        sheet['C'+str(cont)] = i.getFechaNac()
        sheet['D'+str(cont)] = i.getFechaEx()
        sheet['E'+str(cont)] = i.getFechaVenci()
        sheet['F'+str(cont)] = i.getTipoLicencia()
        sheet['G'+str(cont)] = i.getTipoSangre()
        sheet['H'+str(cont)] = traducirDonador(i.getDonador())
        sheet['I'+str(cont)] = traducirSedeReporte(i.getSede())
        sheet['J'+str(cont)] = i.getPuntaje()
        cont+=1
            
    workbook.save(nombreArch)