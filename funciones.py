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
import webbrowser
import dominate
from dominate.tags import *
from archivo import *

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

def random_date(start, end, prop):
    return str_time_prop(start, end, '%d/%m/%Y', prop)

def generarRangoFecha():
    fechaMin = (datetime.today() + relativedelta(years=-18)).strftime('%d/%m/%Y')
    fechaMax = (datetime.today() + relativedelta(years=-50)).strftime('%d/%m/%Y')
    return [fechaMax,fechaMin]
    

def generarDonadores(cant, matriz):
    cant = int(cant)
    while cant != 0:
        insertarDonador(randomDonador(),matriz)
        cant-=1
    
def randomDonador():
    donador = []
    donador.append(str(random.randint(1,9))+"-"+str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999)))
    m = names.get_full_name(gender='male')
    f = names.get_full_name(gender='female')
    winner = random.choice([m, f])
    donador.append(winner+" "+names.get_last_name())
    donador.append(random_date(generarRangoFecha()[0], generarRangoFecha()[1], random.random()))
    donador.append(random.choice(["O", "A", "B", "AB"])+random.choice("-+"))
    if winner == m:
        donador.append(True)
    else:
        donador.append(False)
    donador.append(random.randint(51,120))
    donador.append(str(random.randint(2000,9999))+"-"+str(random.randint(2000,9999)))
    donador.append(randomEmail(7))
    return donador


def traducirLugar(lugar):
    """
    funcionamiento: Traduce el lugar según corresponsa con tilde  no 
    entradas: lugar: lugar a traducir
    salidas: Traduccion
    """
    traduccion = ["San José","San Jose","Limón","Limon"]
    if lugar in traduccion:
        if determinarPar(traduccion.index(lugar)):
            return traduccion[traduccion.index(lugar)+1]
        else:
            return traduccion[traduccion.index(lugar)-1]
    else:
        return lugar

def obtenerIndexLugar(lugar):
    """
    funcionamiento: Traduce el lugar según el número de cédula
    entradas: lugar: lugar a traducir
    salidas: Traduccion
    """
    traduccion =["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón","San José","San José"]
    return str(traduccion.index(lugar)+1)

def datosSangre(sangre):
    datos = ["se  les  recomienda donar  glóbulos  rojos  dobles  y  sangre entera.",
    "se   recomienda   donar   glóbulos   rojos dobles y sangre entera.",
    "se  les recomienda  que  donen  sangre  entera  y plaquetas.",
    "se   les recomienda  que  donen  sangre  entera  y glóbulos rojos dobles.",
    "sangre  entera  y  de  glóbulos  rojos dobles.",
    "se  les  recomienda  que  donen  sangre entera o plaquetas.",
    "se  les recomienda     hacer     donaciones     de plaquetas y de plasma.",
    "se  lesrecomienda donar plaquetas y plasma."]
    tipo =["O+","O-","A+","A-","B+","B-","AB+","AB-"]
    return datos[tipo.index(sangre)]

def datosLugares(cedula,dicc):
    provincias = ["San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón","San José","San José"]
    return "Dado que usted nació en la provincia de " +provincias[int(cedula[0])-1]+" usted podría donar en: \n"+obtenerLugares(traducirLugar(provincias[int(cedula[0])-1]),dicc)

def obtenerLugares(lugar,dicc):
    lugares = ""
    for i in dicc[lugar]:
        lugares+="\t-"+i+"\n"
    return lugares

def traducirSexo(sexo):
    if sexo == True:
        return "Masculino"
    else:
        return "Femenino"

def traducirJustificacion(justificacion):
    razones = ["Su peso bajó a menos de 50 kgms","El donante recibió un transplante de órgano",
               "Enfermedades como: tuberculosis, cáncer o cualquier enfermedad coronaria.", "El donante es adicto a algún tipo de droga.",
               "Padecióhepatitis B o C","Padeció mal de Chagas"]
    return razones[justificacion-1]
#----------------------------------------------------------------------------#
#                           Base de datos                                    #
#----------------------------------------------------------------------------#
def insertarDonador(datos, matriz):
    """
    funcionamiento: Se encarga insertar el donador en la base de datos con la información correspondiente
    entradas: Datos: los datos ha registrar del donador matriz: variable a guardar
    salidas: la matriz con el nuevo donador
    """
    datos.append(1)
    datos.append(0)
    matriz.append(datos)
    return matriz

def obtenerDatosDonador(cedula, matriz):
    """
    Funcionamiento: Se encarga buscar a un donador.
    Entradas: -cedula: cedula del donador matriz: matriz en el que se va a buscar
    Salidas: Los datos del donardor encontrados
    """
    for i in matriz:
        if i[0] == cedula:
            return matriz[matriz.index(i)]

