import pymssql


#Establecer conexion con la base de datos
connection = pymssql.connect(
    server= "host-sqlserver-eoi.database.windows.net",
    user="Administrador",
    password="azurePa$$w0rd",
    database= "Northwind")

# Creamos un cursor para ejecutar cuando en la base de datos
# Retornar Tuplas
cursor = connection.cursor()

# Retorna Diccionarios
cursor = connection.cursor(as_dict=True)

#  Ejemplos de comandos SELECT, para recuperar registros de la base de datos

cursor.execute("SELECT CustomerID, CompanyName, Country FROM dbo.Customers ORDER BY Country")
cursor.execute("SELECT * FROM dbo.Customers")



# Mostrar el contenido del cursor mediante un while
row = cursor.fetchone()
while(row):
    print(f"ID:  {row['CustomerID']:>10}")
    print(f"Empresa:  {row['CompanyName']} - {row['Country']}\n")
    row = cursor.fetchone()


print("==============================")

cursor.execute("SELECT * FROM dbo.Customers")


# Mostramos el contenido del cursor mediante un for
for row in cursor.fetchall():
    #Si trabajamos con tuplas
    #print(f"ID:  {row[0]:>10}")
    #print(f"Empresa:  {row[1]}\n")
    print(f"ID:  {row['CustomerID']:>10}")
    print(f"Empresa:  {row['CompanyName']} - {row['Country']}\n")



exit()
# Insertamos datos usando INSERT
cursor.execute("INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, City, Country) VALUES ('DEM18', 'Comidas 1 2 3, SL', 'Borja Cabeza', 'Madrid', 'Spain')")
# Utilizamos la función commit() para confirmar la transación y las operaciones de inserción
# actualización y borrado
connection.commit()


# Insertamos varios usando comodines
command = "INSERT INTO dbo.Customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
command = "INSERT INTO dbo.Customers(CustomerID, CompanyName, City, Country) VALUES (%d, %d, %d, %d)"

data = []
data.append(('DEA10', 'Empresa Uno SL', 'Madrid', 'Spain'))
data.append(('DEA20', 'Empresa Dos SL', 'Valencia', 'Spain'))
data.append(('DEA30', 'Empresa Tes SL', 'Badajoz', 'Spain'))

cursor.executemany(command, data)
connection.commit()
print(f"Número de filas insertadas: {cursor.rowcount}")


# Utilizamos la función rollback() para cancelar la transación y anular las operaciones de 
# inserción, actualización y borrado
connection.rollback()



# Ejemplos de comandos SELECT, para recuperar registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'Spain'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "Spain")

cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'Spain' ORDER BY City")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY City", "Spain")

pais = "Spain"
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d ORDER BY City", pais)

cursor.execute("SELECT * FROM dbo.Customers ORDER BY Country, City")
cursor.execute("SELECT CustomerID, CompanyName, Country, City FROM dbo.Customers WHERE Country = %d", "Spain")