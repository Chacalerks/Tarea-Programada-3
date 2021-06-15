from bs4 import BeautifulSoup

lista=[]
def leerXML():
    with open('prueba.xml', 'r') as f:
        data = f.read()
    Bs_data = BeautifulSoup(data, "xml")
    NombreSubTipo = Bs_data.find_all('NombreSubTipo')
    for i in NombreSubTipo:
        lista.append(i.text[9:][:2])
    return lista

lista = leerXML()
print(lista)