from bs4 import BeautifulSoup
import re


# Open file html
with open("D:\Automatica\!!!programming route\Proyectos Web\MyPageTest\index.html","r") as f:
    doc = BeautifulSoup(f, "html.parser")

# Read the document
#print(doc.prettify())


# Read the tag
tag_title = doc.title

# Read the tag
print(tag_title)

# Modified the tag
tag_title.string= "Mi first page"

# Read inside the tag
print(tag_title.string)

# Recoge todas las a references
tags = doc.find_all("a")

# pinta los atributos como dictionary
print(tags[1].attrs)

# Cambia el valor del atrivuto href 
tags[1]['href']="micuentanew.html"

# Añade el atributo color si no existe
tags[1]['color']="blue"

print(tags[1])


# apuntando a clases
tag_class= doc.find_all(class_="subtitulo")
print(tag_class)

# Expresion regular
tag_dollar = doc.find_all(string= re.compile("\$.*"), limit=1)#Solo 1
#print(tag_dollar)

# Remueve todo y solo muestra el contenido
for tag in tag_dollar:
    print(tag.strip())

# Modificar el archivo html
tag_inputs = doc.find_all("input", type="text")
for tag in tag_inputs:
    tag['name']="new_name3"


# Abre un nuevo archivo con la modificación
with open("D:\Automatica\!!!programming route\Proyectos Web\MyPageTest\changed.html","w") as file:
    file.write(str(doc))