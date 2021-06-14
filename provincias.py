import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

nodo1 = ET.SubElement(doc, "nodo1", name="nodo")
nodo1.text = "Texto de nodo1"

ET.SubElement(doc, "nodo2", atributo="algo").text = "texto 2"

arbol = ET.ElementTree(root)
arbol.write("./prueba.xml")