def actulizarDonador(datos, matriz):
    """
    Funcionamiento: Se encarga actuallizar a un donador.
    Entradas: -datos: datos del donador matriz: matriz en el que se va a guardar
    Salidas: NA
    """
    matriz[matriz.index(datos)] = datos

#----------------------------------------------------------------------------#
#                           Provincias                                       #
#----------------------------------------------------------------------------#
def guardarLugar(datos,dicc):
    """
    Funcionamiento: Se encarga guardar los nuevos lugares.
    Entradas: -datos: datos del lugar dicc: diccionario en el que se va a guardar
    Salidas: NA
    """
    lugares = []
    lugares = dicc[datos[0]]
    lugares.append(datos[1])
    print("esta es la provincia "+datos[0])
    dicc[datos[0]] = lugares

#----------------------------------------------------------------------------#
#                           Reportes                                         #
#----------------------------------------------------------------------------#

#Procesamiento
def sacarDonantesProvincia(provincia,matriz):
    donantes = []
    for i in matriz:
        if i[0][0] == provincia:
            donantes.append(i)
        elif provincia == "1" and (i[0][0] == "8" or i[0][0] == "9"):
            donantes.append(i)
    return donantes

def sacarDonantesRangoEdad(edadIni, edadFin, matriz):
    donantes = []
    for i in matriz:
        year = int(i[2][-4:])
        contadora = 0
        while year <=2021:            
            if determinarBisiestos(year):
                contadora+=1
            year+=1
        fechaNaci = datetime.strptime(i[2], '%d/%m/%Y')
        annos = datetime.today() - fechaNaci
        annos = annos.days
        annos = (annos-contadora) // 365
        if annos >= edadIni and annos <= edadFin:
            print(contadora)
            donantes.append(i)
    return donantes

def determinarBisiestos(annos):
    if annos % 4 == 0:
        if annos % 100 == 0:
            if annos % 400 == 0:
                return True
            else:
                return False
        else:
           return True
    else:
        return False
        
def sacarDonantesTipoSangre(sangre,matriz):
    donantes = []
    for i in matriz:
        if i[3] == sangre:
            donantes.append(i)
    return donantes

def sacarDonantesActivos(matriz):
    donantes = []
    for i in matriz:
        if i[8] == 1:
           donantes.append(i)
    return donantes 

def sacarMujeresONegativo(matriz):
    donantes = []
    for i in matriz:
        if i[4] == False and i[3] == "O-":
           donantes.append(i)
    return donantes

def sacarAquienPuedeDonar(sangre, matriz):
    donantes = []
    for i in matriz:
        if sangre == "O-":
            donantes.append(i)
        elif sangre == "O+":
            if i[3] in ["O+","A+","B+","AB+"]:
                donantes.append(i)
        elif sangre == "A-":
            if i[3] in ["A-","A+","AB-","AB+"]:
                donantes.append(i)
        elif sangre == "A+":
            if i[3] in ["A+","AB+"]:
                donantes.append(i)
        elif sangre == "B-":
            if i[3] in ["B-","B+","AB-","AB+"]:
                donantes.append(i)
        elif sangre == "B+":
            if i[3] in ["B+", "AB+"]:
                donantes.append(i)
        elif sangre == "AB-":
            if i[3] in ["AB-","AB+"]:
                donantes.append(i)
        else:
            if i[3] == "AB+":
                donantes.append(i)
    return donantes

def sacarDeQuienPuedeRecibir(sangre, matriz):
    donantes = []
    for i in matriz:
        if sangre == "AB+":
            donantes.append(i)
        elif sangre == "AB-":
            if i[3] in ["O-","A-","B-","AB-"]:
                donantes.append(i)
        elif sangre == "B+":
            if i[3] in ["O-","O+","B-","B+"]:
                donantes.append(i)
        elif sangre == "B-":
            if i[3] in ["O-","B-"]:
                donantes.append(i)
        elif sangre == "A+":
            if i[3] in ["O-","O+","A-","A+"]:
                donantes.append(i)
        elif sangre == "A-":
            if i[3] in ["O-", "A-"]:
                donantes.append(i)
        elif sangre == "O+":
            if i[3] in ["O-","O+"]:
                donantes.append(i)
        else:
            if i[3] == "O-":
                donantes.append(i)
    return donantes

def sacarNoActivos(matriz):
    donantes = []
    for i in matriz:
        if i[8] == 0:
           donantes.append(i)
    return donantes 

