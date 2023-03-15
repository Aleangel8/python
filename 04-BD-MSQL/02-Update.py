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

# UPDATE
cursor.execute("UPDATE * FROM db.Customers WHERE CustomerID = 'DEM18'")


cursor.execute("SELECT * FROM dbo.Customers SET CompanyName = 'Los Nachos, SL'")


exit()

# DELETE
cursor.execute("DELETE * FROM db.Customers WHERE CustomerID = 'DEM18'")
connection.commit()

# Al terminar el programa se cierra sola la conexion pero los suyo es cerrarla y abrirla
connection.close()