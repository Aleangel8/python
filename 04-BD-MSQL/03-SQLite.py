import sqlite3, json

# Establecemos conexion conla base de datos, indicamos la ruta del fichero
# Si el fichero no existe se crea
connection = sqlite3.connect("demo.db")

# Creamos un cursor que nos permite conectarnos a la DB con comandos
cursor = connection.cursor()

# Lanzar Consulta de existencia de tabla, de no existir se crea
command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name ='Alumnos'" 
cursor.execute(command)
numTables = cursor.fetchone()[0]
print(f"Numero de tablas Alumnos: {numTables}")

if (numTables == 0):
    command = "CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)"
    cursor.execute(command)





# Consultar datos con SELECT
command = "SELECT * FROM Alumnos"    
"""
cursor.execute(command)
row = cursor.fetchone()
while(row):
    print(row)
    row = row.cursor.fetchone()
"""
print("")

cursor.execute(command)
for row in cursor.fetchall():
    print(row)


exit()
# Insertamos datos utilizando INSERT
command = "Insert INTO Alumnos (id, nombre) VALUES ('000', 'Borja')"
cursor.execute(command)
connection.commit()

# Insertamos varios registros
lista = [

    ('002', 'Ana', 'Trujillo', '2C', None),

    ('003', 'Adrian', 'Sánz', '2A', json.dumps([7.5, 6, 9, 5, 6.9])),

    ('004', 'María', 'Sánchez', '2B', None),

]

command = "INSERT INTO Alumnos VALUES (?, ?, ?, ?, ?)"
cursor.executemany(command, lista)
connection.commit()
print("Numero de registros insertados:", cursor.rowcount)

# Actualizar un registro utilizando UPDATE
command = "UPDATE Alumnos SET apellidos = 'Cabeza' WHERE id = '000'"
cursor.execute(command)
connection.commit()
print(" Numero de registros modificados: ",cursor.rowcount)

# Modificar un registro utilizando DELETE
command = "DELETE FROM Alumnos WHERE id = '004'"
cursor.execute(command)
connection.commit()
print(" Numero de registros modificados: ",cursor.rowcount)
#Crear tabla de profesores
command = "CREATE TABLE Profesores (id integer, salario real, nombre text, apellidos text, curso text, foto blob)"
cursor.execute(command)