def reportePlantillaCorta(donantes,nomReporte):
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M %p")
    doc = dominate.document(title='Reporte por '+nomReporte)
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel="preconnect", href="https://fonts.gstatic.com/%22")
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Abel&display=swap%22")

    with doc:
        with div(id='header'):
            h1("Donadores por "+nomReporte)
            h2('Fecha: '+fecha)
            h2('Hora: '+hora)
            
        with div(cls='body'):
            with table(cls='tabla'):
                with tr(cls="titulos"):
                    th('Cédula')
                    th('Nombre Completo')
                    th('Fecha de Nacimiento')
                    th('Teléfono')
                    th('Correo') 
                for i in donantes:
                    with tr():
                        th(i[0])
                        th(i[1])
                        th(i[2])
                        th(i[6])
                        th(i[7])
    return str(doc)

def reporteSangre(donantes,nomReporte):
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M %p")
    doc = dominate.document(title='Reporte '+nomReporte)
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel="preconnect", href="https://fonts.gstatic.com/%22")
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Abel&display=swap%22")

    with doc:
        with div(id='header'):
            h1("Donadores "+nomReporte)
            h2('Fecha: '+fecha)
            h2('Hora: '+hora)
            
        with div(cls='body'):
            with table(cls='tabla'):
                with tr(cls="titulos"):
                    th('Cédula')
                    th('Nombre Completo')
                    th('Tipo de sangre')
                    th('Teléfono')
                    th('Correo') 
                for i in donantes:
                    with tr():
                        th(i[0])
                        th(i[1])
                        th(i[3])
                        th(i[6])
                        th(i[7])
    return str(doc)

def reporteTotal(donantes):
    
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M %p")
    doc = dominate.document(title='Reporte del total de donadores')
    
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel="preconnect", href="https://fonts.gstatic.com/%22")
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Abel&display=swap%22")

    with doc:
        with div(id='header'):
            h1("Total de donadores")
            h2('Fecha: '+fecha)
            h2('Hora: '+hora)
            
        with div(cls='body'):
            with table(cls='tabla'):
                with tr(cls="titulos"):
                    th('Cédula')
                    th('Nombre Completo')
                    th('Fecha de Nacimiento')
                    th('Tipo de sangre')
                    th('Sexo')
                    th('Peso')
                    th('Teléfono')
                    th('Correo') 
                for i in donantes:
                    with tr():
                        th(i[0])
                        th(i[1])
                        th(i[2])
                        th(i[3])
                        th(traducirSexo(i[4]))
                        th(str(i[5])+" Kg")
                        th(i[6])
                        th(i[7])
    return str(doc)

def reporteNoActivos(donantes):
    """
    funcionamiento: 
    """
    fecha = datetime.today().strftime('%d/%m/%Y')
    hora = datetime.now().strftime("%I:%M %p")
    doc = dominate.document(title='Reporte del total de donadores no activos')
    
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel="preconnect", href="https://fonts.gstatic.com/%22")
        link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Abel&display=swap%22")

    with doc:
        with div(id='header'):
            h1("Total de donadores no activos")
            h2('Fecha: '+fecha)
            h2('Hora: '+hora)
            
        with div(cls='body'):
            with table(cls='tabla'):
                with tr(cls="titulos"):
                    th('Justificación')
                    th('Cédula')
                    th('Nombre Completo')
                    th('Fecha de Nacimiento')
                    th('Tipo de sangre')
                    th('Sexo')
                    th('Peso')
                    th('Teléfono')
                    th('Correo') 
                for i in donantes:
                    with tr():
                        th(traducirJustificacion(i[-1]))
                        th(i[0])
                        th(i[1])
                        th(i[2])
                        th(i[3])
                        th(traducirSexo(i[4]))
                        th(str(i[5])+" Kg")
                        th(i[6])
                        th(i[7])
    return str(doc)


def abrirPage(nombreFile):
    webbrowser.open_new_tab(nombreFile)


def reporteAquienPuedeDonarES(sangre, matriz):
    crearArchivo("aquienDonar.html",reporteSangre(sacarAquienPuedeDonar(sangre,sacarDonantesActivos(matriz)),"a quien puedo donar"))
    abrirPage("aquienDonar.html")

def reporteDeQuienPuedeRecibirES(sangre,matriz):
    crearArchivo("dequienRecibir.html",reporteSangre(sacarDeQuienPuedeRecibir(sangre,sacarDonantesActivos(matriz)),"de quien puedo recibir"))
    abrirPage("dequienRecibir.html")

def reporteNoActivosES(matriz):
    crearArchivo("noActivos.html",reporteNoActivos(sacarNoActivos(matriz)))
    abrirPage("noActivos.html")

#reporteNoActivosES(matriz)    
#reporteAquienPuedeDonarES("O-",matriz)