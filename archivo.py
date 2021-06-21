#Creado por: César Jiménez Salazar y Maynor Erks Martínez Hernández.
#Fecha de realización:05/06/2021 07:21 p.m
#Última modificación:21/06/2021 10:59  a.m
#Versión: 3.9.5
import pickle
def leerDatos(nomArchLeer):
    """
    Funcionamiento: Lee los datos guardados en memoria secundaria
    Entradas: El nombre del archivos
    Salidas: La base de datoss cargada. 
    """
    matriz=[]
    try:
        f=open(nomArchLeer,"rb")
        matriz = pickle.load(f)
        f.close()
    except:
        print("No se ha encontrado datos registrados en: ", nomArchLeer)
    return matriz

def guardarDatos(nomArchGrabar,matriz):
    """
    Funcionamiento: Almacena datos en memoria secuandaria
    Entradas: El nombre del archivos, los datos a almacenar
    Salidas: Confirmación. 
    """
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(matriz,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
    return
